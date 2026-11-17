"""Génère catalogue/catalogue.json à partir de catalogue/tarifs.toml et du contenu des parcours.

Le catalogue contient, pour chaque parcours : titre, niveau, crédits, nombre de modules/leçons/exercices,
durée estimée, et le prix en FCFA, en euro et en dollar (le MÊME prix exprimé en trois monnaies).
Il décrit aussi la phase de lancement gratuite et la date de passage au premium.

Les prix sont toujours ramenés dans la fourchette [prix_plancher ; prix_plafond] du fichier de tarifs.

Usage :  python outils/generer_catalogue.py
"""

import calendar
import json
import re
import tomllib
from datetime import date, timedelta
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CATALOGUE = RACINE / "catalogue"


def arrondir(montant: float, pas: float) -> float:
    return round(montant / pas) * pas


def borner(montant: float, plancher: int, plafond: int) -> int:
    return int(min(max(montant, plancher), plafond))


def ajouter_mois(depart: date, mois: int) -> date:
    index = depart.month - 1 + mois
    annee, mois_cible = depart.year + index // 12, index % 12 + 1
    jour = min(depart.day, calendar.monthrange(annee, mois_cible)[1])
    return date(annee, mois_cible, jour)


def phase_de_lancement(config: dict, aujourdhui: date | None = None) -> dict:
    """Décrit la phase gratuite et indique la phase en cours si la date d'ouverture est connue."""
    aujourdhui = aujourdhui or date.today()
    ouverture_txt = config.get("date_ouverture", "")
    resultat = {
        "gratuit_mois": config["gratuit_mois"],
        "gratuit_jours": config.get("gratuit_jours", 0),
        "telechargements_gratuits": config["telechargements_gratuits"],
        "date_ouverture": ouverture_txt or None,
        "date_debut_premium": None,
        "date_annonce_premium": None,
        "phase_actuelle": "a_definir",
    }
    if not ouverture_txt:
        return resultat
    ouverture = date.fromisoformat(ouverture_txt)
    debut_premium = ajouter_mois(ouverture, config["gratuit_mois"]) + timedelta(
        days=config.get("gratuit_jours", 0)
    )
    annonce = debut_premium - timedelta(days=config["annonce_avant_jours"])
    resultat["date_debut_premium"] = debut_premium.isoformat()
    resultat["date_annonce_premium"] = annonce.isoformat()
    if aujourdhui < ouverture:
        resultat["phase_actuelle"] = "avant_ouverture"
    elif aujourdhui < debut_premium:
        resultat["phase_actuelle"] = "lancement_gratuit"
    else:
        resultat["phase_actuelle"] = "premium"
    return resultat


def prix_multidevises(prix_xaf: int, general: dict) -> dict:
    """Le même prix en XAF, EUR et USD (équivalence, arrondie à 0,50)."""
    eur_exact = prix_xaf / general["parite_euro"]
    pas = general["arrondi_devises"]
    return {
        "XAF": prix_xaf,
        "EUR": arrondir(eur_exact, pas),
        "USD": arrondir(eur_exact * general["usd_pour_1_eur"], pas),
    }


def lire_parcours(code: str, config: dict) -> dict:
    dossier = next((RACINE / "parcours").glob(f"{code}_*"))
    readme = (dossier / "README.md").read_text(encoding="utf-8")
    titre = re.sub(r"^#\s*", "", readme.splitlines()[0]).strip()
    niveau = re.search(r"\*\*Niveau :\*\*\s*([^·\n]+)", readme)
    credits = re.search(r"\*\*Crédits :\*\*\s*(\d+)", readme)
    lecons = sorted((dossier / "lecons").glob("*.md"))
    minutes = 0
    for lecon in lecons:
        trouve = re.search(r"⏱\s*(?:Durée\s*:\s*)?(\d+)\s*min", lecon.read_text(encoding="utf-8"))
        minutes += int(trouve.group(1)) if trouve else 0
    exercices = [
        f for f in (dossier / "exercices").glob("ex*.py") if not f.name.startswith("test_")
    ]
    modules = len(set(re.findall(r"^\|\s*(M\d+)\s*\|", readme, re.M)))
    return {
        "id": code,
        "dossier": dossier.name,
        "titre": titre,
        "titre_court": config["titre_court"],
        "statut": config["statut"],
        "niveau": niveau.group(1).strip() if niveau else "",
        "credits": int(credits.group(1)) if credits else None,
        "promesse": config["promesse"],
        "pour_qui": config["pour_qui"],
        "modules": modules,
        "lecons": len(lecons),
        "exercices": len(exercices),
        "duree_estimee_heures": round(minutes / 60, 1) if minutes else None,
        "apercu_gratuit": config.get("apercu_gratuit", []),
        "prix_base": config["prix_base"],
    }


def main() -> None:
    config = tomllib.loads((CATALOGUE / "tarifs.toml").read_text(encoding="utf-8"))
    general = config["general"]
    plancher, plafond, pas = general["prix_plancher"], general["prix_plafond"], general["arrondi"]
    differencier = config["publics_options"]["differencier_par_public"]

    def prix(montant: float, nombre_de_cours: int = 1) -> dict:
        """Prix arrondi puis borné : le plafond s'applique PAR COURS (un pack de 3 cours : 3 plafonds)."""
        borne = borner(arrondir(montant, pas), plancher, plafond * nombre_de_cours)
        return prix_multidevises(borne, general)

    publics_actifs = config["publics"] if differencier else {"tous": {"coefficient": 1.0}}

    parcours = []
    for code, cfg in config["parcours"].items():
        if not plancher <= cfg["prix_base"] <= plafond:
            raise SystemExit(
                f"Le prix de base de {code} ({cfg['prix_base']}) sort de la fourchette "
                f"[{plancher} ; {plafond}] XAF."
            )
        p = lire_parcours(code, cfg)
        p["prix"] = {
            public: prix(cfg["prix_base"] * infos["coefficient"])
            for public, infos in publics_actifs.items()
        }
        parcours.append(p)

    licences = {}
    for code, lic in config["licences"].items():
        licences[code] = {
            "libelle": lic["libelle"],
            "minimum_places": lic["minimum_places"],
            "justificatif": lic["justificatif"],
            "paliers": lic["paliers"],
            "prix_par_place": {
                p["id"]: [
                    {
                        "a_partir_de": palier["a_partir_de"],
                        "prix": prix(p["prix_base"] * lic["coefficient"] * (1 - palier["remise"])),
                    }
                    for palier in lic["paliers"]
                ]
                for p in parcours
            },
        }

    packs = []
    for pack in config.get("packs", []):
        sommes = sum(
            next(p for p in parcours if p["id"] == c)["prix_base"] for c in pack["parcours"]
        )
        prix_pack = prix(sommes * (1 - pack["remise"]), len(pack["parcours"]))
        packs.append(
            {
                "id": pack["id"],
                "libelle": pack["libelle"],
                "parcours": pack["parcours"],
                "remise": pack["remise"],
                "prix": prix_pack,
                "economie_xaf": int(arrondir(sommes, pas) - prix_pack["XAF"]),
            }
        )

    sortie = {
        "avertissement": "Prix de départ à valider par l'auteur avant toute mise en vente.",
        "strategie": "Volume : prix bas et identiques pour tous, ajustables selon l'effectif des utilisateurs.",
        "devise_reference": general["devise"],
        "fourchette_prix_xaf": {"plancher": plancher, "plafond": plafond},
        "devises_affichees": ["XAF", "EUR", "USD"],
        "taux": {"eur_xaf": general["parite_euro"], "usd_pour_1_eur": general["usd_pour_1_eur"]},
        "duree_acces_mois": general["duree_acces_mois"],
        "lancement": phase_de_lancement(config["lancement"]),
        "differencier_par_public": differencier,
        "publics": {
            k: {x: v[x] for x in ("libelle", "coefficient", "justificatif", "description")}
            for k, v in config["publics"].items()
        },
        "parcours": parcours,
        "licences": licences,
        "packs": packs,
    }
    cible = CATALOGUE / "catalogue.json"
    cible.write_text(json.dumps(sortie, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lancement = sortie["lancement"]
    print(f"OK {cible.relative_to(RACINE)} : {len(parcours)} parcours, {len(packs)} packs")
    print(
        f"   lancement : {lancement['phase_actuelle']} (premium dès {lancement['date_debut_premium']})"
    )
    for p in parcours:
        tarif = p["prix"][next(iter(p["prix"]))]
        print(
            f"   {p['id']} {p['titre_court']:<20} {p['lecons']:>3} leçons"
            f" | {tarif['XAF']} FCFA = {tarif['EUR']} EUR = {tarif['USD']} USD"
        )


if __name__ == "__main__":
    main()
