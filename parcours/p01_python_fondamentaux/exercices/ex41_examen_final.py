"""Examen final P01 — Partie B : problèmes de code.

Écris tes réponses dans CE fichier (une fonction par problème). Chaque fonction doit avoir une docstring.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex41_examen_final.py -v
"""


# Problème 1 (10 pts)
# mention(note) : "Très bien" (>= 16), "Bien" (>= 14), "Assez bien" (>= 12), "Passable" (>= 10),
# sinon "Ajourné". Lève ValueError si la note n'est pas comprise entre 0 et 20.
def mention(note):
    raise NotImplementedError


# Problème 2 (10 pts)
# mots_frequents(texte, n) : liste des n mots les plus fréquents (minuscules, ponctuation .,;:!? retirée),
# sous forme de couples (mot, nombre), triés par fréquence décroissante puis ordre alphabétique.
def mots_frequents(texte, n):
    raise NotImplementedError


# Problème 3 (10 pts)
# rendre_monnaie(montant, pieces) : dictionnaire {piece: nombre} de l'algorithme glouton
# (pièces de valeur décroissante). Lève ValueError si montant < 0.
def rendre_monnaie(montant, pieces):
    raise NotImplementedError


# Problème 4 (15 pts)
# charger_notes(chemin) : lit un CSV (colonnes nom,note), ignore les lignes invalides (note non
# numérique ou hors de 0 à 20), retourne {nom: moyenne} (plusieurs lignes par nom possibles).
# Fichier absent : retourne {}.
def charger_notes(chemin):
    raise NotImplementedError


# Problème 5 (15 pts)
# est_equilibre(texte) : True si les parenthèses (), crochets [] et accolades {} sont correctement
# équilibrés et imbriqués. "([]{})" -> True ; "([)]" -> False ; "" -> True. Pense à une pile.
def est_equilibre(texte):
    raise NotImplementedError


# Problème 6 (10 pts) : qualité — évaluée avec ruff, les docstrings et tes propres tests pytest.
