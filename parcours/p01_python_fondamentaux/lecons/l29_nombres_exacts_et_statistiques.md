# Leçon 8.2 — Calculs exacts, hasard et statistiques

⏱ 55 min · 🎯 Intermédiaire · 📦 Prérequis : leçon 8.1

## 🎯 Ce que tu sauras faire

- Calculer **exactement** avec `decimal` (argent) et `fractions`
- Simuler le hasard avec `random` (dés, tirages, probabilités)
- Résumer des données avec `statistics`
- Estimer une probabilité par simulation (méthode de Monte-Carlo)

---

## 1. Le problème

```python
print(0.1 + 0.2)  # 0.30000000000000004
```

Pour des montants d'argent, une erreur d'un centime répétée un million de fois devient une vraie perte. Et pour
comprendre des données, on a besoin de moyenne, médiane, écart-type. Cette leçon donne les outils.

## 2. Pas à pas

### 2.1 `decimal` : l'argent sans surprise

```python
from decimal import Decimal, ROUND_HALF_UP

a = Decimal("0.1")
b = Decimal("0.2")
print(a + b)  # 0.3   (exact)

prix = Decimal("1999.99")
tva = prix * Decimal("0.18")
print(tva.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))  # 360.00
```

⚠️ Toujours construire un `Decimal` à partir d'un **texte** : `Decimal("0.1")`, pas `Decimal(0.1)`
(le float contient déjà l'erreur).

### 2.2 `fractions` : les fractions exactes

```python
from fractions import Fraction

a = Fraction(1, 3)
b = Fraction(1, 6)
print(a + b)  # 1/2
print(float(a + b))  # 0.5
print(Fraction("0.75"))  # 3/4
```

### 2.3 Hasard avec `random`

```python
import random

random.seed(7)  # graine : résultats reproductibles
random.randint(1, 6)  # un dé
random.choice(["rouge", "bleu"])
random.sample(range(1, 50), 6)  # tirage sans remise
random.choices(["P", "F"], weights=[0.7, 0.3], k=10)  # tirage avec remise pondéré
random.uniform(0, 1)
random.gauss(0, 1)  # loi normale
```

### 2.4 Statistiques descriptives

```python
import statistics as st

notes = [12, 15, 9, 18, 15, 11]
st.mean(notes)  # 13.33  moyenne
st.median(notes)  # 13.5   médiane
st.mode(notes)  # 15     mode
st.pvariance(notes)  # variance de la population
st.pstdev(notes)  # écart-type de la population
st.stdev(notes)  # écart-type d'un échantillon
st.quantiles(notes, n=4)  # quartiles
```

Interprétation rapide :
- **moyenne** : valeur centrale « arithmétique » ;
- **médiane** : valeur qui coupe les données en deux moitiés (robuste aux valeurs extrêmes) ;
- **écart-type** : dispersion autour de la moyenne.

### 2.5 Simulation de Monte-Carlo

Estimer une probabilité en répétant l'expérience.

```python
def probabilite_double_six(essais=100_000):
    succes = 0
    for _ in range(essais):
        if random.randint(1, 6) == 6 and random.randint(1, 6) == 6:
            succes += 1
    return succes / essais


print(probabilite_double_six())  # ≈ 0.0278 (soit 1/36)
```

Estimer π : tire des points dans un carré de côté 1 ; la part de points dans le quart de disque vaut π/4.

```python
def estimer_pi(essais=200_000):
    dedans = sum(1 for _ in range(essais) if random.random() ** 2 + random.random() ** 2 <= 1)
    return 4 * dedans / essais
```

### 2.6 Corrélation (aperçu)

```python
heures = [1, 2, 3, 4, 5]
notes = [8, 11, 12, 15, 17]
print(st.correlation(heures, notes))  # proche de 1 : forte relation positive
```

## 3. ⚠️ Pièges courants

- `Decimal(0.1)` : crée un nombre déjà inexact. Utilise `Decimal("0.1")`.
- Mélanger `Decimal` et `float` : `TypeError`.
- Moyenne d'une liste vide : `StatisticsError`.
- `stdev` (échantillon) ≠ `pstdev` (population) : choisis selon le cas.
- `random` n'est pas sûr pour la sécurité (voir `secrets`).

## 4. À retenir

- `Decimal("…")` pour l'argent ; `Fraction` pour les fractions exactes.
- `random.seed` rend une simulation reproductible.
- `mean`, `median`, `mode`, `stdev`, `quantiles`.
- Plus on répète une simulation, plus l'estimation est précise.

## 5. Exercices

Fichier : [`exercices/ex29_nombres_exacts_et_statistiques.py`](../exercices/ex29_nombres_exacts_et_statistiques.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex29_nombres_exacts_et_statistiques.py -v
```

## 6. Quiz

1. Pourquoi `Decimal("0.1")` plutôt que `Decimal(0.1)` ?
2. Quelle mesure résiste le mieux aux valeurs extrêmes : moyenne ou médiane ?
3. À quoi sert `random.seed(1)` ?
4. Que vaut `Fraction(1, 2) + Fraction(1, 3)` ?

<details>
<summary>Réponses</summary>

1. Un `float` contient déjà l'erreur d'arrondi ; le texte est exact.
2. La médiane.
3. À obtenir les mêmes nombres « aléatoires » à chaque exécution.
4. `Fraction(5, 6)`.

</details>
