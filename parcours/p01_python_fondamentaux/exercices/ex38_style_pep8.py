"""Exercices 10.3 — Style et conventions de nommage.

Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex38_style_pep8.py -v
"""


# Exercice 1
# Écris `vers_snake_case(texte)` : convertit un nom CamelCase / PascalCase en snake_case.
#   "CompteBancaire" -> "compte_bancaire" ; "prixTotal" -> "prix_total" ; "HTTPServer" -> "http_server"
# Indice : le module `re` ou une boucle qui insère "_" avant une majuscule.


# Exercice 2
# Écris `vers_pascal_case(texte)` : convertit snake_case en PascalCase.
#   "compte_bancaire" -> "CompteBancaire" ; "prix" -> "Prix"


# Exercice 3
# Écris `est_snake_case(nom)` : True si le nom ne contient que des minuscules, chiffres et "_",
# ne commence pas par un chiffre. est_snake_case("prix_total") -> True ; ("PrixTotal") -> False


# Exercice 4
# Écris `est_constante(nom)` : True si le nom est en MAJUSCULES_AVEC_UNDERSCORES (lettres majuscules,
# chiffres, "_", commençant par une lettre). est_constante("TAUX_TVA") -> True ; ("taux") -> False


# Exercice 5
# Écris `lignes_trop_longues(code, maximum=100)` : retourne la liste des numéros de ligne (à partir
# de 1) dont la longueur dépasse `maximum` caractères.


# Exercice 6
# Écris `indentation_correcte(code)` : True si toutes les lignes non vides sont indentées avec un
# MULTIPLE de 4 espaces et sans tabulation.


# Exercice 7
# Écris `noms_masquant_le_langage(code)` : retourne la liste TRIÉE (sans doublon) des noms
# de variables du code (texte) qui masquent une fonction intégrée parmi
# {"list", "dict", "set", "str", "int", "sum", "max", "min", "len", "type", "id"}
# lorsqu'ils sont affectés avec `nom = ...` (utilise le module `ast`).
# noms_masquant_le_langage("list = [1]\nsum = 0\nx = 2") -> ["list", "sum"]


# Exercice 8
# Réécris la fonction ci-dessous en code PROPRE (bons noms, espaces, constante, plus simple).
# Elle doit se comporter EXACTEMENT pareil. Nomme-la `prix_apres_remise(prix_unitaire, quantite, remise_pourcent)`.
#
#   def f(a,b,c):
#     x=a*b
#     if c>0 :
#      x=x-x*c/100
#     return x
