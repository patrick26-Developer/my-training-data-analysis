"""Exercices 2.1 — Booléens et comparaisons.

Chaque fonction doit RETOURNER un booléen (True ou False), sans utiliser `if`.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex05_booleens_et_comparaisons.py -v
"""


# Exercice 1
# Retourne True si la personne a 18 ans ou plus.
def est_majeur(age):
    raise NotImplementedError


# Exercice 2
# Retourne True si la note est comprise entre 10 et 20 (inclus) : l'étudiant est admis.
def est_admis(note):
    raise NotImplementedError


# Exercice 3
# Retourne True si le jour est "samedi" ou "dimanche" (en minuscules).
def est_weekend(jour):
    raise NotImplementedError


# Exercice 4
# Retourne True si le stock est épuisé (0) OU si le produit est périmé.
def doit_retirer(stock, perime):
    raise NotImplementedError


# Exercice 5
# Retourne True si on peut emprunter un livre :
# abonnement actif ET moins de 3 livres déjà empruntés.
def peut_emprunter(abonnement_actif, livres_empruntes):
    raise NotImplementedError


# Exercice 6
# Retourne True si le texte est vide ou ne contient que des espaces.
# est_vide("") -> True ; est_vide("   ") -> True ; est_vide(" a ") -> False
def est_vide(texte):
    raise NotImplementedError


# Exercice 7
# Retourne True si la lettre est une voyelle (a, e, i, o, u, y), majuscule ou minuscule.
# Indice : "in" et lower().
def est_voyelle(lettre):
    raise NotImplementedError
