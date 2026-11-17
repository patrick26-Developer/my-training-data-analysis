"""Exercices 10.4 — Documenter son code.

Chaque fonction doit :
  1. être correctement implémentée ;
  2. avoir une DOCSTRING (résumé d'au moins 10 caractères) ;
  3. contenir au moins UN exemple doctest (lignes `>>> ...` suivies du résultat) qui PASSE.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex39_documenter.py -v
"""


# Exercice 1 — carre(x) : retourne x * x.
def carre(x):
    raise NotImplementedError


# Exercice 2 — est_pair(n) : True si n est pair.
def est_pair(n):
    raise NotImplementedError


# Exercice 3 — initiales(nom_complet) : "Grâce Marie Nzoni" -> "G.M.N."
def initiales(nom_complet):
    raise NotImplementedError


# Exercice 4 — prix_ttc(prix_ht, taux=18) : prix TTC arrondi à 2 décimales.
# Documente aussi les paramètres (mot "taux" présent dans la docstring).
def prix_ttc(prix_ht, taux=18):
    raise NotImplementedError


# Exercice 5 — fusionner_mots(mots) : colle les mots avec un tiret ; ["a", "b"] -> "a-b".
def fusionner_mots(mots):
    raise NotImplementedError


# Exercice 6 — Écris la docstring de MODULE de ce fichier (tout en haut) : elle existe déjà,
# complète-la pour qu'elle contienne le mot "Mayele".
