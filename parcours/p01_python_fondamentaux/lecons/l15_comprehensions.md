# Leçon 4.5 — Les compréhensions

⏱ 50 min · 🎯 Débutant+ · 📦 Prérequis : leçons 4.1 à 4.4

## 🎯 Ce que tu sauras faire

- Construire une liste, un ensemble ou un dictionnaire **en une ligne**
- Filtrer et transformer des données
- Savoir quand une boucle classique reste plus lisible

---

## 1. Le problème

Tu as une liste de prix et tu veux ces mêmes prix avec 18 % de TVA, seulement pour ceux supérieurs à 500.
Avec une boucle :

```python
resultat = []
for p in prix:
    if p > 500:
        resultat.append(p * 1.18)
```

Quatre lignes pour une idée simple. Une **compréhension** la dit en une ligne, comme en mathématiques :
« l'ensemble des p × 1,18 pour p dans prix, tel que p > 500 ».

## 2. L'idée en images

```
[ expression   for élément in collection   if condition ]
   ▲              ▲                           ▲
 ce qu'on met    d'où on prend              filtre (facultatif)
```

## 3. Pas à pas

### 3.1 Compréhension de liste

```python
carres = [n * n for n in range(1, 6)]
print(carres)  # [1, 4, 9, 16, 25]

pairs = [n for n in range(10) if n % 2 == 0]
print(pairs)  # [0, 2, 4, 6, 8]

prix = [300, 750, 1200]
avec_tva = [round(p * 1.18) for p in prix if p > 500]
print(avec_tva)  # [885, 1416]

majuscules = [mot.upper() for mot in ["riz", "sel"]]
```

### 3.2 Avec `if / else` (transformation conditionnelle)

Le `if/else` se place **avant** le `for` :

```python
etiquettes = ["pair" if n % 2 == 0 else "impair" for n in range(4)]
# ['pair', 'impair', 'pair', 'impair']
```

### 3.3 Compréhension d'ensemble et de dictionnaire

```python
lettres = {c for c in "banane"}  # {'b', 'a', 'n', 'e'}
carres = {n: n * n for n in range(1, 4)}  # {1: 1, 2: 4, 3: 9}
longueurs = {mot: len(mot) for mot in ["riz", "sucre"]}
```

### 3.4 Deux boucles imbriquées

```python
paires = [(a, b) for a in range(1, 3) for b in range(1, 3)]
# [(1, 1), (1, 2), (2, 1), (2, 2)]

grille = [[0] * 3 for _ in range(3)]  # grille 3x3 correcte (lignes indépendantes)
aplatie = [x for ligne in [[1, 2], [3]] for x in ligne]  # [1, 2, 3]
```

### 3.5 Fonctions utiles avec les compréhensions

```python
notes = [12, 15, 9, 18]
print(sum(n for n in notes if n >= 10))  # 45  (sans crochets : expression génératrice)
print(any(n >= 18 for n in notes))  # True  (au moins un)
print(all(n >= 10 for n in notes))  # False (tous ?)
```

### 3.6 Quand ne PAS les utiliser

Si l'expression devient longue, imbriquée ou avec des effets de bord (`print`, modification), préfère une boucle
claire. **La lisibilité passe avant la concision.**

```python
# ❌ illisible
[x for ligne in m for x in ligne if x % 2 == 0 and x > 10 and x not in vus]
```

## 4. ⚠️ Pièges courants

**Confondre l'ordre `if` / `if-else`**

```python
[x for x in data if x > 0]  # filtre : peut RACCOURCIR la liste
[x if x > 0 else 0 for x in data]  # transforme : garde la MÊME longueur
```

**Utiliser une compréhension pour un effet de bord**

```python
[print(x) for x in data]  # ❌ crée une liste inutile ; utilise un for
```

**Oublier que la variable reste locale** : `x` n'existe pas après la compréhension.

## 5. À retenir

- `[expr for x in coll if cond]` ; `{...}` pour un ensemble ; `{k: v for ...}` pour un dictionnaire.
- Le `if` après le `for` filtre ; le `if/else` avant le `for` transforme.
- `sum`, `any`, `all`, `min`, `max` acceptent directement une expression génératrice.
- Lisibilité d'abord.

## 6. Exercices

Fichier : [`exercices/ex15_comprehensions.py`](../exercices/ex15_comprehensions.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex15_comprehensions.py -v
```

## 7. Mini-projet du module 4 — Gestionnaire de stock

Écris un programme console avec menu (`match`) qui gère un stock sous forme de **liste de dictionnaires**
(`nom`, `prix`, `quantite`) : ajouter, vendre, lister, afficher la valeur totale, rechercher par nom.
La solution de référence est dans [`../projets/m4_gestionnaire_de_stock.py`](../projets/m4_gestionnaire_de_stock.py).

## 8. Quiz

1. Que donne `[n * 2 for n in range(3)]` ?
2. Où place-t-on un `if` de **filtrage** ? et un `if/else` de **transformation** ?
3. Comment créer la liste des longueurs des mots d'une liste `mots` ?
4. Pourquoi `[[0] * 3] * 3` est-il dangereux ?

<details>
<summary>Réponses</summary>

1. `[0, 2, 4]`
2. Le filtrage après le `for` ; la transformation avant le `for`.
3. `[len(m) for m in mots]`
4. Les trois lignes sont le même objet : modifier l'une modifie les autres.

</details>
