# Leçon 8.3 — Tableaux à deux dimensions et matrices

⏱ 55 min · 🎯 Intermédiaire · 📦 Prérequis : leçons 4.1, 4.5 et 8.1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Une feuille de calcul, un damier, une image : tout est un tableau. Tu vas apprendre à les manipuler.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Représenter un **tableau** (lignes × colonnes) avec une liste de listes
- Parcourir, lire, modifier, transposer un tableau
- Faire des opérations de matrices : somme, produit, déterminant 2×2
- Comprendre pourquoi les bibliothèques comme **NumPy** (parcours P08) existent

---

## 1. Le problème

Une feuille de calcul de ventes : une ligne par produit, une colonne par mois.
Un damier, une grille de jeu, une image (lignes de pixels), un système d'équations : **tout cela est un
tableau à deux dimensions**.

## 2. L'idée en images

```
            mois 0  mois 1  mois 2
produit 0 [   120,    150,    130  ]
produit 1 [    80,     95,    110  ]
produit 2 [   200,    180,    210  ]

ventes[ligne][colonne]  →  ventes[1][2] = 110
```

## 3. Pas à pas

### 3.1 Créer

```python
ventes = [
    [120, 150, 130],
    [80, 95, 110],
    [200, 180, 210],
]
nb_lignes = len(ventes)  # 3
nb_colonnes = len(ventes[0])  # 3
```

Tableau de zéros — ⚠️ **jamais** `[[0] * 3] * 3` (lignes partagées) :

```python
zeros = [[0] * 3 for _ in range(3)]
```

### 3.2 Lire et modifier

```python
print(ventes[1][2])  # 110
ventes[0][0] = 125
print(ventes[2])  # une ligne entière
print([ligne[1] for ligne in ventes])  # une colonne entière : [150, 95, 180]
```

### 3.3 Parcourir

```python
for i, ligne in enumerate(ventes):
    for j, valeur in enumerate(ligne):
        print(f"({i},{j}) = {valeur}")
```

### 3.4 Totaux par ligne, par colonne, global

```python
total_par_produit = [sum(ligne) for ligne in ventes]  # [405, 285, 590]
total_par_mois = [sum(colonne) for colonne in zip(*ventes)]  # [405, 425, 450]
total = sum(sum(ligne) for ligne in ventes)  # 1280
```

`zip(*ventes)` **transpose** : il regroupe les premières valeurs de chaque ligne, puis les secondes, etc.

### 3.5 Afficher proprement

```python
for ligne in ventes:
    print(" ".join(f"{v:>5}" for v in ligne))
```

### 3.6 Opérations sur les matrices

**Somme** de deux matrices de même taille :

```python
def addition(a, b):
    return [[x + y for x, y in zip(la, lb)] for la, lb in zip(a, b)]
```

**Multiplication par un nombre** : `[[k * x for x in ligne] for ligne in m]`

**Produit matriciel** : C[i][j] = Σ A[i][k] × B[k][j]

```python
def produit(a, b):
    colonnes_b = list(zip(*b))
    return [[sum(x * y for x, y in zip(ligne, colonne)) for colonne in colonnes_b] for ligne in a]


A = [[1, 2], [3, 4]]
B = [[0, 1], [1, 0]]
print(produit(A, B))  # [[2, 1], [4, 3]]
```

**Déterminant 2×2** : ad − bc

```python
def determinant_2x2(m):
    (a, b), (c, d) = m
    return a * d - b * c
```

**Matrice identité** : 1 sur la diagonale, 0 ailleurs.

```python
def identite(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
```

### 3.7 Un jeu : la grille de morpion

```python
grille = [[" "] * 3 for _ in range(3)]
grille[1][1] = "X"
for ligne in grille:
    print("|".join(ligne))
    print("-" * 5)
```

### 3.8 Et NumPy ?

Pour de grands tableaux (images, données scientifiques), les listes sont lentes et lourdes. **NumPy** offre des
tableaux rapides avec des opérations « vectorisées » (`a + b`, `a @ b`) : tu l'étudieras dans le parcours
**P08 — Data Analysis**. Comprendre les listes de listes t'aidera à saisir ce qu'il fait « sous le capot ».

## 4. ⚠️ Pièges courants

**Lignes partagées** : `[[0] * 3] * 3` crée 3 fois la **même** ligne.

**Tableau irrégulier** : `[[1, 2], [3]]` — les colonnes n'ont pas la même taille : `IndexError` en parcourant.

**Confondre ligne et colonne** : `m[ligne][colonne]` ; mets des noms explicites (`i`, `j`).

**Copier un tableau avec `.copy()`** : copie les lignes **par référence**. Pour une vraie copie :
`[ligne[:] for ligne in m]` ou `copy.deepcopy(m)`.

## 5. À retenir

- Tableau 2D = liste de listes : `m[ligne][colonne]`.
- Colonne : `[l[j] for l in m]` ; transposition : `list(zip(*m))`.
- Crée une grille avec une compréhension, pas avec `*`.
- Copie profonde : `copy.deepcopy`.

## 6. Exercices

Fichier : [`exercices/ex30_tableaux_2d.py`](../exercices/ex30_tableaux_2d.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex30_tableaux_2d.py -v
```

## 7. Quiz

1. Comment lire la 2ᵉ colonne d'un tableau `m` ?
2. Pourquoi `[[0] * 3] * 3` est-il dangereux ?
3. Que fait `zip(*m)` ?
4. Combien vaut le déterminant de `[[1, 2], [3, 4]]` ?

<details>
<summary>Réponses</summary>

1. `[ligne[1] for ligne in m]`
2. Les trois lignes sont le même objet.
3. Il transpose le tableau (les lignes deviennent des colonnes).
4. `1 × 4 − 2 × 3 = −2`.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu sais manipuler des matrices et des grilles. Tu viens de poser les bases de NumPy et de la data science.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 8.4 — Algorithmes classiques](l31_algorithmes_classiques.md).
<!-- /cadre:fin -->
