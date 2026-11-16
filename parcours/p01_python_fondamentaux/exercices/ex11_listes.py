"""Exercices 4.1 — Les listes.

Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex11_listes.py -v
"""


# Exercice 1
# Retourne la moyenne des nombres de la liste (float). Pour une liste vide, retourne 0.0.
# moyenne([10, 15, 20]) -> 15.0
def moyenne(nombres):
    raise NotImplementedError


# Exercice 2
# Retourne le plus grand ET le plus petit, sous forme de couple (plus_petit, plus_grand),
# SANS utiliser min() ni max() (parcours avec for).
# extremes([4, 9, 2, 7]) -> (2, 9)
def extremes(nombres):
    raise NotImplementedError


# Exercice 3
# Retourne une NOUVELLE liste triée du plus grand au plus petit, sans modifier l'originale.
# trier_decroissant([3, 1, 2]) -> [3, 2, 1]
def trier_decroissant(nombres):
    raise NotImplementedError


# Exercice 4
# Retourne une nouvelle liste sans doublons, en gardant l'ordre de première apparition.
# sans_doublons([1, 2, 1, 3, 2]) -> [1, 2, 3]
def sans_doublons(elements):
    raise NotImplementedError


# Exercice 5
# Retourne la liste des éléments à partir de l'indice `debut` jusqu'au bout, à l'envers.
# fin_inversee([1, 2, 3, 4, 5], 2) -> [5, 4, 3]
# Indice : une tranche suffit.
def fin_inversee(elements, debut):
    raise NotImplementedError


# Exercice 6
# Ajoute `produit` à la fin de `stock` s'il n'y est pas déjà (modifie la liste en place),
# puis retourne True si l'ajout a eu lieu, False sinon.
def ajouter_si_absent(stock, produit):
    raise NotImplementedError


# Exercice 7
# `matrice` est une liste de listes de nombres de même taille. Retourne la liste des sommes
# de chaque ligne. somme_des_lignes([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
def somme_des_lignes(matrice):
    raise NotImplementedError


# Exercice 8
# Retourne la transposée d'une matrice rectangulaire (les lignes deviennent des colonnes).
# transposee([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
def transposee(matrice):
    raise NotImplementedError
