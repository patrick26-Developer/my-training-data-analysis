# Leçon 10.3 — Le style : PEP 8 et outils de qualité

⏱ 45 min · 🎯 Intermédiaire · 📦 Prérequis : modules 1 à 7

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Du code lisible, c'est du code que l'on a envie de lire : tu vas découvrir les conventions des professionnels.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Écrire du code **lisible** selon les conventions Python (PEP 8)
- Bien **nommer** variables, fonctions, classes, constantes
- Utiliser un **formateur** (`ruff format`) et un **linter** (`ruff check`)
- Repérer et réécrire du code illisible

---

## 1. Le problème

Un programme est **lu bien plus souvent qu'il n'est écrit** — par ton futur toi, par tes collègues. Deux programmes
qui font la même chose peuvent être l'un clair, l'autre un casse-tête :

```python
def f(a, b, c):
    x = a * b
    if c == True:
        x = x - x * c / 100
    return x
```

contre

```python
def prix_apres_remise(prix_unitaire, quantite, remise_pourcent):
    sous_total = prix_unitaire * quantite
    return sous_total - sous_total * remise_pourcent / 100
```

## 2. PEP 8 : le guide de style officiel

**PEP** = *Python Enhancement Proposal*. La **PEP 8** décrit comment écrire du Python lisible.

### 2.1 Les noms

| Élément | Convention | Exemple |
|---|---|---|
| variable, fonction | `snake_case` (minuscules + `_`) | `prix_total`, `calculer_remise` |
| constante | `MAJUSCULES_AVEC_UNDERSCORES` | `TAUX_TVA`, `MAX_ESSAIS` |
| classe | `PascalCase` (`CamelCase`) | `CompteBancaire` |
| module / fichier | minuscules, `_` si besoin | `gestion_stock.py` |
| « privé » (usage interne) | préfixe `_` | `_cache` |

Choisir de bons noms :
- **Explicites** : `nombre_de_clients`, pas `n` (sauf indices de boucle courts : `i`, `j`) ;
- **Prononçables** et **cohérents** ;
- Fonctions = **verbes** (`calculer_total`), booléens = questions (`est_valide`, `a_du_stock`) ;
- Évite `l`, `O`, `I` (confondus avec `1` et `0`), et les noms qui masquent le langage (`list`, `str`, `sum`, `max`).

### 2.2 Mise en forme

- **4 espaces** par niveau d'indentation (jamais de tabulations mélangées).
- Lignes de **88 à 100 caractères** maximum (ce projet : 100).
- **2 lignes vides** entre fonctions et classes de premier niveau, **1** entre méthodes.
- Espaces autour des opérateurs : `a = b + c`, mais `f(x=1)` (pas d'espaces pour un argument nommé).
- Pas d'espace avant `:` ou `,`, un espace après `,`.
- Imports **en haut du fichier**, un par ligne, groupés : standard, tiers, local.

```python
import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt

from boutique import calculs
```

### 2.3 Commentaires

- Explique le **pourquoi**, pas le **quoi** :

```python
total += 1  # ajoute 1 au total          ← inutile
total += 1  # le client fidèle gagne 1 point bonus  ← utile
```

- Un commentaire qui répète le code est un bruit ; un commentaire qui ment est pire qu'aucun.
- Si tu dois expliquer un bloc entier, **extrais une fonction bien nommée**.

### 2.4 Simplicité

```python
# ❌
if est_valide == True:
    return True
else:
    return False

# ✅
return est_valide
```

```python
# ❌
for i in range(len(liste)):
    print(liste[i])
# ✅
for element in liste:
    print(element)
```

- Compare à `None` avec `is` : `if x is None:`.
- Teste le vide avec la valeur « vraie/fausse » : `if not liste:`.
- Pas de « nombres magiques » : `if age >= 18` → `AGE_MAJORITE = 18`.
- Une fonction = **une seule tâche**, courte (quelques dizaines de lignes au plus).

## 3. Les outils font le travail pour toi

### 3.1 Le formateur : `ruff format`

Il réécrit ton code selon un style uniforme (espaces, guillemets, retours à la ligne).

```powershell
python -m ruff format mon_fichier.py        # formate
python -m ruff format --check .             # vérifie seulement
```

### 3.2 Le linter : `ruff check`

Il détecte des erreurs et des mauvaises pratiques **sans exécuter** le code : variable inutilisée, import oublié,
comparaison inutile, nom non conforme…

```powershell
python -m ruff check .
python -m ruff check --fix .                # corrige ce qui peut l'être
```

### 3.3 Configuration (`pyproject.toml`)

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "N", "UP", "B", "SIM"]
```

(`E` pycodestyle, `F` pyflakes, `I` tri des imports, `N` noms, `UP` syntaxe moderne, `B` bugs probables,
`SIM` simplifications — c'est la configuration de ce projet.)

### 3.4 Dans l'éditeur

Active « format on save » dans VS Code avec l'extension Ruff : ton code se formate à chaque sauvegarde.

### 3.5 Les typages (aperçu)

Les annotations (`def f(x: int) -> str:`) documentent et permettent à `mypy` de vérifier. Approfondi en P03.

### 3.6 Avant chaque commit

```powershell
python -m ruff format .
python -m ruff check .
python -m pytest
```

Les « hooks » `pre-commit` peuvent automatiser cela (parcours P07).

## 4. ⚠️ Pièges courants

- **Appliquer PEP 8 à la lettre au détriment de la clarté** : c'est un guide, pas une loi (« *a foolish consistency…* »).
- **Noms trop courts ou trop longs** : cherche l'équilibre.
- **Mélanger deux styles** dans un même projet : choisis un formateur et laisse-le décider.
- **Commentaires obsolètes** après une modification du code.

## 5. À retenir

- `snake_case` pour fonctions/variables, `PascalCase` pour classes, `MAJUSCULES` pour constantes.
- 4 espaces, lignes courtes, imports groupés, 2 lignes vides entre fonctions.
- Commente le **pourquoi**. Une fonction, une tâche.
- `ruff format` + `ruff check` avant chaque commit.

## 6. Exercices

Fichier : [`exercices/ex38_style_pep8.py`](../exercices/ex38_style_pep8.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex38_style_pep8.py -v
```

## 7. Quiz

1. Quel style de nom pour une constante ? pour une classe ?
2. Que fait `ruff format` ? et `ruff check` ?
3. Pourquoi éviter `list` comme nom de variable ?
4. Qu'est-ce qu'un « nombre magique » ?

<details>
<summary>Réponses</summary>

1. `MAJUSCULES_AVEC_UNDERSCORES` ; `PascalCase`.
2. Le premier met en forme le code ; le second détecte erreurs et mauvaises pratiques.
3. Cela masque la fonction intégrée `list`.
4. Une valeur numérique écrite telle quelle dans le code, sans nom qui explique son rôle.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Ton code a désormais l'allure d'un code professionnel. Les outils font le gros du travail pour toi.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 10.4 — Documenter son code](l39_documenter.md).
<!-- /cadre:fin -->
