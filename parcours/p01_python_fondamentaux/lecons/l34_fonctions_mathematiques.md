# Leçon 9.3 — Représenter une fonction mathématique

⏱ 60 min · 🎯 Intermédiaire · 📦 Prérequis : leçons 8.1, 9.2

## 🎯 Ce que tu sauras faire

- Calculer une **table de valeurs** d'une fonction f(x)
- Tracer des courbes (droite, parabole, sinus, exponentielle…)
- Trouver graphiquement les **zéros** et les extrêmes
- Comparer plusieurs fonctions sur le même graphique

---

## 1. Le problème

Au collège, on trace une courbe point par point sur du papier quadrillé. Python peut calculer **des centaines de points
en un clin d'œil** et les relier. C'est la base de la visualisation scientifique, de l'économie, de la physique.

## 2. L'idée en images

Tracer y = f(x) = x² revient à :
1. choisir des valeurs de x régulièrement espacées (de −3 à 3 par exemple) ;
2. calculer y pour chacune ;
3. relier les points (x, y).

```
 x : -3  -2  -1   0   1   2   3
 y :  9   4   1   0   1   4   9
```

Plus on prend de points, plus la courbe est lisse.

## 3. Pas à pas

### 3.1 Une suite de x régulièrement espacés

Python n'a pas de `linspace` intégré ; on le fabrique :

```python
def linspace(debut, fin, n):
    """n valeurs régulièrement espacées de debut à fin (inclus)."""
    if n == 1:
        return [debut]
    pas = (fin - debut) / (n - 1)
    return [debut + i * pas for i in range(n)]


print(linspace(0, 1, 5))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

(La bibliothèque NumPy, étudiée en P08, fournit `numpy.linspace` et des calculs vectorisés.)

### 3.2 Une table de valeurs

```python
def f(x):
    return x**2 - 2 * x - 3


xs = linspace(-3, 5, 9)
ys = [f(x) for x in xs]
for x, y in zip(xs, ys):
    print(f"{x:>5.1f} → {y:>6.2f}")
```

### 3.3 Tracer la courbe

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(xs, ys)
ax.axhline(0, color="black", linewidth=0.8)  # axe horizontal y = 0
ax.axvline(0, color="black", linewidth=0.8)  # axe vertical x = 0
ax.set_title("f(x) = x² − 2x − 3")
ax.grid(True)
plt.show()
```

### 3.4 Courbes classiques

```python
import math

xs = linspace(-2 * math.pi, 2 * math.pi, 200)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(xs, [math.sin(x) for x in xs], label="sin(x)")
ax.plot(xs, [math.cos(x) for x in xs], label="cos(x)")
ax.legend()
ax.grid(True)
```

| Fonction | Allure |
|---|---|
| `a*x + b` | droite |
| `x**2` | parabole |
| `math.exp(x)` | croissance explosive |
| `math.log(x)` | croissance lente (x > 0) |
| `1 / x` | hyperbole (attention en 0 !) |
| `math.sin(x)` | onde périodique |

### 3.5 Trouver les zéros (le solveur de la dichotomie)

Si f est continue et f(a), f(b) sont de signes opposés, il y a un zéro entre a et b. On coupe l'intervalle en deux
jusqu'à la précision voulue (on retrouve l'idée de la **dichotomie** de la leçon 8.4) :

```python
def zero(f, a, b, precision=1e-9):
    while b - a > precision:
        milieu = (a + b) / 2
        if f(a) * f(milieu) <= 0:
            b = milieu
        else:
            a = milieu
    return (a + b) / 2


print(zero(lambda x: x**2 - 2, 0, 2))  # 1.4142135... (racine de 2)
```

### 3.6 Extrémum et aire (aperçu de l'analyse)

```python
ys = [f(x) for x in xs]
y_min = min(ys)
x_min = xs[ys.index(y_min)]
```

**Aire sous la courbe** (méthode des trapèzes) :

```python
def integrale(f, a, b, n=1000):
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


print(integrale(lambda x: x**2, 0, 3))  # ≈ 9.0
```

**Pente (dérivée approchée)** : `(f(x + h) - f(x)) / h` pour h très petit.

### 3.7 Courbes paramétriques : un cercle

```python
angles = linspace(0, 2 * math.pi, 100)
x = [math.cos(t) for t in angles]
y = [math.sin(t) for t in angles]
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect("equal")  # cercle rond et non ovale
```

### 3.8 Éviter les valeurs interdites

`1/x` en 0, `log(x)` pour x ≤ 0, `sqrt(x)` pour x < 0 : filtre ou gère l'erreur.

```python
xs = [x for x in linspace(-3, 3, 61) if abs(x) > 1e-9]
```

### 3.9 Un exemple concret : coût et recette

Une boutique : recette R(q) = 1500·q, coût C(q) = 20000 + 700·q.

```python
qs = list(range(0, 61))
recette = [1500 * q for q in qs]
cout = [20000 + 700 * q for q in qs]
benefice = [r - c for r, c in zip(recette, cout)]
# seuil de rentabilité : premier q où benefice >= 0
seuil = next(q for q, b in zip(qs, benefice) if b >= 0)  # 25
```

Le graphique montre où les deux droites se croisent : le **point mort**.

## 4. ⚠️ Pièges courants

- **Trop peu de points** : une courbe lisse devient anguleuse (sin avec 5 points).
- **Division par zéro** ou domaine interdit : filtre les x.
- **Radians vs degrés** pour `sin`/`cos`.
- **Échelle déformée** : utilise `ax.set_aspect("equal")` pour les figures géométriques.
- **Zéro non encadré** : la dichotomie exige f(a) et f(b) de signes opposés.

## 5. À retenir

- Tracer f = choisir des x, calculer les y, relier les points.
- `linspace` maison (ou NumPy) pour des x réguliers.
- Dichotomie pour trouver un zéro ; trapèzes pour une aire.
- Tout graphique : titre, axes, grille, légende.

## 6. Exercices

Fichier : [`exercices/ex34_fonctions_mathematiques.py`](../exercices/ex34_fonctions_mathematiques.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex34_fonctions_mathematiques.py -v
```

## 7. Quiz

1. Combien de valeurs donne `linspace(0, 1, 5)` et quel est le pas ?
2. Pourquoi la dichotomie exige-t-elle deux signes opposés ?
3. Quelle fonction pour une courbe périodique ?
4. Comment obtenir un cercle « rond » sur un graphique ?

<details>
<summary>Réponses</summary>

1. 5 valeurs, avec un pas de 0,25.
2. Pour être sûr qu'un zéro existe entre les deux bornes (théorème des valeurs intermédiaires).
3. `math.sin` ou `math.cos`.
4. `ax.set_aspect("equal")`.

</details>
