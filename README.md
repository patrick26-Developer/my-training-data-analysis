# Mayele Python Académie

> *Mayele* (lingala) : le savoir, l'intelligence, la débrouillardise.

Plateforme de formation complète à Python, **du premier `print()` jusqu'à l'expertise sénior**,
pensée pour les apprenants du **Congo-Brazzaville** et de l'Afrique francophone.
Organisation inspirée du système **LMD** (Licence – Master – Doctorat).

## Où en est-on ?

| Parcours | Statut |
|---|---|
| P01 Python Fondamentaux | ✅ complet (11 modules, 39 leçons, projet de synthèse, examen final) |
| P03 Python Avancé | 🟡 1 leçon disponible (sera complété après P01 et P02) |
| Autres parcours | ⏳ planifiés, voir [`docs/CURSUS.md`](docs/CURSUS.md) |

Principe : **un parcours est terminé complètement avant d'ouvrir le suivant.**

## Documentation

- [`docs/CURSUS.md`](docs/CURSUS.md) — les 12 parcours, le LMD, les crédits et les certificats
- [`docs/MODELE_DE_LECON.md`](docs/MODELE_DE_LECON.md) — la structure commune à toutes les leçons
- [`docs/PLATEFORME.md`](docs/PLATEFORME.md) — architecture du futur site web et feuille de route

## Arborescence

```
.
├── docs/                          Documentation du projet
└── parcours/
    ├── p01_python_fondamentaux/
    ├── p03_python_avance/
    └── pNN_.../                   (créés au fur et à mesure)
        ├── README.md              Plan du parcours
        ├── lecons/                Cours en Markdown
        ├── exercices/             Exercices à compléter + tests
        ├── solutions/             Corrigés commentés + tests
        └── projets/               Mini-projets et projet de synthèse
```

## Démarrage rapide (Windows / PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Tester **les solutions** (toujours vertes) :

```powershell
pytest
```

Faire **un exercice** (rouge au début, vert quand tu as réussi) :

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex01_premiers_pas.py -v
```

## Qualité de code

`ruff check .`, `ruff format .`, `mypy` et `pytest` doivent passer avant chaque commit.
