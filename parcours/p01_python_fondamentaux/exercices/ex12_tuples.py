"""Exercices 4.2 — Les tuples.

Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex12_tuples.py -v
"""


# Exercice 1
# Retourne le couple (a, b) échangé : echanger((1, 2)) -> (2, 1)
# Utilise le déballage.
def echanger(couple):
    raise NotImplementedError


# Exercice 2
# Retourne (quotient, reste) de la division entière de a par b, sous forme de tuple.
# diviser(17, 5) -> (3, 2)
def diviser(a, b):
    raise NotImplementedError


# Exercice 3
# `date` est un tuple (jour, mois, annee). Retourne le texte "JJ/MM/AAAA" avec zéros devant.
# formater_date((5, 3, 2026)) -> "05/03/2026"
def formater_date(date):
    raise NotImplementedError


# Exercice 4
# Retourne la distance entre deux points (x, y) : racine de (dx² + dy²), arrondie à 2 décimales.
# distance((0, 0), (3, 4)) -> 5.0
# Indice : ** 0.5 pour la racine carrée.
def distance(p1, p2):
    raise NotImplementedError


# Exercice 5
# `produits` et `prix` sont deux listes de même taille. Retourne la liste de tuples (produit, prix).
# associer(["Riz", "Sel"], [800, 100]) -> [("Riz", 800), ("Sel", 100)]
def associer(produits, prix):
    raise NotImplementedError


# Exercice 6
# `ventes` est une liste de tuples (produit, quantite, prix_unitaire).
# Retourne le chiffre d'affaires total. chiffre_affaires([("Riz", 2, 800), ("Sel", 5, 100)]) -> 2100
def chiffre_affaires(ventes):
    raise NotImplementedError


# Exercice 7
# Retourne (premier, dernier, nombre_d_elements_du_milieu) d'une liste d'au moins 2 éléments.
# Utilise le déballage avec *. resume([1, 2, 3, 4, 5]) -> (1, 5, 3)
def resume(elements):
    raise NotImplementedError
