"""Exercices 2.3 — match / case.

Utilise `match` pour chacun de ces exercices.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex07_match.py -v
"""


# Exercice 1
# Retourne l'action d'un menu :
#   "1" -> "ajouter" ; "2" -> "supprimer" ; "3" -> "afficher" ;
#   "q" ou "Q" -> "quitter" ; autre -> "inconnu"
def action_menu(choix):
    raise NotImplementedError


# Exercice 2
# Retourne "semaine" pour lundi..vendredi, "week-end" pour samedi/dimanche, "inconnu" sinon.
def type_de_jour(jour):
    raise NotImplementedError


# Exercice 3
# Retourne le nombre de jours du mois (année non bissextile) : 1 = janvier ... 12 = décembre.
#   31 jours : 1, 3, 5, 7, 8, 10, 12 ; 30 jours : 4, 6, 9, 11 ; 28 jours : 2
# Pour toute autre valeur, retourne 0.
def jours_du_mois(mois):
    raise NotImplementedError


# Exercice 4
# Retourne l'opérateur mobile selon l'indicatif (les 2 premiers chiffres) :
#   "04" -> "MTN" ; "05" ou "06" -> "Airtel" ; autre -> "Inconnu"
def operateur(indicatif):
    raise NotImplementedError


# Exercice 5
# Calculatrice : operation vaut "+", "-", "*" ou "/".
# Retourne le résultat de a <operation> b.
# Pour "/" avec b == 0, ou pour une opération inconnue, retourne None.
def calculer(a, operation, b):
    raise NotImplementedError


# Exercice 6
# Retourne un statut de commande (utilise une GARDE avec `if` dans un case) :
#   quantite == 0 -> "vide" ; négative -> "invalide" ; 1 à 9 -> "normale" ; 10 et plus -> "grosse"
def statut_commande(quantite):
    raise NotImplementedError
