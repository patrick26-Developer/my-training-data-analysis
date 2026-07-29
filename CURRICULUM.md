# Programme de formation — Python niveau senior

Progression séquentielle : chaque module s'appuie sur les précédents. Théorie courte (fichiers dans `lecons/`),
beaucoup de pratique (`exercices/` puis `projet/`).

---

## Module 00 — Setup (fait)

Environnement vérifié : Python 3.13.5, venv, dépendances runtime + dev installées, Git initialisé,
config qualité (`pyproject.toml`) en place.

---

## Module 01 — Python senior : les fondations avancées

Objectif : écrire du Python idiomatique, typé, testé et performant — le socle commun aux 4 spécialisations.

| # | Sujet | Points clés |
|---|-------|-------------|
| 1.1 | Typing avancé & structures de données | `dataclasses`, `NamedTuple`, `TypedDict`, `Protocol`, `Generic`, `Literal`, `overload`, `mypy --strict` |
| 1.2 | POO avancée | héritage vs composition, ABC, mixins, dunder methods, `@property`, descriptors, `__slots__` |
| 1.3 | Fonctions avancées | closures, décorateurs paramétrés, `functools` (`lru_cache`, `wraps`, `partial`, `reduce`, `singledispatch`) |
| 1.4 | Itérateurs & générateurs | protocole itérateur, `yield`/`yield from`, `itertools`, générateurs infinis/paresseux |
| 1.5 | Erreurs & context managers | exceptions custom, chaînage (`raise ... from`), `contextlib`, gestion de ressources |
| 1.6 | Programmation asynchrone | `asyncio`, `async`/`await`, `Task`, `gather`, `Queue`, client HTTP async (`httpx`) |
| 1.7 | Concurrence & parallélisme | GIL, `threading` vs `multiprocessing` vs `asyncio`, `concurrent.futures`, quand choisir quoi |
| 1.8 | Performance & profiling | complexité algorithmique, `cProfile`, `timeit`, vectorisation NumPy, pièges de perf courants |
| 1.9 | Tests professionnels | `pytest` (fixtures, `parametrize`, `monkeypatch`, mocking), `hypothesis` (property-based testing), TDD |
| 1.10 | Packaging & outillage | structure de package, `pyproject.toml`, `ruff`, `pre-commit`, bases de CI |

**Mini-projet** : CLI robuste (gestionnaire de tâches concurrent ou scraper asynchrone) — typée strict,
testée (>90% coverage), packagée, avec pre-commit configuré.

---

## Module 02 — Data Analyst

Objectif : explorer, nettoyer, transformer et communiquer des données efficacement.

| # | Sujet | Points clés |
|---|-------|-------------|
| 2.1 | Pandas & Polars fondamentaux | `Series`/`DataFrame`, indexation, sélection, différences Pandas/Polars |
| 2.2 | Nettoyage de données | valeurs manquantes, doublons, typage, détection d'outliers |
| 2.3 | Transformation & agrégation | `groupby`, `pivot_table`, `merge`/`join`, reshaping (`melt`/`pivot`) |
| 2.4 | SQL pour l'analyse | requêtes complexes, window functions, CTE — pratiqué avec DuckDB/SQLite |
| 2.5 | Visualisation | `matplotlib`, `seaborn`, `plotly` — choisir le bon graphique, storytelling |
| 2.6 | Reporting automatisé | export Excel (`openpyxl`), génération de rapports reproductibles |
| 2.7 | Analyse exploratoire (EDA) | méthodologie complète, `missingno`, détection de signaux |

**Mini-projet** : analyse complète d'un dataset réel (ventes/opérations) → rapport EDA + dashboard de visualisations.

---

## Module 03 — Data Engineer

Objectif : construire des pipelines de données fiables, testés et scalables.

| # | Sujet | Points clés |
|---|-------|-------------|
| 3.1 | Formats de données | CSV/JSON vs Parquet/Arrow, colonne vs ligne, `pyarrow` |
| 3.2 | Bases relationnelles | SQL avancé, `SQLAlchemy` (Core + ORM), migrations avec `alembic` |
| 3.3 | Stores clé-valeur / cache | Redis — cas d'usage cache, files, TTL |
| 3.4 | Pipelines ETL/ELT | extraction, transformation, chargement, idempotence, gestion des reprises |
| 3.5 | Orchestration | DAGs, scheduling, dépendances entre tâches (concepts Airflow/Prefect) |
| 3.6 | Qualité & validation des données | schémas `Pydantic`, contrats de données, tests de pipeline |
| 3.7 | Traitement à l'échelle | Polars vs Pandas, DuckDB pour l'analytique, traitement par lots/streaming |
| 3.8 | Modélisation analytique | schéma en étoile, dimensions/faits, data warehouse vs data lake |

**Mini-projet** : pipeline ETL complet (source CSV/API → transformation → entrepôt DuckDB/Postgres),
testé, idempotent, orchestré par un scheduler simple.

---

## Module 04 — Data Science

Objectif : construire et évaluer des modèles prédictifs de bout en bout.

| # | Sujet | Points clés |
|---|-------|-------------|
| 4.1 | Statistiques appliquées | distributions, tests d'hypothèses, corrélation vs causalité |
| 4.2 | Préparation pour le ML | encodage, scaling, feature engineering, `Pipeline` scikit-learn |
| 4.3 | ML supervisé | régression, classification, arbres, `RandomForest`, `XGBoost`/`LightGBM` |
| 4.4 | ML non supervisé | clustering (k-means, DBSCAN), réduction de dimension (PCA) |
| 4.5 | Évaluation de modèles | validation croisée, métriques adaptées, overfitting, tuning d'hyperparamètres |
| 4.6 | Introduction Deep Learning | réseaux de neurones (Keras/PyTorch), cas d'usage pertinents |
| 4.7 | MLOps de base | reproductibilité, versioning de modèles, mise en production via API |

**Mini-projet** : cas de prédiction complet (EDA → feature engineering → modèle → évaluation),
puis exposition du modèle via une API (lien direct avec le module 5).

---

## Module 05 — Backend robuste, sécurisé, professionnel

Objectif : construire une API de production : sécurisée, testée, observable, déployable.

| # | Sujet | Points clés |
|---|-------|-------------|
| 5.1 | Architecture logicielle | couches, injection de dépendances, principes SOLID en Python |
| 5.2 | API REST avec FastAPI | routing, validation `Pydantic`, dépendances, endpoints async |
| 5.3 | Base de données en prod | `SQLAlchemy` async, migrations, gestion des transactions |
| 5.4 | Authentification & sécurité | JWT, hash de mots de passe (`passlib`/`bcrypt`), OAuth2, rôles/permissions, protection injection SQL/XSS/CSRF, rate limiting |
| 5.5 | Tests backend | unitaires, intégration (DB de test), `TestClient`, mocking de services externes |
| 5.6 | Tâches asynchrones | files de messages avec `Celery` + `Redis`, tâches en arrière-plan |
| 5.7 | Observabilité | logging structuré, gestion centralisée des erreurs, monitoring |
| 5.8 | Performance & scalabilité | cache Redis, pagination, N+1 queries, tests de charge (`locust`) |
| 5.9 | Conteneurisation & déploiement | Docker, `docker-compose`, variables d'environnement, CI/CD basique |
| 5.10 | Documentation & design d'API | OpenAPI/Swagger, versionnement, conventions REST |

**Mini-projet final** : API production-ready — auth JWT, CRUD sécurisé, tests (>80% coverage),
Dockerisée, tâches async avec Celery/Redis, connectée à Postgres.

---

## Projet fil rouge (`projects/`)

Une fois les 5 modules complétés : plateforme end-to-end combinant les 4 axes —
ingestion de données (Data Engineer) → stockage → analyse exploratoire (Data Analyst) →
modèle prédictif (Data Science) → API sécurisée exposant le tout (Backend).

---

## Suivi de progression

- [ ] Module 01 — Python senior
- [ ] Module 02 — Data Analyst
- [ ] Module 03 — Data Engineer
- [ ] Module 04 — Data Science
- [ ] Module 05 — Backend robuste
- [ ] Projet fil rouge
