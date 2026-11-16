"""Exercices 4.4 — Les ensembles.

Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex14_ensembles.py -v
"""


# Exercice 1
# Retourne le nombre d'éléments DIFFÉRENTS de la liste. nb_differents([1, 2, 2, 3, 1]) -> 3
def nb_differents(elements):
    raise NotImplementedError


# Exercice 2
# Retourne la liste TRIÉE des produits vendus dans les DEUX boutiques (listes en entrée).
# communs(["Riz", "Sel"], ["Sel", "Huile", "Riz"]) -> ["Riz", "Sel"]
def communs(boutique_a, boutique_b):
    raise NotImplementedError


# Exercice 3
# Retourne la liste TRIÉE des produits que A vend et que B ne vend pas.
def seulement_chez_a(boutique_a, boutique_b):
    raise NotImplementedError


# Exercice 4
# Retourne True si TOUTES les lettres de `mot` sont dans `lettres_permises`.
# mot_valide("riz", "zirabc") -> True ; mot_valide("rat", "riz") -> False
def mot_valide(mot, lettres_permises):
    raise NotImplementedError


# Exercice 5
# Retourne True si la phrase contient toutes les lettres de l'alphabet (pangramme),
# sans tenir compte de la casse. L'alphabet est "abcdefghijklmnopqrstuvwxyz".
def est_pangramme(phrase):
    raise NotImplementedError


# Exercice 6
# Retourne la liste des doublons (éléments présents plus d'une fois), triée, sans répétition.
# doublons([1, 2, 2, 3, 3, 3, 4]) -> [2, 3]
def doublons(elements):
    raise NotImplementedError


# Exercice 7
# Retourne True si les deux textes sont des anagrammes (mêmes lettres, mêmes quantités),
# en ignorant la casse et les espaces. anagrammes("Marie", "aimer") -> True
# Indice : compare sorted(...) des lettres.
def anagrammes(a, b):
    raise NotImplementedError
