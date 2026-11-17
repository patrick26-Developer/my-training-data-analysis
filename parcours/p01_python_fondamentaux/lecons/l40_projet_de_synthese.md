# Projet de synthèse — Gestion de boutique en console

⏱ 8 à 12 heures · 🎯 Évaluation finale du parcours P01 · 📦 Prérequis : modules 1 à 10

## 🎯 Objectif

Construire, **seul(e)**, une application console complète pour une petite boutique, en mobilisant tout le parcours :
variables, conditions, boucles, collections, fonctions, exceptions, fichiers JSON/CSV, modules, tests, style et
documentation.

## 1. Le client

*Mama Nzoni tient une boutique à Brazzaville. Elle veut un programme sur son ordinateur pour : enregistrer ses
produits, vendre, imprimer un reçu, savoir ce qu'il reste en stock, et retrouver ses ventes le lendemain.*

## 2. Cahier des charges

### 2.1 Fonctions obligatoires

| # | Fonction | Détails |
|---|---|---|
| F1 | **Ajouter un produit** | nom, prix > 0, quantité ≥ 0 ; si le produit existe, cumuler la quantité |
| F2 | **Vendre** | client, produit, quantité ; vérifier le stock ; mettre à jour le stock |
| F3 | **Remise** | 5 % si le total dépasse 10 000 FCFA |
| F4 | **Reçu** | affichage aligné : date, client, produit, remise, total en FCFA **et** en euros |
| F5 | **Voir le stock** | tableau trié par nom |
| F6 | **Alertes** | liste des produits dont la quantité est ≤ 5 |
| F7 | **Chiffre d'affaires** | total des ventes, meilleur client |
| F8 | **Sauvegarde / chargement** | JSON ; le programme retrouve ses données au redémarrage |
| F9 | **Export CSV** | journal des ventes lisible dans un tableur |

### 2.2 Contraintes techniques

1. **Aucune saisie ne doit faire planter le programme** (texte à la place d'un nombre, produit inconnu, stock insuffisant…) :
   messages clairs et nouvelle tentative.
2. Le code est organisé en **plusieurs modules** : `stock`, `ventes`, `stockage`, `affichage`, `main`.
3. La logique (calculs) est **séparée** de l'affichage et des `input()`.
4. Des **exceptions personnalisées** pour les erreurs métier.
5. Au moins **15 tests `pytest`** : cas normaux, limites, erreurs, fichiers (`tmp_path`).
6. Code formaté (`ruff format`), sans erreur `ruff check`, avec **docstrings** et un **README**.

### 2.3 Pour aller plus loin (bonus)

- Plusieurs articles par vente (panier).
- Statistiques par mois avec un **graphique matplotlib**.
- Interface en ligne de commande avec `argparse` (`python -m boutique vendre --client ...`).
- Gestion de deux monnaies, historique des prix.
- Un mot de passe pour accéder au programme (jamais en clair : voir le module `hashlib`).

## 3. Méthode de travail conseillée

1. **Comprendre** : relis le cahier des charges, liste les cas particuliers.
2. **Concevoir sur papier** : quelles données ? quelles fonctions ? quels modules ?
3. **Avancer par petites étapes**, une fonctionnalité à la fois : écrire le test, puis le code (TDD), puis committer.
4. **Tester à la main** avec le menu, puis automatiquement avec `pytest`.
5. **Relire** : noms, docstrings, doublons, fonctions trop longues.
6. **Rédiger le README** : installation, utilisation, tests, structure.

Planning indicatif :

| Séance | Travail |
|---|---|
| 1 | Conception, structure des dossiers, `stock.py` + tests |
| 2 | `ventes.py` (remise, journal) + tests |
| 3 | `stockage.py` (JSON, CSV) + tests |
| 4 | `affichage.py`, `main.py` (menu, saisies robustes) |
| 5 | Finitions : style, docstrings, README, bonus |

## 4. Barème (sur 100 points)

| Critère | Points |
|---|---|
| Fonctionnalités F1–F9 correctes | 35 |
| Robustesse (aucun plantage sur saisie invalide, erreurs gérées) | 15 |
| Organisation en modules, séparation logique/affichage | 10 |
| Tests (≥ 15, pertinents, qui passent) | 15 |
| Qualité du code (noms, style, `ruff` propre, fonctions courtes) | 10 |
| Documentation (docstrings, README) | 10 |
| Originalité / bonus | 5 |

**Seuil de réussite : 70/100.**

## 5. Solution de référence

Une solution complète se trouve dans [`../projets/synthese_boutique/`](../projets/synthese_boutique/) avec ses tests
([`test_boutique.py`](../projets/synthese_boutique/test_boutique.py)). **Ne la consulte qu'après avoir terminé le tien**
— ou en cas de blocage prolongé, pour comparer une partie précise.

Lancer la solution :

```powershell
python -m parcours.p01_python_fondamentaux.projets.synthese_boutique.main
python -m pytest parcours/p01_python_fondamentaux/projets
```

## 6. Après le projet

Félicitations ! Tu maîtrises les **fondamentaux de Python**. Prochaine étape : le parcours **P02 — POO et
conception**, où tu transformeras ce projet avec des classes (`Produit`, `Stock`, `Vente`) pour un code encore
plus propre.
