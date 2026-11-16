"""Exercices 7.4 — Écrire ses modules.

Ici tu vas CRÉER un petit package dans un dossier temporaire à partir de texte, puis l'importer.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex27_ecrire_ses_modules.py -v
"""

# N'oublie pas : from pathlib import Path


# Exercice 1
# Écris `creer_module(dossier, nom, code)` : crée dans `dossier` un fichier `<nom>.py` contenant
# `code` (texte) et retourne le chemin (Path) du fichier créé.


# Exercice 2
# Écris `creer_package(dossier, nom, modules)` : crée un sous-dossier `nom` dans `dossier`, avec un
# fichier __init__.py vide, et un fichier <module>.py pour chaque (nom_module, code) du dictionnaire
# `modules`. Retourne le chemin (Path) du dossier du package.


# Exercice 3
# Écris `executable_directement(code)` : retourne True si le texte `code` contient la ligne
# `if __name__ == "__main__":` (en ignorant les espaces au début de ligne).


# Exercice 4
# Écris `importer_module(dossier, nom)` : importe dynamiquement le module `<nom>.py` situé dans
# `dossier` et retourne l'objet module (utilise importlib.util.spec_from_file_location,
# module_from_spec et spec.loader.exec_module).


# Exercice 5
# Écris `liste_des_fonctions(module)` : retourne la liste TRIÉE des noms des fonctions publiques
# (ne commençant pas par "_") définies dans le module (inspect.isfunction sur les attributs).
