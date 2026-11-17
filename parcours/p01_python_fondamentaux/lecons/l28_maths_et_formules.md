# Leçon 8.1 — Le module `math` et les formules

⏱ 55 min · 🎯 Intermédiaire · 📦 Prérequis : module 7

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Aires, intérêts, mensualités d'un prêt, équations : tu vas traduire de vraies formules en programmes qui calculent à ta place.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Utiliser `math` : racines, puissances, logarithmes, trigonométrie, arrondis
- Traduire une **formule mathématique** en code Python
- Calculer aires, volumes, intérêts, pourcentages, équations du 2ᵉ degré
- Comparer des nombres décimaux sans se faire piéger

---

## 1. Le problème

« Quelle est la mensualité d'un prêt de 2 000 000 FCFA sur 24 mois à 12 % par an ? » Une formule existe, mais encore
faut-il savoir l'écrire correctement en Python. Cette leçon t'apprend à passer de **la formule sur le papier** à
**la fonction qui calcule**.

## 2. Pas à pas

### 2.1 Les opérateurs, rappel

```python
2**3  # 8      puissance
10**-2  # 0.01
17 // 5  # 3      quotient entier
17 % 5  # 2      reste
abs(-7)  # 7
round(3.14159, 2)  # 3.14
divmod(17, 5)  # (3, 2)
pow(2, 10)  # 1024 (idem 2 ** 10)
pow(2, 10, 1000)  # 24   (2**10 modulo 1000)
```

### 2.2 Le module `math`

```python
import math

math.sqrt(144)  # 12.0     racine carrée
math.isqrt(150)  # 12       racine entière
math.pi, math.e  # 3.14159..., 2.71828...
math.ceil(2.1)  # 3        arrondi supérieur
math.floor(2.9)  # 2        arrondi inférieur
math.trunc(-2.9)  # -2       coupe la partie décimale
math.factorial(5)  # 120
math.gcd(48, 18)  # 6        PGCD
math.lcm(4, 6)  # 12       PPCM
math.comb(5, 2)  # 10       combinaisons (5 parmi 2)
math.perm(5, 2)  # 20       arrangements
math.hypot(3, 4)  # 5.0      hypoténuse
math.dist((0, 0), (3, 4))  # 5.0  distance entre deux points
```

Logarithmes et exponentielle :

```python
math.exp(1)  # 2.718...
math.log(math.e)  # 1.0     logarithme népérien
math.log10(1000)  # 3.0
math.log2(1024)  # 10.0
math.log(8, 2)  # 3.0     logarithme en base 2
```

Trigonométrie (angles en **radians**) :

```python
math.sin(math.pi / 2)  # 1.0
math.cos(0)  # 1.0
math.degrees(math.pi)  # 180.0
math.radians(90)  # 1.5707...
```

### 2.3 Traduire une formule en code

Méthode : (1) nommer chaque lettre par une variable claire ; (2) écrire la formule avec des parenthèses explicites.

**Aire d'un disque** : A = π × r²

```python
def aire_disque(rayon):
    return math.pi * rayon**2
```

**Intérêts composés** : C = C₀ × (1 + t)ⁿ

```python
def capital_final(capital, taux_annuel, annees):
    return capital * (1 + taux_annuel / 100) ** annees
```

**Mensualité d'un prêt** : M = C × i / (1 − (1 + i)⁻ⁿ), avec i le taux mensuel, n le nombre de mois

```python
def mensualite(capital, taux_annuel, mois):
    i = taux_annuel / 100 / 12
    if i == 0:
        return capital / mois
    return capital * i / (1 - (1 + i) ** -mois)


print(round(mensualite(2_000_000, 12, 24)))  # 94147
```

**Équation du 2ᵉ degré** : ax² + bx + c = 0, Δ = b² − 4ac

```python
def resoudre(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        return []  # pas de solution réelle
    if delta == 0:
        return [-b / (2 * a)]
    racine = math.sqrt(delta)
    return [(-b - racine) / (2 * a), (-b + racine) / (2 * a)]


print(resoudre(1, -3, 2))  # [1.0, 2.0]
```

### 2.4 Pourcentages

```python
def augmenter(prix, pourcent):
    return prix * (1 + pourcent / 100)


def reduire(prix, pourcent):
    return prix * (1 - pourcent / 100)


def variation(ancien, nouveau):
    return (nouveau - ancien) / ancien * 100


print(variation(500, 650))  # 30.0  (% d'augmentation)
```

### 2.5 Comparer des décimaux

```python
print(0.1 + 0.2 == 0.3)  # False
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

### 2.6 Nombres spéciaux

```python
math.inf  # infini
math.nan  # « pas un nombre »
math.isnan(math.nan)  # True
math.sqrt(-1)  # ValueError: math domain error
```

Pour les nombres complexes : `import cmath`.

## 3. ⚠️ Pièges courants

**Degrés vs radians** : `math.sin(90)` n'est **pas** 1. Convertis : `math.sin(math.radians(90))`.

**Division entière** : `5 / 2 = 2.5` mais `5 // 2 = 2`.

**Priorité** : `-2 ** 2` vaut `-4` (la puissance passe avant le signe). Écris `(-2) ** 2`.

**Erreur de domaine** : `math.sqrt(-4)`, `math.log(0)` → `ValueError`.

**`==` entre flottants** : utilise `math.isclose`.

## 4. À retenir

- `math` : `sqrt`, `pi`, `ceil`, `floor`, `log`, `sin`, `cos`, `gcd`, `comb`, `hypot`, `isclose`…
- Une formule = des variables bien nommées + des parenthèses.
- Angles en radians ; `isclose` pour comparer des décimaux.

## 5. Exercices

Fichier : [`exercices/ex28_maths_et_formules.py`](../exercices/ex28_maths_et_formules.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex28_maths_et_formules.py -v
```

## 6. Quiz

1. Quelle fonction donne le plafond de `2.1` ?
2. En quelle unité `math.sin` attend-il l'angle ?
3. Pourquoi ne pas écrire `0.1 + 0.2 == 0.3` ?
4. Que vaut `-3 ** 2` ?

<details>
<summary>Réponses</summary>

1. `math.ceil(2.1)`, soit `3`.
2. En radians.
3. À cause des erreurs d'arrondi des flottants : utilise `math.isclose`.
4. `-9`.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Les mathématiques ne te font plus peur : tu les fais travailler pour toi.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 8.2 — Calculs exacts, hasard et statistiques](l29_nombres_exacts_et_statistiques.md).
<!-- /cadre:fin -->
