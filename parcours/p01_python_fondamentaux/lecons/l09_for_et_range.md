# Leçon 3.2 — La boucle `for` et `range`

⏱ 50 min · 🎯 Débutant · 📦 Prérequis : leçon 3.1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Tables de multiplication, comptes à rebours, dessins en étoiles : avec `for`, des tâches longues deviennent de simples jeux.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Parcourir une suite de valeurs avec `for`
- Générer des nombres avec `range(début, fin, pas)`
- Parcourir un texte lettre par lettre
- Choisir entre `for` et `while`

---

## 1. Le problème

« Affiche la table de multiplication de 7. » Tu sais **à l'avance** combien de fois répéter : 10 fois.
Quand on connaît le nombre de tours (ou la collection à parcourir), `for` est plus simple et plus sûr que `while` :
pas de compteur à initialiser ni à incrémenter, donc pas de boucle infinie.

## 2. L'idée en images

`for` est un **convoyeur** : il prend les éléments un par un, et pour chacun exécute le bloc.

```
[ 1 ] [ 2 ] [ 3 ]  ──►  pour chaque élément : print(élément)
```

## 3. Pas à pas

### 3.1 `for` sur un texte

```python
for lettre in "Mbote":
    print(lettre)
```
```
M
b
o
t
e
```

`lettre` est une variable qui prend, à chaque tour, la valeur suivante.

### 3.2 `range`

`range(n)` produit les entiers de **0 à n-1**.

```python
for i in range(5):
    print(i)  # 0 1 2 3 4
```

| Appel | Valeurs |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(10, 0, -1)` | 10, 9, 8, …, 1 |

La borne de fin est toujours **exclue** (comme pour les tranches de texte).

### 3.3 Table de multiplication

```python
n = 7
for i in range(1, 11):
    print(f"{n} x {i:>2} = {n * i:>3}")
```
```
7 x  1 =   7
7 x  2 =  14
...
7 x 10 =  70
```

### 3.4 Accumuler dans un `for`

```python
total = 0
for i in range(1, 101):
    total += i
print(total)  # 5050
```

### 3.5 Compter avec une condition

```python
phrase = "Le manioc est bon"
voyelles = 0
for lettre in phrase.lower():
    if lettre in "aeiouy":
        voyelles += 1
print(voyelles)  # 6
```

### 3.6 Indices : `range(len(...))` et `enumerate`

```python
mot = "Congo"
for i in range(len(mot)):
    print(i, mot[i])

for i, lettre in enumerate(mot):  # plus élégant
    print(i, lettre)
```

### 3.7 `for` ou `while` ?

| Situation | Choix |
|---|---|
| Nombre de tours connu, ou parcours d'une collection | `for` |
| On répète jusqu'à ce qu'un événement arrive (saisie valide, fin de fichier) | `while` |

### 3.8 Aperçu : construire un résultat avec une liste

Pour fabriquer plusieurs morceaux de texte puis les assembler, on utilise une **liste** (étudiée en détail
au module 4). Retiens seulement ces trois gestes :

```python
morceaux = []  # une liste vide
morceaux.append("a")  # ajouter un élément à la fin
morceaux.append("b")
print(" - ".join(morceaux))  # a - b   (colle les éléments avec un séparateur)
```

Les solutions des exercices de cette leçon s'en servent.

## 4. ⚠️ Pièges courants

**Oublier que `range` exclut la fin**

```python
for i in range(1, 10):   # s'arrête à 9, pas 10 !
```

**Modifier la variable de boucle**

```python
for i in range(3):
    i = i * 10  # n'influence pas le tour suivant
```

**`range` avec un décimal**

```python
range(0.5, 3)
```
```
TypeError: 'float' object cannot be interpreted as an integer
```

## 5. À retenir

- `for x in collection:` parcourt élément par élément.
- `range(début, fin, pas)` : début inclus, fin **exclue**.
- `enumerate` donne l'indice et la valeur.
- Nombre de tours connu → `for` ; répétition conditionnelle → `while`.

## 6. Exercices

Fichier : [`exercices/ex09_for_et_range.py`](../exercices/ex09_for_et_range.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex09_for_et_range.py -v
```

## 7. Quiz

1. Quelles valeurs produit `range(2, 8, 3)` ?
2. Combien de fois s'exécute `for i in range(0)` ?
3. Comment parcourir un compte à rebours de 5 à 1 ?
4. Quand préférer `while` à `for` ?

<details>
<summary>Réponses</summary>

1. 2 puis 5.
2. Aucune fois.
3. `for i in range(5, 0, -1):`
4. Quand on ne connaît pas le nombre de tours à l'avance et qu'on répète jusqu'à un événement.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

`for` et `range` n'ont plus de secret pour toi. Tu peux désormais parcourir n'importe quelle suite de valeurs.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 3.3 — `break`, `continue` et boucles imbriquées](l10_break_continue_imbriquees.md).
<!-- /cadre:fin -->
