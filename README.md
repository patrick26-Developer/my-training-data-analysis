# Mayele Python Académie

> *Mayele* (lingala) : le savoir, l'intelligence, la débrouillardise.

Plateforme de formation complète à Python, **du premier `print()` jusqu'à l'expertise sénior**,
pensée pour les apprenants du **Congo-Brazzaville** et de l'Afrique francophone.
Organisation inspirée du système **LMD** (Licence – Master – Doctorat).

## Où en est-on ?

| Parcours | Statut |
|---|---|
| P01 Python Fondamentaux | ✅ complet (11 modules, 39 leçons, projet de synthèse, examen final) |
| P02 POO et conception | ✅ contenu livré : [6 modules, exercices, boutique et examen](parcours/p02_poo_et_conception/README.md) |
| P03 Python Avancé | 🟡 1 leçon disponible (sera complété après P01 et P02) |
| Autres parcours | ⏳ planifiés, voir [`docs/CURSUS.md`](docs/CURSUS.md) |

Principe : **un parcours est terminé complètement avant d'ouvrir le suivant.**

## Documentation

- [`docs/CURSUS.md`](docs/CURSUS.md) — les 12 parcours, le LMD, les crédits et les certificats
- [`docs/MODELE_DE_LECON.md`](docs/MODELE_DE_LECON.md) — la structure commune à toutes les leçons
- [`docs/PLATEFORME.md`](docs/PLATEFORME.md) — architecture du futur site web et feuille de route
- [`docs/GUIDE_DE_STYLE.md`](docs/GUIDE_DE_STYLE.md) — écrire des leçons qui donnent envie d'apprendre
- [`docs/TARIFS.md`](docs/TARIFS.md) — publics (élèves, étudiants, enseignants, entreprises…), licences et packs
- [`docs/pages_de_vente/`](docs/pages_de_vente/) — textes de pages de vente par parcours
- [`catalogue/`](catalogue/) — `tarifs.toml` (tu règles les prix) et `catalogue.json` (lu par ta plateforme)

## Outils du projet

| Commande | Rôle |
|---|---|
| `python outils/verifier_lecons.py` | exécute les exemples de code des leçons pour vérifier qu'ils fonctionnent |
| `python outils/sync_tests_solutions.py` | génère les tests des solutions à partir de ceux des exercices |
| `python outils/ajouter_cadre_lecons.py` | ajoute l'accroche et le « Bravo » des leçons P01 |
| `python outils/generer_catalogue.py` | génère `catalogue/catalogue.json` (parcours, durées, prix par public) |

## Arborescence

```
.
├── docs/                          Documentation du projet
└── parcours/
    ├── p01_python_fondamentaux/
    ├── p02_poo_et_conception/
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

`ruff check .`, `ruff format --check .` et `pytest` doivent passer avant chaque commit.
Le typage strict porte sur le code typé publié, pas sur les squelettes incomplets :
`mypy parcours/p03_python_avance/solutions/sol01_typing_et_structures_de_donnees.py`.
P01 et P02 sont exclus de mypy : les annotations avancées sont enseignées en P03.

P01 et P02 sont validés techniquement ; relecture humaine et essais avec de vrais
débutants restent à réaliser. Les certificats sont pour l'instant des règles de
validation : le site, les comptes et le paiement sont à construire.
