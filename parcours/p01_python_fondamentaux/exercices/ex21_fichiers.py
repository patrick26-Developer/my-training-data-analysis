"""Exercices 6.2 — Lire et écrire des fichiers.

Toutes les fonctions reçoivent le CHEMIN du fichier en paramètre (les tests utilisent un dossier temporaire).
Utilise `with open(..., encoding="utf-8")`.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex21_fichiers.py -v
"""


# Exercice 1
# Écris `ecrire_lignes(chemin, lignes)` : écrit chaque élément de `lignes` sur sa propre ligne
# (écrase le fichier s'il existe).


# Exercice 2
# Écris `lire_lignes(chemin)` : retourne la liste des lignes SANS le "\n" final, en ignorant
# les lignes vides. Si le fichier n'existe pas, retourne [].


# Exercice 3
# Écris `ajouter_ligne(chemin, ligne)` : ajoute `ligne` à la fin du fichier (le crée si besoin),
# suivie d'un retour à la ligne.


# Exercice 4
# Écris `compter_lignes(chemin)` : retourne le nombre de lignes non vides du fichier
# (lecture ligne par ligne). Fichier absent : 0.


# Exercice 5
# Écris `compter_mots(chemin)` : retourne le nombre total de mots du fichier (séparés par des espaces).


# Exercice 6
# Écris `valeur_du_stock(chemin)` : chaque ligne du fichier a la forme "produit;prix;quantite".
# Retourne la somme de prix * quantite (entiers). Ignore les lignes vides.


# Exercice 7
# Écris `copier_en_majuscules(source, destination)` : écrit dans `destination` le contenu de `source`
# en MAJUSCULES.


# Exercice 8
# Écris `derniere_ligne(chemin)` : retourne la dernière ligne non vide (sans "\n"), ou None si
# le fichier est vide ou absent.
