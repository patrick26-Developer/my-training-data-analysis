# Leçon 9.1 — Dessiner avec `turtle`

⏱ 50 min · 🎯 Débutant · 📦 Prérequis : modules 3 et 5

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Une tortue, un crayon, et quelques lignes de code : tu vas dessiner des formes et des motifs qui s'affichent à l'écran.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Dessiner des formes avec la **tortue** de Python
- Utiliser des boucles et des fonctions pour créer des motifs
- Calculer les **coordonnées** d'un polygone (la géométrie derrière le dessin)

---

## 1. Le problème

Voir le résultat d'un programme **à l'écran** est motivant. La bibliothèque `turtle` te donne un crayon (la tortue)
que tu pilotes avec des ordres : avance, tourne, lève le crayon… Idéal pour comprendre les boucles et les angles.

> ℹ️ `turtle` ouvre une **fenêtre** : lance les exemples depuis ton terminal ou ton éditeur, pas depuis un
> notebook en ligne. Les exercices, eux, se testent **sans fenêtre** (on calcule les coordonnées).

## 2. Pas à pas

### 2.1 Premier dessin

```python
import turtle

t = turtle.Turtle()
t.forward(100)  # avance de 100 pixels
t.left(90)  # tourne de 90° à gauche
t.forward(100)
turtle.done()  # garde la fenêtre ouverte
```

Commandes de base :

| Commande | Effet |
|---|---|
| `forward(d)` / `backward(d)` | avance / recule |
| `left(a)` / `right(a)` | tourne de `a` degrés |
| `penup()` / `pendown()` | lève / baisse le crayon |
| `goto(x, y)` | va au point (x, y) |
| `color("red")`, `pensize(3)` | couleur, épaisseur |
| `begin_fill()` / `end_fill()` | remplit la forme |
| `circle(r)` | cercle de rayon r |
| `speed(0)` | vitesse maximale |
| `hideturtle()` | cache la tortue |

### 2.2 Un carré avec une boucle

```python
for _ in range(4):
    t.forward(100)
    t.left(90)
```

### 2.3 Tout polygone régulier

Pour un polygone à `n` côtés, la tortue tourne de **360 / n** degrés à chaque sommet.

```python
def polygone(t, n, cote):
    for _ in range(n):
        t.forward(cote)
        t.left(360 / n)


polygone(t, 6, 80)  # hexagone
```

### 2.4 Motifs : la rosace

```python
for _ in range(36):
    polygone(t, 4, 80)
    t.left(10)
```

### 2.5 Spirale

```python
longueur = 5
for _ in range(100):
    t.forward(longueur)
    t.left(91)
    longueur += 2
```

### 2.6 Déplacer sans dessiner, colorier

```python
t.penup()
t.goto(-100, 50)
t.pendown()
t.color("green")
t.begin_fill()
polygone(t, 3, 100)
t.end_fill()
```

### 2.7 Réagir à la souris et au clavier

```python
ecran = turtle.Screen()
ecran.onclick(lambda x, y: t.goto(x, y))  # va où l'on clique
ecran.listen()
```

### 2.8 La géométrie derrière le dessin

Dessiner un polygone, c'est calculer des **points**. Pour un polygone régulier à `n` sommets inscrit dans un cercle
de rayon `R` centré en (0, 0), le sommet `k` est en :

```
x = R × cos(2πk / n)        y = R × sin(2πk / n)
```

```python
import math


def sommets(n, rayon):
    return [
        (rayon * math.cos(2 * math.pi * k / n), rayon * math.sin(2 * math.pi * k / n))
        for k in range(n)
    ]
```

C'est exactement ce que font les logiciels de dessin et les jeux vidéo : ils calculent des points, puis les relient.
Cette version se **teste** facilement, contrairement à une fenêtre graphique : c'est ce que feront les exercices.

## 3. ⚠️ Pièges courants

- **Fenêtre qui se ferme tout de suite** : oublier `turtle.done()` à la fin.
- **Programme lent** : ajoute `t.speed(0)` ou utilise `turtle.tracer(0)` puis `turtle.update()`.
- **Nom de fichier `turtle.py`** : masque le vrai module (voir leçon 7.1).
- **Erreur `TclError: no display`** : on est sur un serveur sans écran ; utilise un ordinateur avec affichage.
- Angles en **degrés** pour `turtle` mais en **radians** pour `math` !

## 4. À retenir

- `forward`, `left`, `penup`, `goto`, `color`, `begin_fill`.
- Polygone à n côtés : tourner de `360 / n`.
- Une boucle + une fonction = un motif répété.
- Dessiner = calculer des points ; les sommets se calculent avec cos et sin.

## 5. Exercices

Fichier : [`exercices/ex32_turtle.py`](../exercices/ex32_turtle.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex32_turtle.py -v
```

Défi libre (sans test) : dessine ton drapeau, une maison, une fleur, ou une rosace colorée avec `turtle`.

## 6. Quiz

1. De combien de degrés tourne la tortue pour dessiner un pentagone régulier ?
2. Quelle commande déplace la tortue sans tracer ?
3. À quoi sert `turtle.done()` ?
4. Quelle unité d'angle utilise `turtle` ? et `math.cos` ?

<details>
<summary>Réponses</summary>

1. 72° (360 / 5).
2. `penup()` puis `goto(x, y)`.
3. À garder la fenêtre ouverte jusqu'à ce qu'on la ferme.
4. `turtle` : degrés ; `math.cos` : radians.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu as vu à quel point un dessin n'est qu'un calcul de points. Cela te servira dans les jeux et les graphiques.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 9.2 — Courbes et histogrammes avec `matplotlib`](l33_matplotlib.md).
<!-- /cadre:fin -->
