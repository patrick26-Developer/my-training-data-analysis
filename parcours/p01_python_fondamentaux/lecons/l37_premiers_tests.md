# Leçon 10.2 — Tes premiers tests

⏱ 60 min · 🎯 Intermédiaire · 📦 Prérequis : leçon 10.1

## 🎯 Ce que tu sauras faire

- Écrire des tests avec `assert` et `pytest`
- Choisir de bons cas de test (normaux, limites, erreurs)
- Utiliser `parametrize`, `pytest.raises`, les fixtures simples
- Pratiquer le **TDD** : écrire le test **avant** le code

---

## 1. Le problème

Tu corriges un bug… et tu en crées un autre ailleurs sans le savoir. Relancer le programme à la main avec quelques
valeurs ne suffit pas. Un **test automatique** vérifie en une seconde que tout fonctionne encore. Tu l'as déjà
utilisé : les `pytest` de ce cours sont des tests !

## 2. L'idée en images

```
       code à tester          test
     ┌──────────────┐     ┌──────────────────────────────┐
     │ prix_ttc(...)│ ◄── │ assert prix_ttc(1000) == 1180│
     └──────────────┘     └──────────────────────────────┘
                              ✔ vert ou ✘ rouge
```

## 3. Pas à pas

### 3.1 `assert`

```python
assert 2 + 2 == 4  # ne fait rien : l'affirmation est vraie
assert 2 + 2 == 5, "maths cassées"  # AssertionError: maths cassées
```

### 3.2 Un premier fichier de test

`calculs.py` :

```python
def prix_ttc(prix_ht, taux=18):
    return prix_ht * (1 + taux / 100)
```

`test_calculs.py` :

```python
from calculs import prix_ttc


def test_prix_ttc_taux_par_defaut():
    assert prix_ttc(1000) == 1180


def test_prix_ttc_taux_zero():
    assert prix_ttc(1000, 0) == 1000
```

Lancer :

```powershell
python -m pytest -v
```

Règles de `pytest` :
- fichiers nommés `test_*.py` ;
- fonctions nommées `test_*` ;
- un test **échoue** si une exception (souvent `AssertionError`) est levée.

### 3.3 Que tester ? La règle des trois familles

1. **Cas normaux** : `prix_ttc(1000, 18)`.
2. **Cas limites** : `0`, liste vide, un seul élément, valeur maximale.
3. **Cas d'erreur** : entrée invalide → exception attendue.

### 3.4 Comparer des flottants

```python
import pytest

assert 0.1 + 0.2 == pytest.approx(0.3)
```

### 3.5 Tester qu'une erreur est levée

```python
import pytest


def test_division_par_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_message_d_erreur():
    with pytest.raises(ValueError, match="positif"):
        retirer(1000, -5)
```

### 3.6 `parametrize` : un test, plusieurs cas

```python
@pytest.mark.parametrize(
    ("n", "attendu"),
    [(0, True), (1, False), (2, True), (-4, True)],
)
def test_est_pair(n, attendu):
    assert est_pair(n) is attendu
```

### 3.7 Fixtures : préparer des données

```python
@pytest.fixture
def panier():
    return ["Riz", "Sel"]


def test_taille(panier):
    assert len(panier) == 2
```

`tmp_path` (dossier temporaire) et `capsys` (capturer `print`) sont des fixtures fournies par pytest.

### 3.8 Le TDD : tester d'abord

Cycle **Rouge → Vert → Refactorisation** :

1. **Rouge** : écris un test qui échoue (la fonction n'existe pas ou est fausse).
2. **Vert** : écris le code **minimal** pour qu'il passe.
3. **Refactorisation** : améliore le code, les tests restent verts.

Exemple : « `est_bissextile(2000)` doit être vrai » → test → code simple → nouveau test (1900) → code corrigé…

### 3.9 Ce qu'un bon test est

- **Rapide**, **indépendant** (n'influence pas les autres), **déterministe** (pas de hasard non contrôlé),
- **lisible** : le nom dit ce qui est vérifié (`test_remise_100_pourcent_donne_zero`),
- un test = **une idée**.

### 3.10 Mesurer la couverture

```powershell
python -m pytest --cov=calculs --cov-report=term-missing
```

La **couverture** indique quel pourcentage du code est exécuté par les tests. 100 % ne garantit pas l'absence de
bugs, mais une couverture très faible est un signal d'alerte.

## 4. ⚠️ Pièges courants

- **Tester l'implémentation plutôt que le comportement** : le test casse à chaque refactorisation.
- **Tests dépendants entre eux** (l'un prépare ce dont l'autre a besoin).
- **Pas de cas limites** : les bugs se cachent aux bords.
- **`assert` avec flottants** sans `approx`.
- **Tests qui lisent le réseau ou l'heure réelle** : instables.

## 5. À retenir

- `test_*.py`, `test_*()`, `assert`, `python -m pytest`.
- Teste cas normaux, limites, erreurs.
- `parametrize`, `pytest.raises`, `pytest.approx`, fixtures.
- TDD : rouge, vert, refactorisation.

## 6. Exercices : écris les tests !

Fichier : [`exercices/ex37_premiers_tests.py`](../exercices/ex37_premiers_tests.py)

Cette fois, **tu écris les tests**. Chaque fonction `tests_pour_xxx(fonction)` reçoit une implémentation de `xxx`
et doit :
- **ne rien lever** si l'implémentation est correcte ;
- **échouer** (un de tes `assert`, ou un `pytest.raises` qui ne trouve pas l'erreur attendue) si l'implémentation est boguée.

Nos tests vérifient tes tests contre une bonne version **et plusieurs versions boguées** (« mutants »).

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex37_premiers_tests.py -v
```

## 7. Quiz

1. Comment s'appellent les fichiers de test détectés par pytest ?
2. À quoi sert `pytest.approx` ?
3. Que signifie TDD ?
4. Cite les trois familles de cas à tester.

<details>
<summary>Réponses</summary>

1. `test_*.py` (ou `*_test.py`).
2. À comparer des nombres flottants avec une tolérance.
3. *Test-Driven Development* : on écrit le test avant le code.
4. Cas normaux, cas limites, cas d'erreur.

</details>
