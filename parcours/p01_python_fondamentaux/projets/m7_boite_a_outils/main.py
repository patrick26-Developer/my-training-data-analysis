"""Programme principal de la boîte à outils.

Lancement depuis la racine du dépôt :
    python -m parcours.p01_python_fondamentaux.projets.m7_boite_a_outils.main
(ou, dans ton propre projet : python -m outils.main)
"""

from datetime import date

from . import age_en_annees, est_palindrome, jours_restants, moyenne, nettoyer_nom, pgcd


def main() -> None:
    print("Nom nettoyé :", nettoyer_nom("  grâce   MARIE  "))
    print("Moyenne :", moyenne([12, 15, 9]))
    print("PGCD(48, 18) :", pgcd(48, 18))
    print(
        "« Esope reste ici et se repose » est un palindrome ?",
        est_palindrome("Esope reste ici et se repose"),
    )
    print("Âge pour une naissance le 15/08/1960 :", age_en_annees(date(1960, 8, 15)), "ans")
    print("Jours avant Noël 2026 :", jours_restants(date(2026, 12, 25)))


if __name__ == "__main__":
    main()
