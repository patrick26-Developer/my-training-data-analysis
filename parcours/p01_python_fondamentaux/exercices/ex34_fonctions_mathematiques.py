"""Exercices 9.3 — Représenter une fonction mathématique.

Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex34_fonctions_mathematiques.py -v
"""

# N'oublie pas : import math et import matplotlib.pyplot as plt


# Exercice 1
# Écris `linspace(debut, fin, n)` : n valeurs (float) régulièrement espacées de debut à fin INCLUS.
# linspace(0, 1, 5) -> [0.0, 0.25, 0.5, 0.75, 1.0] ; n == 1 -> [debut]


# Exercice 2
# Écris `table_de_valeurs(f, debut, fin, n)` : retourne la liste de couples (x, f(x)) pour n valeurs
# régulièrement espacées.


# Exercice 3
# Écris `tracer_fonction(f, debut, fin, titre, n=100)` : trace la courbe de f et retourne la figure.
# Titre = `titre`, étiquettes "x" et "f(x)", grille activée.


# Exercice 4
# Écris `zero_par_dichotomie(f, a, b, precision=1e-9)` : retourne un zéro de f dans [a, b] (f(a) et
# f(b) de signes opposés). Lève ValueError("Zéro non encadré") si f(a) * f(b) > 0.


# Exercice 5
# Écris `integrale(f, a, b, n=1000)` : aire sous la courbe par la méthode des trapèzes.


# Exercice 6
# Écris `derivee(f, x, h=1e-6)` : pente approchée (f(x + h) - f(x - h)) / (2 * h).


# Exercice 7
# Écris `minimum(f, debut, fin, n=1000)` : retourne le couple (x, f(x)) du plus petit f(x) parmi n
# valeurs régulièrement espacées.


# Exercice 8
# Écris `point_mort(prix, cout_variable, cout_fixe)` : plus petite quantité ENTIÈRE q telle que
# prix * q >= cout_fixe + cout_variable * q. Retourne None si prix <= cout_variable.
# point_mort(1500, 700, 20000) -> 25


# Exercice 9
# Écris `tracer_cercle(rayon)` : trace un cercle de 100 points (courbe paramétrique), avec
# ax.set_aspect("equal"), et retourne la figure.


# Exercice 10
# Écris `comparer_fonctions(fonctions, debut, fin, n=100)` : `fonctions` est un dictionnaire
# {nom: fonction}. Trace toutes les courbes sur un seul graphique avec une légende (labels = noms)
# et retourne la figure.
