# Formation Python Senior — Data & Backend

Formation complète et pratique pour atteindre un niveau **senior** en Python sur quatre axes :
Data Analyst, Data Engineer, Data Scientist, et développement Backend robuste/sécurisé.

Le programme détaillé est dans [`CURRICULUM.md`](./CURRICULUM.md).

## Démarrage rapide

```powershell
# Activer l'environnement virtuel
.\venv\Scripts\Activate.ps1

# Installer/mettre à jour les dépendances
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Vérifier que tout fonctionne
pytest --version
ruff --version
mypy --version
```

## Arborescence

```
.
├── 00_setup/            Vérifications d'environnement, prise en main des outils
├── 01_python_senior/    Fondations avancées du langage (typing, OOP, async, perf, tests)
├── 02_data_analyst/     Pandas/Polars, SQL, visualisation, reporting
├── 03_data_engineer/    Pipelines ETL/ELT, bases de données, orchestration, formats de données
├── 04_data_science/     Statistiques, machine learning, évaluation de modèles
├── 05_backend/          FastAPI/Django, architecture, sécurité, tests, déploiement
└── projects/            Projets fil rouge combinant plusieurs axes
```

Chaque module `NN_xxx/` suit la même structure :

```
NN_module/
├── README.md       Objectifs du module et plan des leçons
├── lecons/          Théorie concise (fichiers Markdown numérotés)
├── exercices/        Katas et exercices à trous (squelettes de code)
├── solutions/         Corrections commentées des exercices
└── projet/            Mini-projet réel de fin de module
```

## Méthode de travail

1. Lire la leçon théorique correspondante dans `lecons/`.
2. Faire les exercices dans `exercices/` sans regarder `solutions/`.
3. Comparer avec la solution, comprendre les écarts.
4. Réaliser le mini-projet du module dans `projet/`.
5. Lancer `pytest`, `ruff check`, `mypy` sur son propre code avant de passer au module suivant.

## Qualité de code — à respecter dès le premier exercice

- **Type hints partout** (`mypy --strict` doit passer sans erreur en dehors de `exercices/`).
- **Tests** pour toute fonction non triviale (`pytest`, viser une couverture significative).
- **Formatage automatique** : `ruff format .` avant chaque commit.
- **Lint** : `ruff check .` doit être propre.
- Committer régulièrement (un commit par exercice/module terminé) pour suivre la progression.
