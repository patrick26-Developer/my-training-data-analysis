"""Exercices 8.3 — Tableaux à deux dimensions.

Un tableau est une liste de listes de nombres, de taille rectangulaire.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex30_tableaux_2d.py -v
"""


# Exercice 1
# Écris `creer_grille(lignes, colonnes, valeur=0)` : retourne un tableau lignes x colonnes
# rempli de `valeur`, dont les lignes sont INDÉPENDANTES.


# Exercice 2
# Écris `colonne(tableau, j)` : retourne la liste des valeurs de la colonne j.


# Exercice 3
# Écris `totaux_lignes(tableau)` et `totaux_colonnes(tableau)` : retournent les listes de sommes.


# Exercice 4
# Écris `transposer(tableau)` : retourne la transposée (liste de listes).


# Exercice 5
# Écris `somme_matrices(a, b)` : somme case par case de deux tableaux de même taille.


# Exercice 6
# Écris `produit_matrices(a, b)` : produit matriciel (a de taille n x m, b de taille m x p).


# Exercice 7
# Écris `identite(n)` : matrice identité n x n.


# Exercice 8
# Écris `determinant_2x2(m)` et `determinant_3x3(m)` (règle de Sarrus ou développement).
# determinant_2x2([[1, 2], [3, 4]]) -> -2


# Exercice 9
# Écris `diagonale_principale(m)` : liste des éléments m[i][i] d'un tableau carré, et
# `trace(m)` : leur somme.


# Exercice 10
# Écris `tourner_90(m)` : retourne le tableau tourné de 90° dans le sens des aiguilles d'une montre.
# tourner_90([[1, 2], [3, 4]]) -> [[3, 1], [4, 2]]
# Indice : transposer puis inverser chaque ligne.


# Exercice 11
# Écris `gagnant_morpion(grille)` : `grille` est un tableau 3x3 de "X", "O" ou " ".
# Retourne "X" ou "O" si un joueur a aligné 3 symboles (ligne, colonne ou diagonale), sinon None.
