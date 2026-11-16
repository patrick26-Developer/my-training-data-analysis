"""Exercices 1.2 — Variables et nombres.

Remplace chaque `raise NotImplementedError` par ton code.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex02_variables_et_nombres.py -v
"""


# Exercice 1
# Retourne le total à payer : prix_unitaire multiplié par quantite.
# total_facture(2500, 3) -> 7500
def total_facture(prix_unitaire, quantite):
    raise NotImplementedError


# Exercice 2
# Retourne le prix après une remise exprimée en pourcentage.
# appliquer_remise(20000, 15) -> 17000.0
def appliquer_remise(prix, pourcentage):
    raise NotImplementedError


# Exercice 3
# Convertit des FCFA en euros. La parité fixe est : 1 euro = 655.957 FCFA.
# Retourne le résultat arrondi à 2 décimales.
# fcfa_en_euro(65595.7) -> 100.0
def fcfa_en_euro(montant_fcfa):
    raise NotImplementedError


# Exercice 4
# Partage un montant équitablement entre des personnes.
# Retourne un couple (part_de_chacun, reste) avec des entiers.
# partager(10000, 3) -> (3333, 1)
# Indice : // et %, ou la fonction divmod().
def partager(montant, personnes):
    raise NotImplementedError


# Exercice 5
# Retourne le NOM du type de la valeur, sous forme de texte.
# nom_du_type(3) -> "int" ; nom_du_type(3.5) -> "float" ; nom_du_type("a") -> "str"
# Indice : type(valeur).__name__
def nom_du_type(valeur):
    raise NotImplementedError


# Exercice 6
# Un commerçant a `stock` articles. Il en vend `vendus`, puis reçoit `livres` nouveaux.
# Retourne le stock final, en utilisant les opérateurs -= et +=.
# stock_final(100, 35, 20) -> 85
def stock_final(stock, vendus, livres):
    raise NotImplementedError
