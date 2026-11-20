# P03 — Python Avancé

> Prérequis : terminer P01 (Fondamentaux) et P02 (POO) avant de commencer.
> Les leçons 3.1 et 3.2 sont disponibles avec exercices, corrigés et tests.

Objectif : maîtriser les mécanismes du langage qu'un développeur Python senior utilise
quotidiennement — typing statique, POO avancée, générateurs, async, tests, performance.

## Plan des leçons

| # | Leçon | Statut |
|---|-------|--------|
| 3.1 | Typing avancé & structures de données | ✅ disponible |
| 3.2 | [POO avancée](lecons/02_poo_avancee.md) | ✅ disponible |
| 3.3 | Fonctions avancées & `functools` | à venir |
| 3.4 | Itérateurs & générateurs | à venir |
| 3.5 | Erreurs & context managers | à venir |
| 3.6 | Programmation asynchrone | à venir |
| 3.7 | Concurrence & parallélisme | à venir |
| 3.8 | Performance & profiling | à venir |
| 3.9 | Tests professionnels (pytest, hypothesis) | à venir |
| 3.10 | Packaging & outillage | à venir |

Les leçons sont ajoutées au fil de la progression plutôt que toutes générées d'un coup :
dis-moi quand tu as terminé une leçon (exercices + solution comprises) et je crée la suivante.

## Comment travailler une leçon

1. Lire `lecons/NN_sujet.md`.
2. Ouvrir `exercices/exNN_sujet.py` : compléter les fonctions/classes marquées `# TODO`.
3. Lancer les tests de l'exercice :
   ```powershell
   python -m pytest parcours/p03_python_avance/exercices/test_exNN_sujet.py -v
   ```
4. Une fois les tests verts, comparer avec `solutions/solNN_sujet.py`.
5. Vérifier le typage strict :
   ```powershell
   python -m mypy --follow-imports=silent parcours/p03_python_avance/solutions/solNN_sujet.py
   ```

## Mini-projet de fin de module

CLI robuste et typée (voir `projet/README.md`, ajouté après la dernière leçon).
