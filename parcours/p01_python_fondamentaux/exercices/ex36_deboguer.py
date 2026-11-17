"""Exercices 10.1 — Déboguer.

Chaque fonction ci-dessous contient UN bug (parfois deux). Trouve-le(s) et corrige-le(s) !
La docstring décrit le comportement CORRECT attendu. Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex36_deboguer.py -v
"""


# Bug 1
def somme_jusqua(n):
    """Retourne la somme des entiers de 1 à n INCLUS."""
    total = 0
    for i in range(1, n):
        total += i
    return total


# Bug 2
def moyenne(notes):
    """Retourne la moyenne de la liste ; 0.0 si elle est vide."""
    total = 0
    for note in notes:
        total += note
    return total / len(notes)


# Bug 3
def est_pair(n):
    """Retourne True si n est pair."""
    if n % 2 == 1:
        return True
    return False


# Bug 4
def trier_decroissant(nombres):
    """Retourne une NOUVELLE liste triée du plus grand au plus petit (sans modifier l'original)."""
    resultat = nombres
    resultat.sort(reverse=True)
    return resultat


# Bug 5
def ajouter_produit(produit, panier=[]):
    """Ajoute le produit au panier et retourne le panier. Sans panier fourni : nouvelle liste."""
    panier.append(produit)
    return panier


# Bug 6
def compter_voyelles(texte):
    """Retourne le nombre de voyelles (a, e, i, o, u, y), majuscules comprises."""
    compteur = 0
    for lettre in texte:
        if lettre in "aeiouy":
            compteur += 1
    return compteur


# Bug 7
def remise(prix, pourcentage):
    """Retourne le prix après remise exprimée en pourcentage."""
    return prix - pourcentage / 100


# Bug 8
def premier_mot(phrase):
    """Retourne le premier mot de la phrase (séparé par des espaces) ; '' si la phrase est vide."""
    mots = phrase.split(" ")
    return mots[1]


# Bug 9
def maximum(nombres):
    """Retourne le plus grand nombre de la liste (non vide), même si tous sont négatifs."""
    plus_grand = 0
    for n in nombres:
        if n > plus_grand:
            plus_grand = n
    return plus_grand


# Bug 10
def est_premier(n):
    """Retourne True si n est un nombre premier."""
    if n < 2:
        return False
    for diviseur in range(2, n):
        if n % diviseur == 0:
            return False
        else:
            return True


# Bug 11
def fusionner(a, b):
    """Retourne un NOUVEAU dictionnaire avec les entrées de a, complétées/écrasées par celles de b."""
    resultat = a
    for cle, valeur in b.items():
        resultat[cle] = valeur
    return resultat


# Bug 12
def nombre_de_jours_du_mois(mois, annee):
    """Retourne le nombre de jours du mois (1 à 12) en tenant compte des années bissextiles."""
    if mois == 2:
        if annee % 4 == 0:
            return 29
        return 28
    if mois in (4, 6, 9, 11):
        return 30
    return 31
