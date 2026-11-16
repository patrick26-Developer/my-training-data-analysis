"""Exercices 7.2 — La bibliothèque standard.

Écris les fonctions demandées (ajoute les imports nécessaires).
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex25_bibliotheque_standard.py -v
"""


# Exercice 1
# Écris `age(naissance, aujourdhui)` : `naissance` et `aujourdhui` sont des objets date.
# Retourne l'âge en années complètes (tient compte du mois et du jour).
# age(date(2000, 5, 20), date(2026, 5, 19)) -> 25 ; age(date(2000, 5, 20), date(2026, 5, 20)) -> 26


# Exercice 2
# Écris `jours_avant(date_cible, aujourdhui)` : nombre de jours entre aujourd'hui et date_cible
# (négatif si la date est passée).


# Exercice 3
# Écris `formater_date_fr(texte_iso)` : convertit "2026-12-25" (AAAA-MM-JJ) en "25/12/2026".
# Utilise datetime.strptime puis strftime.


# Exercice 4
# Écris `ajouter_jours(texte_iso, n)` : retourne la date (texte ISO "AAAA-MM-JJ") n jours plus tard.
# ajouter_jours("2026-12-30", 5) -> "2027-01-04"


# Exercice 5
# Écris `resume_statistique(notes)` : retourne un dictionnaire
# {"moyenne": ..., "mediane": ..., "min": ..., "max": ...} (moyenne arrondie à 2 décimales).


# Exercice 6
# Écris `regrouper_par_initiale(mots)` : retourne un dictionnaire {initiale: [mots]} (initiale en
# minuscule) en utilisant defaultdict(list). L'ordre des mots est conservé.


# Exercice 7
# Écris `toutes_les_paires(elements)` : retourne la liste de toutes les paires (combinaisons de 2)
# d'éléments distincts, sous forme de tuples, avec itertools.combinations.
# toutes_les_paires(["A", "B", "C"]) -> [("A", "B"), ("A", "C"), ("B", "C")]


# Exercice 8
# Écris `mot_de_passe(longueur)` : retourne un mot de passe aléatoire de `longueur` caractères,
# choisis parmi les lettres (string.ascii_letters) et les chiffres (string.digits),
# en utilisant le module `secrets` (secrets.choice).
