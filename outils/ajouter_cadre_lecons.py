"""Ajoute (ou met à jour) un cadre motivant au début et à la fin des leçons d'un parcours.

Au début  : un encadré « Pourquoi tu vas aimer cette leçon » avec une accroche.
À la fin  : un encadré « Bravo ! » avec un mot d'encouragement et un lien vers la leçon suivante.

Les textes viennent de outils/cadres_p01.json (modifiables à la main). Le script est idempotent :
les blocs sont délimités par des commentaires HTML et remplacés à chaque exécution.

Usage :  python outils/ajouter_cadre_lecons.py p01_python_fondamentaux
"""

import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DEBUT = ("<!-- cadre:debut -->", "<!-- /cadre:debut -->")
FIN = ("<!-- cadre:fin -->", "<!-- /cadre:fin -->")


def titre(chemin: Path) -> str:
    premiere = chemin.read_text(encoding="utf-8").splitlines()[0]
    return re.sub(r"^#+\s*", "", premiere).strip()


def nettoyer(texte: str) -> str:
    for ouvrant, fermant in (DEBUT, FIN):
        texte = re.sub(
            rf"\n*{re.escape(ouvrant)}.*?{re.escape(fermant)}\n*", "\n\n", texte, flags=re.S
        )
    return texte.rstrip() + "\n"


def cadre_debut(accroche: str) -> str:
    return f"{DEBUT[0]}\n> 🔥 **Pourquoi tu vas aimer cette leçon** — {accroche}\n{DEBUT[1]}"


def cadre_fin(bravo: str, suivante: Path | None) -> str:
    suite = "Tu as terminé ce parcours. Prochaine étape : le parcours suivant !"
    if suivante is not None:
        suite = f"**Prochaine étape :** [{titre(suivante)}]({suivante.name})."
    return (
        f"{FIN[0]}\n---\n\n## 🎉 Bravo !\n\n{bravo}\n\n"
        f"💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants »,"
        f" refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*\n\n{suite}\n{FIN[1]}"
    )


def main(parcours: str) -> None:
    dossier = RACINE / "parcours" / parcours / "lecons"
    textes = json.loads((RACINE / "outils" / "cadres_p01.json").read_text(encoding="utf-8"))
    lecons = sorted(dossier.glob("l[0-9][0-9]_*.md"))
    for i, chemin in enumerate(lecons):
        cle = chemin.name[:3]
        if cle not in textes:
            continue
        accroche, bravo = textes[cle]
        suivante = lecons[i + 1] if i + 1 < len(lecons) else None
        texte = nettoyer(chemin.read_text(encoding="utf-8"))
        lignes = texte.split("\n")
        # insère l'accroche juste après la ligne de métadonnées (⏱ …), sinon après le titre
        indice = next((k for k, ligne in enumerate(lignes[:6]) if ligne.startswith("⏱")), 0)
        lignes[indice + 1 : indice + 1] = ["", cadre_debut(accroche)]
        texte = "\n".join(lignes).rstrip() + "\n\n" + cadre_fin(bravo, suivante) + "\n"
        chemin.write_text(texte, encoding="utf-8")
        print("OK", chemin.name)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "p01_python_fondamentaux")
