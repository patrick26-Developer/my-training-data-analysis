"""Exercices 9.1 — La géométrie derrière turtle.

On ne teste pas de fenêtre : on calcule les points, comme le ferait un logiciel de dessin.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex32_turtle.py -v
"""

# N'oublie pas : import math


# Exercice 1
# Écris `angle_de_rotation(n)` : angle (en degrés) dont la tortue tourne pour un polygone régulier
# à n côtés. angle_de_rotation(4) -> 90.0


# Exercice 2
# Écris `angle_interieur(n)` : angle intérieur (en degrés) d'un polygone régulier à n côtés.
# angle_interieur(3) -> 60.0 ; angle_interieur(6) -> 120.0   (180 - angle de rotation)


# Exercice 3
# Écris `sommets_polygone(n, rayon)` : liste des n sommets (x, y) d'un polygone régulier inscrit dans
# un cercle de rayon `rayon` centré en (0, 0), le premier sommet étant en (rayon, 0).
# Les coordonnées sont ARRONDIES à 6 décimales.


# Exercice 4
# Écris `perimetre_polygone(points)` : périmètre du polygone fermé défini par la liste de points
# (distance entre chaque point et le suivant, et entre le dernier et le premier), arrondi à 6 décimales.


# Exercice 5
# Écris `longueur_cote(n, rayon)` : longueur du côté d'un polygone régulier à n côtés inscrit dans un
# cercle de rayon `rayon` : 2 * rayon * sin(pi / n). Arrondi à 6 décimales.


# Exercice 6
# Écris `chemin_carre(cote)` : retourne la liste des ordres que la tortue exécuterait pour tracer un
# carré, sous forme de tuples : [("forward", cote), ("left", 90), ...] (4 fois).


# Exercice 7
# Écris `position_finale(ordres)` : simule une tortue partant de (0, 0) orientée vers l'Est (angle 0)
# et retourne sa position finale (x, y) arrondie à 6 décimales après avoir exécuté la liste d'ordres
# ("forward", d) et ("left", angle_en_degres) / ("right", angle_en_degres).
# Pour un carré complet, la tortue revient en (0.0, 0.0).


# Exercice 8
# Écris `aire_polygone(points)` : aire d'un polygone par la formule du lacet (Shoelace) :
# 1/2 * |somme(x_i * y_(i+1) - x_(i+1) * y_i)|, arrondie à 6 décimales.
# aire_polygone([(0, 0), (4, 0), (4, 3), (0, 3)]) -> 12.0
