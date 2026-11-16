"""Exercices 1.3 — Le texte.

Remplace chaque `raise NotImplementedError` par ton code.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex03_le_texte.py -v
"""


# Exercice 1
# Nettoie un nom saisi n'importe comment : sans espaces aux bords, avec une majuscule à chaque mot.
# nettoyer_nom("  mAmA nzoni ") -> "Mama Nzoni"
def nettoyer_nom(nom):
    raise NotImplementedError


# Exercice 2
# Retourne la phrase "<nom> a <age> ans" en utilisant une f-string.
# presenter("Grâce", 25) -> "Grâce a 25 ans"
def presenter(nom, age):
    raise NotImplementedError


# Exercice 3
# Retourne un prix formaté avec séparateur de milliers (virgule), 2 décimales et " FCFA".
# formater_prix(1234567.5) -> "1,234,567.50 FCFA"
def formater_prix(montant):
    raise NotImplementedError


# Exercice 4
# Retourne les 3 premières lettres du texte en MAJUSCULES (code de ville).
# code_ville("Brazzaville") -> "BRA"
def code_ville(ville):
    raise NotImplementedError


# Exercice 5
# Retourne le texte à l'envers.
# inverser("Mbote") -> "etobM"
def inverser(texte):
    raise NotImplementedError


# Exercice 6
# Une ligne de stock a la forme "produit;prix;quantite", par exemple "Manioc;500;12".
# Retourne la valeur du stock de cette ligne (prix * quantite) sous forme d'entier.
# valeur_du_stock("Manioc;500;12") -> 6000
# Indice : split(";") puis int().
def valeur_du_stock(ligne):
    raise NotImplementedError


# Exercice 7
# Retourne True si le texte est un numéro de téléphone local valide :
# exactement 9 caractères, tous des chiffres.
# telephone_valide("060123456") -> True ; telephone_valide("06012345a") -> False
def telephone_valide(texte):
    raise NotImplementedError
