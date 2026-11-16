"""Exercices 2.2 — if, elif, else.

Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex06_if_elif_else.py -v
"""


# Exercice 1
# Retourne "pair" si le nombre est pair, sinon "impair".
# Indice : un nombre est pair si nombre % 2 == 0.
def parite(nombre):
    raise NotImplementedError


# Exercice 2
# Retourne la mention selon la note sur 20 :
#   >= 16 "Très bien" ; >= 14 "Bien" ; >= 12 "Assez bien" ; >= 10 "Passable" ; sinon "Ajourné"
def mention(note):
    raise NotImplementedError


# Exercice 3
# Retourne le pourcentage de remise selon la quantité achetée :
#   50 et plus -> 10 ; de 10 à 49 -> 5 ; moins de 10 -> 0
def taux_remise(quantite):
    raise NotImplementedError


# Exercice 4
# Retourne le prix du ticket de bus :
#   moins de 12 ans : 100 FCFA ; de 12 à 64 ans : 200 FCFA ; 65 ans et plus : 0 (gratuit)
def prix_ticket(age):
    raise NotImplementedError


# Exercice 5
# Retourne le plus grand des trois nombres, SANS utiliser max().
def plus_grand(a, b, c):
    raise NotImplementedError


# Exercice 6
# Année bissextile : divisible par 4, sauf les années divisibles par 100,
# sauf celles divisibles par 400.  (2000 -> True ; 1900 -> False ; 2024 -> True ; 2023 -> False)
def est_bissextile(annee):
    raise NotImplementedError


# Exercice 7
# Retourne le type d'un triangle selon la longueur de ses trois côtés :
#   "equilateral" (3 côtés égaux), "isocele" (exactement 2 égaux), "scalene" (tous différents)
def type_triangle(a, b, c):
    raise NotImplementedError
