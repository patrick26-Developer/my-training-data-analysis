"""Exercices 4.5 — Les compréhensions.

Réponds à chaque exercice en UNE expression (compréhension) lorsque c'est possible.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex15_comprehensions.py -v
"""


# Exercice 1
# Retourne la liste des carrés des entiers de 1 à n. carres(4) -> [1, 4, 9, 16]
def carres(n):
    raise NotImplementedError


# Exercice 2
# Retourne la liste des prix TTC arrondis (TVA 18 %) pour les prix strictement supérieurs à `seuil`.
# prix_ttc([300, 750, 1200], 500) -> [885, 1416]
def prix_ttc(prix, seuil):
    raise NotImplementedError


# Exercice 3
# Retourne la liste des longueurs des mots. longueurs(["riz", "sucre"]) -> [3, 5]
def longueurs(mots):
    raise NotImplementedError


# Exercice 4
# Retourne la liste des mots qui commencent par la lettre donnée (casse ignorée).
# commencant_par(["Riz", "rat", "Sel"], "r") -> ["Riz", "rat"]
def commencant_par(mots, lettre):
    raise NotImplementedError


# Exercice 5
# Retourne un dictionnaire {mot: longueur}. dico_longueurs(["riz", "sucre"]) -> {"riz": 3, "sucre": 5}
def dico_longueurs(mots):
    raise NotImplementedError


# Exercice 6
# Remplace chaque nombre négatif par 0 en gardant la même longueur.
# sans_negatifs([3, -1, 4, -5]) -> [3, 0, 4, 0]
def sans_negatifs(nombres):
    raise NotImplementedError


# Exercice 7
# Aplatit une liste de listes en une seule liste. aplatir([[1, 2], [3], []]) -> [1, 2, 3]
def aplatir(listes):
    raise NotImplementedError


# Exercice 8
# Retourne True si tous les éléments sont des nombres strictement positifs (utilise all()).
def tous_positifs(nombres):
    raise NotImplementedError


# Exercice 9
# Retourne la grille n x m remplie de zéros (lignes indépendantes).
# grille(2, 3) -> [[0, 0, 0], [0, 0, 0]]
def grille(n, m):
    raise NotImplementedError
