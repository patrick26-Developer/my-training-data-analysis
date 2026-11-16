"""Exercices 7.3 — venv et pip (fichiers de dépendances).

Tu vas écrire de petits outils qui manipulent un fichier requirements.txt.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex26_venv_et_pip.py -v
"""


# Exercice 1
# Écris `nom_du_paquet(ligne)` : extrait le nom d'un paquet dans une ligne de requirements.
#   "requests==2.32.5" -> "requests" ; "pandas>=2.0" -> "pandas" ; "numpy" -> "numpy"
#   "fastapi[standard]==0.1" -> "fastapi"
# Les opérateurs possibles : ==, >=, <=, >, <, ~=, !=


# Exercice 2
# Écris `lire_requirements(chemin)` : retourne la liste des lignes utiles du fichier :
# sans espaces aux bords, en ignorant les lignes vides et les commentaires (commençant par #).


# Exercice 3
# Écris `versions_figees(chemin)` : retourne un dictionnaire {nom: version} pour les lignes de la
# forme "nom==version" (les autres lignes sont ignorées).


# Exercice 4
# Écris `non_figes(chemin)` : retourne la liste TRIÉE des noms de paquets dont la ligne n'est PAS
# de la forme "nom==version" (donc non figés).


# Exercice 5
# Écris `ajouter_dependance(chemin, ligne)` : ajoute `ligne` au fichier si le NOM du paquet n'y est pas
# déjà (le fichier peut ne pas exister). Retourne True si ajoutée, False sinon.


# Exercice 6
# Écris `commande_creation_venv(nom="venv")` : retourne la commande texte pour créer l'environnement :
#   "python -m venv venv"


# Exercice 7
# Écris `gitignore_contient_venv(chemin)` : retourne True si le fichier .gitignore contient une ligne
# "venv/" ou ".venv/" (ou "venv" / ".venv"). Fichier absent : False.
