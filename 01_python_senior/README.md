# Module 01 — Python senior : les fondations avancées

Objectif : maîtriser les mécanismes du langage qu'un développeur Python senior utilise
quotidiennement — typing statique, POO avancée, générateurs, async, tests, performance.

## Plan des leçons

| # | Leçon | Statut |
|---|-------|--------|
| 1.1 | Typing avancé & structures de données | ✅ disponible |
| 1.2 | POO avancée | à venir |
| 1.3 | Fonctions avancées & `functools` | à venir |
| 1.4 | Itérateurs & générateurs | à venir |
| 1.5 | Erreurs & context managers | à venir |
| 1.6 | Programmation asynchrone | à venir |
| 1.7 | Concurrence & parallélisme | à venir |
| 1.8 | Performance & profiling | à venir |
| 1.9 | Tests professionnels (pytest, hypothesis) | à venir |
| 1.10 | Packaging & outillage | à venir |

Les leçons sont ajoutées au fil de la progression plutôt que toutes générées d'un coup :
dis-moi quand tu as terminé une leçon (exercices + solution comprises) et je crée la suivante.

## Comment travailler une leçon

1. Lire `lecons/NN_sujet.md`.
2. Ouvrir `exercices/exNN_sujet.py` : compléter les fonctions/classes marquées `# TODO`.
3. Lancer les tests de l'exercice :
   ```powershell
   ..\venv\Scripts\python.exe -m pytest 01_python_senior\exercices\test_exNN_sujet.py -v
   ```
4. Une fois les tests verts, comparer avec `solutions/solNN_sujet.py`.
5. Vérifier le typage strict :
   ```powershell
   ..\venv\Scripts\python.exe -m mypy 01_python_senior\solutions\solNN_sujet.py
   ```

## Mini-projet de fin de module

CLI robuste et typée (voir `projet/README.md`, ajouté après la dernière leçon).
