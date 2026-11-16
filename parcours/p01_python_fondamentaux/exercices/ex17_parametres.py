"""Exercices 5.2 — Paramètres.

Écris les fonctions demandées (noms et paramètres imposés).
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex17_parametres.py -v
"""


# Exercice 1
# Écris `prix_ttc(prix_ht, taux=18)` : retourne le prix TTC, avec 18 % de TVA par défaut.


# Exercice 2
# Écris `remise(prix, pourcentage=0)` : retourne le prix après remise.
# remise(1000) -> 1000.0 ; remise(1000, 10) -> 900.0


# Exercice 3
# Écris `additionner(*nombres)` : retourne la somme de tous les nombres reçus (0 si aucun).


# Exercice 4
# Écris `moyenne(*notes)` : retourne la moyenne des notes reçues.
# Si aucune note n'est reçue, retourne 0.0.


# Exercice 5
# Écris `plus_grand(premier, *autres)` : retourne le plus grand de tous les nombres reçus
# (sans utiliser max()). plus_grand(3, 9, 4) -> 9 ; plus_grand(5) -> 5


# Exercice 6
# Écris `fiche(**infos)` : retourne un texte "cle=valeur" séparé par " | ", dans l'ordre reçu.
# fiche(nom="Grâce", age=25) -> "nom=Grâce | age=25"


# Exercice 7
# Écris `formater_prix(montant, *, devise="FCFA", decimales=0)` : paramètres mot-clé seulement.
# formater_prix(1234.5) -> "1,234 FCFA" (ou "1,235 FCFA" si arrondi : utilise le format :,.{decimales}f)
# formater_prix(1234.5, devise="EUR", decimales=2) -> "1,234.50 EUR"
# Indice : f"{montant:,.{decimales}f} {devise}"


# Exercice 8
# Écris `ajouter_produit(produit, panier=None)` : ajoute `produit` à `panier` et retourne le panier.
# Si panier est None, crée une NOUVELLE liste à chaque appel (pas de défaut partagé !).
