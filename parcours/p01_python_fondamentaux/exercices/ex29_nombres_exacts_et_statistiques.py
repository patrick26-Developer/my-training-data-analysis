"""Exercices 8.2 — Calculs exacts, hasard et statistiques.

Écris les fonctions demandées (noms et paramètres imposés ; ajoute les imports nécessaires).
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex29_nombres_exacts_et_statistiques.py -v
"""


# Exercice 1
# Écris `total_exact(prix)` : `prix` est une liste de TEXTES ("0.10", "0.20"). Retourne la somme
# exacte sous forme de Decimal. total_exact(["0.10", "0.20"]) == Decimal("0.30")


# Exercice 2
# Écris `ttc(prix_ht, taux)` : prix_ht et taux sont des textes ("1999.99", "0.18"). Retourne le
# prix TTC en Decimal arrondi au centime (2 décimales, arrondi ROUND_HALF_UP).


# Exercice 3
# Écris `somme_fractions(fractions)` : `fractions` est une liste de couples (numerateur, denominateur).
# Retourne la somme sous forme de Fraction. somme_fractions([(1, 3), (1, 6)]) == Fraction(1, 2)


# Exercice 4
# Écris `lancer_des(n, graine)` : retourne la liste de n lancers d'un dé (1 à 6), reproductible
# grâce à random.seed(graine).


# Exercice 5
# Écris `resume(notes)` : retourne un dictionnaire {"moyenne", "mediane", "mode", "ecart_type"}
# avec la moyenne et l'écart-type de la POPULATION (pstdev) arrondis à 2 décimales.


# Exercice 6
# Écris `valeurs_aberrantes(valeurs, k=2)` : retourne la liste des valeurs situées à plus de
# k écarts-types (pstdev) de la moyenne, dans l'ordre d'origine.


# Exercice 7
# Écris `probabilite_estimee(evenement, essais, graine)` : `evenement` est une fonction sans
# paramètre qui retourne True/False (utilise le hasard). Retourne la fréquence de True sur `essais`
# répétitions, après random.seed(graine).


# Exercice 8
# Écris `tirage_loto(graine)` : retourne la liste TRIÉE de 6 numéros distincts entre 1 et 49,
# reproductible avec random.seed(graine).
