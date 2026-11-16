"""Exercices 3.1 — La boucle while.

Utilise `while` pour chacun de ces exercices (pas de for, pas de sum()).
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex08_while.py -v
"""


# Exercice 1
# Retourne la somme des entiers de 1 à n inclus. somme_jusqua(100) -> 5050 ; somme_jusqua(0) -> 0
def somme_jusqua(n):
    raise NotImplementedError


# Exercice 2
# Retourne n! = 1 * 2 * ... * n (et 1 pour n == 0). factorielle(5) -> 120
def factorielle(n):
    raise NotImplementedError


# Exercice 3
# Retourne combien de fois il faut diviser n par 2 (division entière //) pour arriver à 0.
# Autrement dit, le nombre de chiffres binaires de n. nombre_de_bits(8) -> 4 ; nombre_de_bits(0) -> 0
def nombre_de_bits(n):
    raise NotImplementedError


# Exercice 4
# Un capital placé gagne `taux` pourcent par an (intérêts composés).
# Retourne le nombre d'années pour qu'il atteigne au moins `objectif`.
# annees_pour_doubler(1000, 2000, 10) -> 8  (1000 * 1.1^8 = 2143,58)
def annees_pour_atteindre(capital, objectif, taux):
    raise NotImplementedError


# Exercice 5
# Suite de Collatz : retourne le nombre d'étapes pour atteindre 1.
#   si n est pair : n = n // 2 ; sinon : n = 3 * n + 1. collatz(6) -> 8 ; collatz(1) -> 0
def collatz(n):
    raise NotImplementedError


# Exercice 6
# Retourne la somme des chiffres d'un entier positif. somme_des_chiffres(1234) -> 10
# Indice : n % 10 donne le dernier chiffre, n // 10 enlève le dernier chiffre.
def somme_des_chiffres(n):
    raise NotImplementedError


# Exercice 7
# `saisies` est une liste de textes simulant ce que tape l'utilisateur.
# Additionne les nombres tapés jusqu'à rencontrer "fin" (non inclus) et retourne le total (float).
# total_jusqua_fin(["500", "250.5", "fin", "999"]) -> 750.5
def total_jusqua_fin(saisies):
    raise NotImplementedError
