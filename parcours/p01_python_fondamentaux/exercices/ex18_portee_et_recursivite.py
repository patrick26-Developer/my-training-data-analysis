"""Exercices 5.3 — Portée et récursivité.

Écris les fonctions demandées (noms et paramètres imposés). N'utilise pas `global`.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex18_portee_et_recursivite.py -v
"""

# Exercice 1
# Constante globale : définis TVA = 18 au niveau du module (en dehors de toute fonction).


# Exercice 2
# Écris `prix_ttc(prix_ht)` qui LIT la constante globale TVA et retourne le prix TTC.


# Exercice 3
# Écris `incrementer(compteur, pas=1)` qui RETOURNE compteur + pas, sans modifier de variable globale.


# Exercice 4
# Écris `ajouter_sans_modifier(liste, element)` qui retourne une NOUVELLE liste contenant
# les éléments de `liste` suivis de `element`, SANS modifier la liste reçue.


# Exercice 5
# Écris `factorielle(n)` de façon RÉCURSIVE (factorielle(0) == 1).


# Exercice 6
# Écris `somme_recursive(n)` : somme de 1 à n, de façon récursive (somme_recursive(0) == 0).


# Exercice 7
# Écris `puissance(base, exposant)` de façon récursive, pour un exposant entier >= 0.
# puissance(2, 10) -> 1024 ; puissance(5, 0) -> 1


# Exercice 8
# Écris `inverser(texte)` de façon récursive (sans tranche [::-1]).
# inverser("Mbote") -> "etobM"


# Exercice 9
# Écris `fibonacci(n)` : version AVEC BOUCLE, rapide. fibonacci(0)=0, fibonacci(1)=1, fibonacci(10)=55.
# Elle doit gérer fibonacci(90) sans lenteur.


# Exercice 10
# Écris `pgcd(a, b)` : plus grand commun diviseur par l'algorithme d'Euclide, de façon récursive.
#   pgcd(a, 0) = a ; sinon pgcd(a, b) = pgcd(b, a % b).   pgcd(48, 18) -> 6
