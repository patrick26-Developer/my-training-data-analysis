"""Exercices 6.1 — Les exceptions.

Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex20_exceptions.py -v
"""


# Exercice 1
# Retourne l'entier contenu dans le texte, ou None si le texte n'est pas un entier valide.
# convertir_entier("42") -> 42 ; convertir_entier("abc") -> None
def convertir_entier(texte):
    raise NotImplementedError


# Exercice 2
# Retourne a / b, ou None en cas de division par zéro.
def diviser_sans_erreur(a, b):
    raise NotImplementedError


# Exercice 3
# Retourne la valeur associée à `cle` dans `dico`, ou `defaut` si la clé est absente.
# Utilise try / except KeyError (sans utiliser .get).
def valeur_ou_defaut(dico, cle, defaut):
    raise NotImplementedError


# Exercice 4
# Retourne le nouveau solde après retrait. Lève ValueError("Montant invalide") si montant <= 0
# et ValueError("Solde insuffisant") si montant > solde.
def retirer(solde, montant):
    raise NotImplementedError


# Exercice 5
# `saisies` est une liste de textes simulant ce que tape l'utilisateur, dans l'ordre.
# Retourne le premier entier valide trouvé ; si aucun n'est valide, lève ValueError("Aucune saisie valide").
# premier_entier_valide(["abc", "x1", "12", "7"]) -> 12
def premier_entier_valide(saisies):
    raise NotImplementedError


# Exercice 6
# Retourne la somme des nombres de la liste de textes en IGNORANT les textes invalides.
# somme_tolerante(["10", "abc", "2.5", "5"]) -> 17.5
def somme_tolerante(textes):
    raise NotImplementedError


# Exercice 7
# Définis une exception personnalisée `StockInsuffisantError` (qui hérite de Exception) et une fonction
# `vendre(stock, quantite)` qui retourne stock - quantite, ou lève StockInsuffisantError si stock < quantite.
