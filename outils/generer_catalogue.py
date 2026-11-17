"""Génère catalogue/catalogue.json à partir de catalogue/tarifs.toml et du contenu des parcours.

Le catalogue contient, pour chaque parcours : titre, niveau, crédits, nombre de modules/leçons/exercices,
durée estimée (somme des « ⏱ N min » des leçons) et le prix pour chaque public.
Ta plateforme n'a qu'à lire catalogue.json : les chiffres sont toujours à jour avec le contenu.

Usage :  python outils/generer_catalogue.py
"""

import json
import re
import tomllib
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CATALOGUE = RACINE / "catalogue"


def arrondir(montant: float, pas: int) -> int:
    return int(round(montant / pas) * pas)


def lire_parcours(code: str, config: dict) -> dict:
    dossier = next((RACINE / "parcours").glob(f"{code}_*"))
    readme = (dossier / "README.md").read_text(encoding="utf-8")
    titre = re.sub(r"^#\s*", "", readme.splitlines()[0]).strip()
    niveau = re.search(r"\*\*Niveau :\*\*\s*([^·\n]+)", readme)
    credits = re.search(r"\*\*Crédits :\*\*\s*(\d+)", readme)
    lecons = sorted((dossier / "lecons").glob("*.md"))
    minutes = 0
    for lecon in lecons:
        trouve = re.search(r"⏱\s*(\d+)\s*min", lecon.read_text(encoding="utf-8"))
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
        "duree_estimee_heures": round(minutes / 60, 1)
        if minutes
        else None,  # None = non renseignée
        "apercu_gratuit": config.get("apercu_gratuit", []),
        "prix_base": config["prix_base"],
    }


def main() -> None:
    config = tomllib.loads((CATALOGUE / "tarifs.toml").read_text(encoding="utf-8"))
    general = config["general"]
    pas = general["arrondi"]
    parite = general["parite_euro"]

    parcours = []
    for code, cfg in config["parcours"].items():
        p = lire_parcours(code, cfg)
        p["prix"] = {
            public: arrondir(cfg["prix_base"] * infos["coefficient"], pas)
            for public, infos in config["publics"].items()
        }
        p["prix_eur_indicatif"] = {
            public: round(montant / parite, 2) for public, montant in p["prix"].items()
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
                        "prix": arrondir(
                            p["prix_base"] * lic["coefficient"] * (1 - palier["remise"]), pas
                        ),
                    }
                    for palier in lic["paliers"]
                ]
                for p in parcours
            },
        }

    prix_par_id = {p["id"]: p for p in parcours}
    packs = []
    for pack in config.get("packs", []):
        total = {
            public: sum(prix_par_id[c]["prix"][public] for c in pack["parcours"])
            for public in config["publics"]
        }
        packs.append(
            {
                "id": pack["id"],
                "libelle": pack["libelle"],
                "parcours": pack["parcours"],
                "remise": pack["remise"],
                "prix": {k: arrondir(v * (1 - pack["remise"]), pas) for k, v in total.items()},
                "economie": {
                    k: arrondir(v, pas) - arrondir(v * (1 - pack["remise"]), pas)
                    for k, v in total.items()
                },
            }
        )

    sortie = {
        "devise": general["devise"],
        "duree_acces_mois": general["duree_acces_mois"],
        "avertissement": "Prix de départ à valider par l'auteur avant toute mise en vente.",
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
    print(f"OK {cible.relative_to(RACINE)} : {len(parcours)} parcours, {len(packs)} packs")
    for p in parcours:
        print(
            f"  {p['id']} {p['titre_court']:<22} {p['lecons']:>3} leçons {p['duree_estimee_heures'] or 'n/d':>5} h"
            f" | particulier {p['prix']['particulier']:>6} | élève {p['prix']['eleve']:>6} | étudiant {p['prix']['etudiant']:>6}"
        )


if __name__ == "__main__":
    main()
