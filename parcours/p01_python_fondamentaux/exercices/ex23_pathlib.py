"""Exercices 6.4 — pathlib.

Les fonctions reçoivent un dossier ou un chemin (objets `Path` ou textes). Convertis avec Path(...).
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex23_pathlib.py -v
"""

# N'oublie pas : from pathlib import Path


# Exercice 1
# Écris `extension(chemin)` : retourne l'extension SANS le point, en minuscules ("" s'il n'y en a pas).
# extension("rapport.PDF") -> "pdf" ; extension("Makefile") -> ""


# Exercice 2
# Écris `changer_extension(chemin, nouvelle)` : retourne un NOUVEAU chemin (Path) avec une autre
# extension (donnée sans point). changer_extension("a/b.txt", "md") -> Path("a/b.md")


# Exercice 3
# Écris `creer_arborescence(racine, noms)` : crée dans `racine` un sous-dossier pour chaque nom
# de `noms` (sans erreur si ils existent déjà). Retourne le nombre de dossiers présents ensuite.


# Exercice 4
# Écris `lister_csv(dossier)` : retourne la liste TRIÉE des NOMS (str) des fichiers .csv du dossier
# (non récursif).


# Exercice 5
# Écris `lister_python(dossier)` : retourne la liste TRIÉE des NOMS des fichiers .py du dossier
# et de TOUS ses sous-dossiers (récursif).


# Exercice 6
# Écris `taille_totale(dossier)` : retourne la somme des tailles (en octets) de tous les fichiers
# du dossier et de ses sous-dossiers.


# Exercice 7
# Écris `ranger_par_extension(dossier)` : déplace chaque fichier du dossier (non récursif) dans un
# sous-dossier portant le nom de son extension (sans point) ; "sans_extension" s'il n'en a pas.
# Retourne un dictionnaire {extension: nombre_de_fichiers}.
# Indice : fichier.rename(sous_dossier / fichier.name)


# Exercice 8
# Écris `dossier_du_script()` : retourne le dossier (Path) qui contient CE fichier (utilise __file__).
