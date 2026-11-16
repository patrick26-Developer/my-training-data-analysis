"""Exercices 5.4 — Les fonctions sont des valeurs.

Écris les fonctions demandées (noms et paramètres imposés).
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex19_fonctions_comme_valeurs.py -v
"""

# Exercice 1
# Écris `appliquer(fonction, valeurs)` : retourne la liste des fonction(v) pour chaque v.
# appliquer(len, ["a", "bb"]) -> [1, 2]


# Exercice 2
# Écris `trier_par_prix(produits)` : `produits` est une liste de tuples (nom, prix).
# Retourne une NOUVELLE liste triée par prix croissant (utilise sorted + key + lambda).


# Exercice 3
# Écris `meilleur_eleve(eleves)` : `eleves` est une liste de dictionnaires {"nom", "note"}.
# Retourne le NOM de l'élève avec la meilleure note (utilise max + key).


# Exercice 4
# Écris `trier_par_longueur(mots)` : retourne les mots triés du plus court au plus long
# (à longueur égale, ordre alphabétique). Indice : key peut retourner un tuple (len(m), m).


# Exercice 5
# Écris `multiplicateur(facteur)` qui RETOURNE une fonction multipliant son argument par facteur.
# triple = multiplicateur(3) ; triple(5) -> 15


# Exercice 6
# Écris `calculer(a, operation, b)` en utilisant un DICTIONNAIRE de fonctions (lambda) pour
# "+", "-", "*", "/". Pour une opération inconnue ou une division par zéro, retourne None.


# Exercice 7
# Écris `filtrer(valeurs, condition)` : retourne la liste des v pour lesquels condition(v) est vrai.
# filtrer([1, 2, 3, 4], lambda n: n % 2 == 0) -> [2, 4]


# Exercice 8
# Écris `composer(f, g)` qui retourne une fonction h telle que h(x) == f(g(x)).
# composer(str.upper, str.strip)("  mbote ") -> "MBOTE"
