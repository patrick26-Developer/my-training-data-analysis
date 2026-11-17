"""Exercices 8.4 — Algorithmes classiques.

Écris les fonctions demandées SANS utiliser les raccourcis de Python quand c'est précisé
(pas de sorted/sort/min/max/index pour les tris et recherches).
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex31_algorithmes_classiques.py -v
"""


# Exercice 1
# Écris `recherche_lineaire(liste, cible)` : retourne l'indice de la PREMIÈRE occurrence, ou -1.


# Exercice 2
# Écris `dichotomie(liste_triee, cible)` : retourne un indice de `cible` dans une liste TRIÉE
# (ordre croissant), ou -1. Vise O(log n).


# Exercice 3
# Écris `tri_a_bulles(liste)` : retourne une NOUVELLE liste triée (croissant) sans modifier l'originale.


# Exercice 4
# Écris `tri_insertion(liste)` : idem avec le tri par insertion.


# Exercice 5
# Écris `crible(n)` : retourne la liste des nombres premiers <= n (crible d'Ératosthène).


# Exercice 6
# Écris `fibonacci_liste(n)` : retourne la liste des n premiers termes de Fibonacci
# (0, 1, 1, 2, 3, ...). fibonacci_liste(6) -> [0, 1, 1, 2, 3, 5]


# Exercice 7
# Écris `est_palindrome(texte)` : ignore la casse, les espaces et la ponctuation.
# est_palindrome("Esope reste ici et se repose") -> True


# Exercice 8
# Écris `a_des_doublons(liste)` : True si un élément apparaît plus d'une fois (utilise un set).


# Exercice 9
# Écris `deux_sommes(nombres, cible)` : retourne un couple d'indices (i, j) avec i < j tels que
# nombres[i] + nombres[j] == cible, ou None. Vise O(n) avec un dictionnaire.
# deux_sommes([2, 7, 11, 15], 9) -> (0, 1)


# Exercice 10
# Écris `rendre_monnaie(montant, pieces)` : retourne le NOMBRE MINIMAL de pièces pour atteindre
# `montant` (pieces : liste de valeurs, par exemple [500, 100, 50, 25]) avec l'algorithme glouton
# (on prend toujours la plus grande pièce possible). Retourne le dictionnaire {piece: nombre}.
# rendre_monnaie(675, [500, 100, 50, 25]) -> {500: 1, 100: 1, 50: 1, 25: 1}


# Exercice 11
# Écris `nombre_de_chiffres_binaires(n)` : retourne l'écriture binaire (texte) de l'entier n >= 0,
# sans utiliser bin(). nombre_de_chiffres_binaires(10) -> "1010" ; (0) -> "0"
