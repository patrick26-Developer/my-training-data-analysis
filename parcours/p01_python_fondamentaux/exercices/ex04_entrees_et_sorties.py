"""Exercices 1.4 — Entrées et sorties.

Dans ces exercices, les tests simulent la saisie de l'utilisateur : tu n'as rien à taper.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex04_entrees_et_sorties.py -v
"""


# Exercice 1
# Demande le prénom avec input("Prénom : ") et RETOURNE-le nettoyé
# (sans espaces aux bords, première lettre de chaque mot en majuscule).
def demander_prenom():
    raise NotImplementedError


# Exercice 2
# Demande deux nombres avec input() (un par appel) et RETOURNE leur somme.
# Les nombres peuvent avoir une virgule décimale : "2.5" ou "2,5".
def additionner_saisies():
    raise NotImplementedError


# Exercice 3
# Demande avec input() le prix unitaire (décimal) puis la quantité (entier),
# et RETOURNE le total sous forme de décimal.
def total_saisi():
    raise NotImplementedError


# Exercice 4
# Demande un nom avec input() et AFFICHE (print) : Mbote, <Nom> !
# Le nom est nettoyé comme à l'exercice 1.
def saluer_utilisateur():
    raise NotImplementedError


# Exercice 5
# Retourne un reçu sur 3 lignes (texte unique séparé par "\n") :
#   Client   : <client>
#   Quantité : <quantite>
#   Total    : <total> FCFA          (total avec séparateur de milliers, sans décimale)
# recu("Grâce", 3, 7500) ->
#   "Client   : Grâce\nQuantité : 3\nTotal    : 7,500 FCFA"
def recu(client, quantite, total):
    raise NotImplementedError
