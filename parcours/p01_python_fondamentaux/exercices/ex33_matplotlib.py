"""Exercices 9.2 — matplotlib.

Chaque fonction CRÉE un graphique et RETOURNE la figure (`fig`). N'appelle pas plt.show().
Utilise : fig, ax = plt.subplots()
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex33_matplotlib.py -v
"""

# N'oublie pas : import matplotlib.pyplot as plt


# Exercice 1
# Écris `courbe_ventes(mois, ventes)` : une courbe (ax.plot) avec les marqueurs "o",
# le titre "Ventes", l'étiquette x "Mois" et l'étiquette y "Ventes (FCFA)".


# Exercice 2
# Écris `barres_stock(produits, quantites)` : diagramme en barres (ax.bar), titre "Stock par produit",
# étiquette y "Quantité".


# Exercice 3
# Écris `histogramme_notes(notes, classes=5)` : histogramme (ax.hist) avec `classes` intervalles,
# titre "Répartition des notes", étiquette x "Note".


# Exercice 4
# Écris `nuage_points(x, y)` : nuage de points (ax.scatter), étiquettes "Heures" (x) et "Note" (y).


# Exercice 5
# Écris `camembert(parts)` : `parts` est un dictionnaire {nom: valeur}. Dessine un camembert (ax.pie)
# avec les étiquettes = noms et le titre "Répartition".


# Exercice 6
# Écris `deux_courbes(x, y1, y2)` : UN seul graphique avec deux courbes, légendes "A" et "B"
# (label=... puis ax.legend()), titre "Comparaison".


# Exercice 7
# Écris `figure_double(mois, ventes)` : une figure de 1 ligne et 2 colonnes (plt.subplots(1, 2)) :
# à gauche la courbe des ventes, à droite les barres. Retourne la figure.


# Exercice 8
# Écris `enregistrer(fig, chemin)` : enregistre la figure dans le fichier (savefig, dpi=100) et
# retourne True si le fichier existe ensuite.
