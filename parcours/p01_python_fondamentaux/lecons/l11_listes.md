# Leçon 4.1 — Les listes

⏱ 60 min · 🎯 Débutant · 📦 Prérequis : module 3

## 🎯 Ce que tu sauras faire

- Créer une liste, lire et modifier ses éléments
- Ajouter, retirer, trier, chercher
- Parcourir une liste avec `for`
- Comprendre la différence entre **copier** et **partager** une liste

---

## 1. Le problème

Ton stock contient 50 produits. Créer 50 variables (`produit1`, `produit2`…) est impossible à gérer.
Une **liste** range plusieurs valeurs sous un seul nom, dans un ordre précis.

## 2. L'idée en images

Une liste est une **étagère à cases numérotées** :

```
prix = [ 500 , 1200 , 300 , 750 ]
indice:   0     1      2     3        (et -1 pour la dernière)
```

## 3. Pas à pas

### 3.1 Créer et lire

```python
produits = ["Manioc", "Plantain", "Riz"]
print(produits[0])  # Manioc
print(produits[-1])  # Riz
print(produits[0:2])  # ['Manioc', 'Plantain']  (tranches, comme pour le texte)
print(len(produits))  # 3
vide = []
```

Une liste peut mélanger les types : `["Manioc", 500, True]`.

### 3.2 Modifier

Contrairement au texte, une liste est **modifiable** (*mutable*) :

```python
produits[1] = "Banane"  # remplace
produits.append("Sucre")  # ajoute à la fin
produits.insert(0, "Sel")  # insère à l'indice 0
produits.remove("Riz")  # retire la première occurrence
dernier = produits.pop()  # retire et renvoie le dernier
del produits[0]  # supprime l'indice 0
```

### 3.3 Chercher et compter

```python
nombres = [4, 8, 15, 8, 23]
print(8 in nombres)  # True
print(nombres.index(15))  # 2   (position, erreur si absent)
print(nombres.count(8))  # 2
print(min(nombres), max(nombres), sum(nombres))  # 4 23 58
```

### 3.4 Trier et inverser

```python
nombres.sort()  # modifie la liste : [4, 8, 8, 15, 23]
nombres.sort(reverse=True)  # décroissant
nombres.reverse()  # inverse l'ordre
trie = sorted(nombres)  # NOUVELLE liste triée, l'originale est inchangée
```

### 3.5 Parcourir

```python
for produit in produits:
    print(produit)

for i, produit in enumerate(produits, start=1):
    print(f"{i}. {produit}")
```

### 3.6 Assembler et découper

```python
a = [1, 2]
b = [3]
print(a + b)  # [1, 2, 3]
print(a * 2)  # [1, 2, 1, 2]
print("Mbote na yo".split())  # ['Mbote', 'na', 'yo']
print(", ".join(["a", "b"]))  # a, b
```

### 3.7 Listes de listes (tableaux à 2 dimensions)

```python
grille = [
    [1, 2, 3],
    [4, 5, 6],
]
print(grille[1][2])  # 6  (ligne 1, colonne 2)
```

## 4. ⚠️ Pièges courants

**Copier une liste ≠ l'affecter**

```python
a = [1, 2, 3]
b = a  # b est le MÊME objet que a
b.append(4)
print(a)  # [1, 2, 3, 4]  !!
c = a.copy()  # vraie copie (ou a[:] ou list(a))
```

**`sort()` renvoie `None`**

```python
x = [3, 1, 2]
x = x.sort()  # ❌ x vaut maintenant None
```

**Modifier une liste pendant qu'on la parcourt** : des éléments sont sautés. Construis plutôt une nouvelle liste.

**Indice hors limites**

```python
[1, 2, 3][5]
```
```
IndexError: list index out of range
```

**Liste de listes mal créée**

```python
grille = [[0] * 3] * 3  # ❌ trois fois LA MÊME ligne
grille = [[0] * 3 for _ in range(3)]  # ✅ (voir leçon 4.5)
```

## 5. À retenir

- `[a, b, c]` ; indices à partir de 0 ; tranches comme pour le texte.
- Mutable : `append`, `insert`, `remove`, `pop`, `sort`.
- `sorted(x)` crée une nouvelle liste, `x.sort()` modifie en place et renvoie `None`.
- `b = a` partage ; `b = a.copy()` copie.

## 6. Exercices

Fichier : [`exercices/ex11_listes.py`](../exercices/ex11_listes.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex11_listes.py -v
```

## 7. Quiz

1. Que vaut `[10, 20, 30][-2]` ?
2. Quelle différence entre `sorted(x)` et `x.sort()` ?
3. Que contient `a` après `a = [1]; b = a; b.append(2)` ?
4. Comment copier une liste ?

<details>
<summary>Réponses</summary>

1. `20`
2. `sorted` renvoie une nouvelle liste ; `sort` modifie la liste et renvoie `None`.
3. `[1, 2]`, car `b` et `a` désignent la même liste.
4. `a.copy()`, `a[:]` ou `list(a)`.

</details>
