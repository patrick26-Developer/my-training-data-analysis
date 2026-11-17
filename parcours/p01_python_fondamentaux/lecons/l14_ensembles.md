# Leçon 4.4 — Les ensembles (`set`)

⏱ 40 min · 🎯 Débutant · 📦 Prérequis : leçon 4.3

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Doublons éliminés, produits en commun entre deux boutiques, tout cela en une seule opération : voici les ensembles.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Créer un ensemble et retirer les doublons d'une liste
- Faire union, intersection, différence
- Tester l'appartenance très rapidement

---

## 1. Le problème

Deux boutiques vendent des produits. Quels produits ont-elles **en commun** ? Lesquels n'existent que dans l'une ?
Combien de clients **différents** ont acheté cette semaine ? Un **ensemble** répond à ces questions : une collection
**sans doublons** et **sans ordre**, comme en mathématiques.

## 2. Pas à pas

### 2.1 Créer

```python
produits = {"Riz", "Sel", "Riz", "Sucre"}
print(produits)  # {'Sel', 'Riz', 'Sucre'}  (sans doublon, ordre quelconque)
vide = set()  # ⚠ {} crée un dictionnaire vide, pas un ensemble
a = set([1, 2, 2, 3])  # {1, 2, 3}
```

### 2.2 Ajouter, retirer, tester

```python
produits.add("Huile")
produits.discard("Sel")  # pas d'erreur si absent
produits.remove("Riz")  # KeyError si absent
print("Sucre" in produits)  # True  (très rapide, même pour des millions d'éléments)
print(len(produits))
```

### 2.3 Opérations mathématiques

```python
boutique_a = {"Riz", "Sel", "Sucre"}
boutique_b = {"Sel", "Huile", "Sucre"}

print(boutique_a | boutique_b)  # union         : tous les produits
print(boutique_a & boutique_b)  # intersection  : en commun
print(boutique_a - boutique_b)  # différence    : seulement dans A
print(boutique_a ^ boutique_b)  # différence symétrique : dans l'un ou l'autre, pas les deux
print({"Sel"} <= boutique_a)  # True : sous-ensemble
```

### 2.4 Supprimer les doublons d'une liste

```python
clients = ["Jean", "Marie", "Jean", "Paul", "Marie"]
uniques = set(clients)
print(len(uniques))  # 3
print(sorted(uniques))  # ['Jean', 'Marie', 'Paul']
```

⚠️ `set(...)` ne conserve **pas l'ordre**. Pour garder l'ordre : `list(dict.fromkeys(clients))`.

### 2.5 Éléments permis

Seuls les éléments **non modifiables** (nombres, textes, tuples) peuvent être dans un ensemble. Pas de listes
ni de dictionnaires dedans.

## 3. ⚠️ Pièges courants

**`{}` n'est pas un ensemble vide**

```python
type({})  # <class 'dict'>
type(set())  # <class 'set'>
```

**Compter sur l'ordre**

```python
{3, 1, 2}[0]
```
```
TypeError: 'set' object is not subscriptable
```

**Mettre une liste dans un ensemble**

```python
{[1, 2]}
```
```
TypeError: unhashable type: 'list'
```

## 4. À retenir

- `set` : sans doublons, sans ordre, appartenance rapide.
- `|` union, `&` intersection, `-` différence, `^` différence symétrique.
- `set()` pour un ensemble vide.
- `set(liste)` supprime les doublons (mais perd l'ordre).

## 5. Exercices

Fichier : [`exercices/ex14_ensembles.py`](../exercices/ex14_ensembles.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex14_ensembles.py -v
```

## 6. Quiz

1. Que vaut `len({1, 1, 2})` ?
2. Que calcule `a & b` ?
3. Comment créer un ensemble vide ?
4. Pourquoi ne peut-on pas écrire `mon_set[0]` ?

<details>
<summary>Réponses</summary>

1. `2`
2. L'intersection : les éléments présents dans `a` **et** `b`.
3. `set()`
4. Un ensemble n'a pas d'ordre, donc pas d'indices.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Les ensembles sont ajoutés à ta boîte à outils. Éliminer les doublons n'a jamais été aussi simple.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 4.5 — Les compréhensions](l15_comprehensions.md).
<!-- /cadre:fin -->
