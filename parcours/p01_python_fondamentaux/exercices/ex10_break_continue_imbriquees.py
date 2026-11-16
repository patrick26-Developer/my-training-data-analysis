"""Exercices 3.3 — break, continue et boucles imbriquées.

Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex10_break_continue_imbriquees.py -v
"""


# Exercice 1
# Retourne le plus petit entier n >= 1 tel que n * n > limite (utilise break).
# premier_carre_superieur(50) -> 8
def premier_carre_superieur(limite):
    raise NotImplementedError


# Exercice 2
# Retourne la somme des nombres de 1 à n qui NE sont PAS multiples de 3 (utilise continue).
# somme_sans_multiples_de_3(10) -> 37  (55 - 3 - 6 - 9)
def somme_sans_multiples_de_3(n):
    raise NotImplementedError


# Exercice 3
# Retourne le texte jusqu'à (non inclus) le premier espace. Si pas d'espace, retourne tout le texte.
# premier_mot("Mbote na yo") -> "Mbote" (utilise for + break, pas split)
def premier_mot(texte):
    raise NotImplementedError


# Exercice 4
# Retourne la table de multiplication carrée de taille n, une ligne par rangée, nombres séparés
# par des espaces, rangées séparées par "\n".
# table_carree(3) -> "1 2 3\n2 4 6\n3 6 9"
def table_carree(n):
    raise NotImplementedError


# Exercice 5
# Retourne la liste (list) des nombres premiers inférieurs ou égaux à n, en utilisant
# une boucle imbriquée avec break (ou for/else). nombres_premiers(20) -> [2, 3, 5, 7, 11, 13, 17, 19]
def nombres_premiers(n):
    raise NotImplementedError


# Exercice 6
# Retourne toutes les paires (a, b) avec 1 <= a < b <= n dont la somme vaut `cible`,
# sous forme de liste de tuples, dans l'ordre croissant de a.
# paires_de_somme(10, 5) -> [(1, 4), (2, 3)]
def paires_de_somme(n, cible):
    raise NotImplementedError
