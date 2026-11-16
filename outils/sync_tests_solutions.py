"""Génère les tests des solutions à partir des tests des exercices.

Pour chaque parcours/<p>/exercices/test_exNN_x.py, crée parcours/<p>/solutions/test_solNN_x.py
en remplaçant l'import `exNN_x` par `solNN_x`. Les tests d'exercice restent donc l'unique
source de vérité.

Usage :  python outils/sync_tests_solutions.py
"""

from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent / "parcours"


def main() -> None:
    for test_ex in sorted(RACINE.glob("*/exercices/test_ex*.py")):
        nom_sol = test_ex.name.replace("test_ex", "test_sol", 1)
        contenu = test_ex.read_text(encoding="utf-8")
        suffixe = test_ex.stem.removeprefix("test_ex")
        contenu = contenu.replace(f"from ex{suffixe} import", f"from sol{suffixe} import")
        contenu = contenu.replace(f"import ex{suffixe} as", f"import sol{suffixe} as")
        contenu = contenu.replace("Tests de l'exercice", "Tests des solutions")
        contenu = contenu.replace(
            "Ne modifie pas ce fichier", "Généré par outils/sync_tests_solutions.py"
        )
        cible = test_ex.parent.parent / "solutions" / nom_sol
        cible.write_text(contenu, encoding="utf-8")
        print(f"OK {cible.relative_to(RACINE.parent)}")


if __name__ == "__main__":
    main()
