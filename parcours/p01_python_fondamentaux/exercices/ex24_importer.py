"""Exercices 7.1 — Importer des modules.

Ajoute les imports nécessaires en haut du fichier, puis écris les fonctions demandées.
Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex24_importer.py -v
"""


# Exercice 1
# Écris `racine(n)` : retourne la racine carrée de n (module math).


# Exercice 2
# Écris `aire_cercle(rayon)` : retourne pi * rayon² arrondi à 2 décimales (math.pi).


# Exercice 3
# Écris `arrondi_superieur(x)` et `arrondi_inferieur(x)` : plafond et plancher d'un nombre
# (math.ceil et math.floor). arrondi_superieur(2.1) -> 3 ; arrondi_inferieur(2.9) -> 2


# Exercice 4
# Écris `nombres_aleatoires(n, minimum, maximum, graine=None)` : retourne une liste de n entiers
# aléatoires entre minimum et maximum inclus (module random). Si `graine` est donnée, appelle
# random.seed(graine) d'abord pour rendre le résultat reproductible.


# Exercice 5
# Écris `mot_le_plus_frequent(mots)` : retourne le mot qui apparaît le plus souvent
# (collections.Counter.most_common). Liste vide : None.


# Exercice 6
# Écris `existe_module(nom)` : retourne True si le module `nom` peut être importé, False sinon.
# Indice : importlib.util.find_spec(nom) is not None. (gère aussi un nom vide)


# Exercice 7
# Écris `nom_du_module_de(fonction)` : retourne le nom du module où est définie une fonction.
# nom_du_module_de(math.sqrt) -> "math" (attribut __module__ ; si absent, retourne None)
