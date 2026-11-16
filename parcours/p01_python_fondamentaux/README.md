# P01 — Python Fondamentaux

**Cycle :** Licence 1 · **Niveau :** débutant complet · **Crédits :** 30 · **Durée :** ≈ 10 semaines à 6 h/semaine

Aucun prérequis : si tu sais allumer un ordinateur, tu peux commencer.
À la fin, tu écris des programmes console complets, lis et écris des fichiers, gères les erreurs
et organises ton code en fonctions et modules.

## Plan du parcours

| Module | Titre | Leçons | Statut |
|---|---|---|---|
| M1 | Premiers pas | 1.1 Premier programme · 1.2 Variables et nombres · 1.3 Le texte · 1.4 Entrées et sorties | ✅ terminé |
| M2 | Prendre des décisions | 2.1 Booléens et comparaisons · 2.2 `if / elif / else` · 2.3 `match` | ✅ leçons terminées (mini-projet à venir) |
| M3 | Répéter | 3.1 `while` · 3.2 `for` et `range` · 3.3 `break`, `continue`, boucles imbriquées | ⏳ |
| M4 | Les collections | 4.1 Listes · 4.2 Tuples · 4.3 Dictionnaires · 4.4 Ensembles · 4.5 Compréhensions | ⏳ |
| M5 | Les fonctions | 5.1 Définir et appeler · 5.2 Paramètres et valeurs par défaut · 5.3 Portée · 5.4 Fonctions comme valeurs | ⏳ |
| M6 | Fichiers et erreurs | 6.1 Lire/écrire des fichiers · 6.2 CSV et JSON · 6.3 Exceptions · 6.4 `pathlib` | ⏳ |
| M7 | Modules et environnement | 7.1 Importer · 7.2 Bibliothèque standard · 7.3 `venv` et `pip` · 7.4 Écrire ses modules | ⏳ |
| M8 | Maths et algorithmique | 8.1 Module `math` et formules (aire, intérêts, pourcentages) · 8.2 `statistics`, `random`, `decimal`, `fractions` · 8.3 Tableaux à 2 dimensions (listes de listes, matrices) · 8.4 Algorithmes classiques (recherche, tri, suite de Fibonacci, nombres premiers) | ⏳ |
| M9 | Premiers graphiques | 9.1 Dessiner avec `turtle` · 9.2 Courbes et histogrammes avec `matplotlib` · 9.3 Représenter une fonction mathématique · 9.4 Graphique des ventes d'une boutique | ⏳ |
| M10 | Écrire du bon code | 10.1 Déboguer · 10.2 Premiers tests · 10.3 Style PEP 8 · 10.4 Documenter | ⏳ |
| M11 | Projets | Mini-projets de chaque module + **projet de synthèse : gestion de boutique en console** | ⏳ |

## Comment travailler une leçon

1. Lis `lecons/lNN_sujet.md` en **tapant** les exemples toi-même (ne copie pas).
2. Ouvre `exercices/exNN_sujet.py` et remplace chaque `raise NotImplementedError` par ton code.
3. Lance les tests :
   ```powershell
   pytest parcours/p01_python_fondamentaux/exercices/test_ex01_premiers_pas.py -v
   ```
4. Quand tout est vert, compare avec `solutions/solNN_sujet.py`.
5. Réponds au quiz en bas de la leçon.

## Évaluation

Quiz et exercices ≥ 70 % par module, plus le projet de synthèse → **Certificat « Python Fondamentaux »**.
