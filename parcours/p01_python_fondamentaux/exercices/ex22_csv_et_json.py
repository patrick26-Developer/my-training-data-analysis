"""Exercices 6.3 — CSV et JSON.

Les fonctions reçoivent le CHEMIN du fichier (les tests utilisent un dossier temporaire).
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex22_csv_et_json.py -v
"""

# N'oublie pas : import csv, import json


# Exercice 1
# Écris `ecrire_stock_csv(chemin, produits)` : `produits` est une liste de dictionnaires
# {"nom", "prix", "quantite"}. Écris un CSV avec en-tête (colonnes : nom, prix, quantite).


# Exercice 2
# Écris `lire_stock_csv(chemin)` : retourne la liste de dictionnaires, avec "prix" et "quantite"
# convertis en ENTIERS (le nom reste un texte).


# Exercice 3
# Écris `valeur_totale_csv(chemin)` : retourne la somme de prix * quantite d'un CSV de stock
# (réutilise lire_stock_csv).


# Exercice 4
# Écris `sauvegarder_json(chemin, donnees)` : écrit `donnees` en JSON lisible
# (indent=2) en conservant les accents (ensure_ascii=False).


# Exercice 5
# Écris `charger_json(chemin, defaut=None)` : retourne les données du fichier JSON.
# Si le fichier n'existe pas OU n'est pas du JSON valide, retourne `defaut`.


# Exercice 6
# Écris `compter_par_ville(chemin)` : le CSV contient les colonnes "nom,ville". Retourne un
# dictionnaire {ville: nombre_de_personnes}.


# Exercice 7
# Écris `csv_vers_json(chemin_csv, chemin_json)` : convertit un CSV (colonnes quelconques, toutes
# les valeurs restent des textes) en un fichier JSON contenant la liste des lignes (dictionnaires).


# Exercice 8
# Écris `ajouter_produit_json(chemin, produit)` : le fichier JSON contient une LISTE de produits.
# Charge-la (liste vide si le fichier est absent), ajoute `produit` et réécris le fichier.
# Retourne le nombre de produits après ajout.
