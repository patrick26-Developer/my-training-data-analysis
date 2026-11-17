# Leçon 4.2 — Les tuples

⏱ 40 min · 🎯 Débutant · 📦 Prérequis : leçon 4.1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Un petit paquet de valeurs qui ne change jamais : les tuples vont te permettre de renvoyer plusieurs résultats d'un coup.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Créer et lire un tuple
- Expliquer la différence entre tuple et liste
- Utiliser le **déballage** (*unpacking*) pour échanger ou extraire des valeurs
- Retourner plusieurs valeurs depuis une fonction

---

## 1. Le problème

Un point sur une carte a une latitude et une longitude. Une date a un jour, un mois, une année.
Ces valeurs vont **ensemble** et ne doivent **pas changer** : on veut un « paquet figé ». C'est un **tuple**.

## 2. Pas à pas

### 2.1 Créer un tuple

```python
point = (4.26, 15.28)  # Brazzaville : latitude, longitude (approx.)
date = (16, 11, 2026)
un_seul = (5,)  # attention à la virgule !
vide = ()
```

Lecture identique à une liste : `point[0]`, `point[-1]`, `point[0:1]`, `len(point)`, `in`, `for`.

### 2.2 Immuable

```python
point[0] = 5
```
```
TypeError: 'tuple' object does not support item assignment
```

Pour « modifier », on crée un **nouveau** tuple : `point = (5.0,) + point[1:]`.

### 2.3 Déballage

```python
latitude, longitude = point
print(latitude)  # 4.26

jour, mois, annee = date
```

Échanger deux variables **sans variable temporaire** :

```python
a, b = 1, 2
a, b = b, a  # a vaut 2, b vaut 1
```

Avec `*` pour « le reste » :

```python
premier, *milieu, dernier = [1, 2, 3, 4, 5]
print(premier, milieu, dernier)  # 1 [2, 3, 4] 5
```

### 2.4 Retourner plusieurs valeurs

```python
def min_max(nombres):
    return min(nombres), max(nombres)  # un tuple (parenthèses facultatives)


petit, grand = min_max([4, 9, 2])
```

### 2.5 Parcourir avec déballage

```python
couples = [("Manioc", 500), ("Riz", 800)]
for nom, prix in couples:
    print(f"{nom} : {prix} FCFA")
```

Et `zip` pour parcourir deux listes en parallèle :

```python
noms = ["Manioc", "Riz"]
prix = [500, 800]
for nom, p in zip(noms, prix):
    print(nom, p)
```

### 2.6 Tuple ou liste ?

| Tuple | Liste |
|---|---|
| Valeurs figées, qui forment un tout (coordonnées, date) | Collection qui évolue (panier, stock) |
| Peut servir de clé de dictionnaire (leçon 4.3) | Ne peut pas |
| Un peu plus léger | Plus de méthodes (`append`…) |

## 3. ⚠️ Pièges courants

**Oublier la virgule** : `(5)` est le nombre 5 ; `(5,)` est un tuple.

**Mauvais nombre de variables au déballage**

```python
a, b = (1, 2, 3)
```
```
ValueError: too many values to unpack (expected 2)
```

**Un tuple contenant une liste** : la liste interne reste modifiable. L'immutabilité est superficielle.

## 4. À retenir

- Tuple = paquet **immuable** : `(a, b, c)`.
- Déballage : `x, y = point` ; échange : `a, b = b, a`.
- Une fonction qui « retourne plusieurs valeurs » retourne un tuple.
- `zip(a, b)` parcourt deux séquences en parallèle.

## 5. Exercices

Fichier : [`exercices/ex12_tuples.py`](../exercices/ex12_tuples.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex12_tuples.py -v
```

## 6. Quiz

1. Comment écrire un tuple à un seul élément ?
2. Que fait `a, b = b, a` ?
3. Peut-on faire `t[0] = 1` sur un tuple ?
4. Que vaut `premier, *reste = [1, 2, 3]` pour `reste` ?

<details>
<summary>Réponses</summary>

1. `(5,)`, avec la virgule.
2. Échange les valeurs de `a` et `b`.
3. Non : `TypeError`, car un tuple est immuable.
4. `[2, 3]`

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu maîtrises les tuples et le déballage. Échanger deux valeurs en une ligne, c'est la classe !

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 4.3 — Les dictionnaires](l13_dictionnaires.md).
<!-- /cadre:fin -->
