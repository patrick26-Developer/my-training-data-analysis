"""Exercices 9.4 — Tableau de bord d'une boutique.

Une vente est un dictionnaire {"mois": "2026-01", "produit": "Riz", "quantite": 60, "prix": 800.0}.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex35_graphique_des_ventes.py -v
"""

# N'oublie pas : import csv, import matplotlib.pyplot as plt


# Exercice 1
# Écris `lire_ventes(chemin)` : lit un CSV (colonnes mois, produit, quantite, prix_unitaire) et
# retourne la liste de ventes (quantite en int, prix en float).


# Exercice 2
# Écris `chiffre_affaires_par_mois(ventes)` : dictionnaire {mois: total}, trié par mois croissant.


# Exercice 3
# Écris `chiffre_affaires_par_produit(ventes)` : dictionnaire {produit: total}.


# Exercice 4
# Écris `meilleur_produit(ventes)` : nom du produit au plus grand chiffre d'affaires.


# Exercice 5
# Écris `evolution(par_mois)` : liste des variations en % (arrondies à 1 décimale) d'un mois sur
# l'autre. Un mois à 0 est ignoré comme point de départ (pas de division par zéro).
# evolution({"01": 100, "02": 150, "03": 120}) -> [50.0, -20.0]


# Exercice 6
# Écris `droite_de_tendance(valeurs)` : droite des moindres carrés y = a*x + b pour x = 0, 1, 2, ...
# Retourne (a, b) arrondis à 4 décimales.
#   a = (n*Σxy - Σx*Σy) / (n*Σx² - (Σx)²)     b = (Σy - a*Σx) / n
# droite_de_tendance([1, 3, 5, 7]) -> (2.0, 1.0)


# Exercice 7
# Écris `prevision(valeurs, mois_suivants=1)` : prolonge la droite de tendance et retourne la valeur
# prévue pour le mois numéro len(valeurs) + mois_suivants - 1, arrondie à 2 décimales.
# prevision([1, 3, 5, 7]) -> 9.0


# Exercice 8
# Écris `tableau_de_bord(ventes)` : figure à 2 graphiques côte à côte (plt.subplots(1, 2)) :
# à gauche la courbe du chiffre d'affaires par mois (titre "Chiffre d'affaires par mois"),
# à droite les barres par produit (titre "Chiffre d'affaires par produit").
# Ajoute le titre général "Boutique Mama Nzoni" (fig.suptitle). Retourne la figure.
