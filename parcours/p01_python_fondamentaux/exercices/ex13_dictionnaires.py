"""Exercices 4.3 — Les dictionnaires.

Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex13_dictionnaires.py -v
"""


# Exercice 1
# Retourne le prix du produit, ou 0 s'il n'existe pas dans le catalogue (dictionnaire nom -> prix).
def prix_du_produit(catalogue, produit):
    raise NotImplementedError


# Exercice 2
# Retourne un dictionnaire qui compte les occurrences de chaque lettre du texte.
# compter_lettres("banane") -> {"b": 1, "a": 2, "n": 2, "e": 1}
def compter_lettres(texte):
    raise NotImplementedError


# Exercice 3
# Retourne la valeur totale du stock : somme de prix * quantité.
# `stock` est de la forme {"Riz": (800, 3), "Sel": (100, 10)} (prix, quantité).
# valeur_du_stock(...) -> 3400
def valeur_du_stock(stock):
    raise NotImplementedError


# Exercice 4
# Retourne le nom du produit le plus cher (catalogue nom -> prix). Pour un catalogue vide : None.
def plus_cher(catalogue):
    raise NotImplementedError


# Exercice 5
# `ventes` est une liste de tuples (jour, montant). Retourne le total par jour.
# total_par_jour([("lundi", 500), ("mardi", 300), ("lundi", 200)]) -> {"lundi": 700, "mardi": 300}
def total_par_jour(ventes):
    raise NotImplementedError


# Exercice 6
# Retourne un NOUVEAU dictionnaire dont les clés et valeurs sont inversées.
# inverser({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
def inverser(dico):
    raise NotImplementedError


# Exercice 7
# `eleves` est une liste de dictionnaires {"nom": ..., "note": ...}.
# Retourne la liste des noms des élèves dont la note est >= 10, dans le même ordre.
def admis(eleves):
    raise NotImplementedError


# Exercice 8
# Fusionne deux stocks (nom -> quantité) en additionnant les quantités des produits communs.
# fusionner({"Riz": 2, "Sel": 1}, {"Riz": 3, "Sucre": 4}) -> {"Riz": 5, "Sel": 1, "Sucre": 4}
def fusionner_stocks(a, b):
    raise NotImplementedError
