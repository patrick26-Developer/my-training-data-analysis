# Leçon 5.4 — Les fonctions sont des valeurs

⏱ 55 min · 🎯 Intermédiaire · 📦 Prérequis : leçons 5.1 à 5.3

## 🎯 Ce que tu sauras faire

- Passer une fonction en argument d'une autre fonction
- Écrire une fonction anonyme avec `lambda`
- Utiliser `sorted(..., key=...)`, `map`, `filter`
- Reconnaître le principe des fonctions de rappel (*callbacks*)

---

## 1. Le problème

Tu veux trier des produits tantôt par prix, tantôt par nom, tantôt par stock. Plutôt que d'écrire trois fonctions de
tri, tu écris **un** tri et tu lui dis **par quelle règle** comparer. Pour cela, il faut pouvoir **passer une règle
(une fonction) en argument**.

## 2. L'idée en images

En Python, une fonction est un **objet comme un autre** : on peut la ranger dans une variable, la mettre dans
une liste, la passer à une autre fonction.

```
   trier( produits , règle = par_prix )
                         ▲
                   une fonction !
```

## 3. Pas à pas

### 3.1 Une fonction dans une variable

```python
def doubler(n):
    return n * 2


f = doubler  # pas de parenthèses : on ne l'appelle pas, on la désigne
print(f(5))  # 10
```

### 3.2 Passer une fonction en argument

```python
def appliquer(fonction, valeurs):
    return [fonction(v) for v in valeurs]


print(appliquer(doubler, [1, 2, 3]))  # [2, 4, 6]
print(appliquer(str.upper, ["a", "b"]))  # ['A', 'B']
```

### 3.3 `lambda` : une mini-fonction sans nom

```python
carre = lambda x: x * x  # équivalent à def carre(x): return x * x
print(carre(4))  # 16
print(appliquer(lambda x: x + 1, [1, 2]))  # [2, 3]
```

Une `lambda` ne contient qu'**une expression** (pas d'instructions). Pour toute logique plus longue, utilise `def`.

### 3.4 `sorted` et `key`

```python
produits = [("Riz", 800), ("Sel", 100), ("Manioc", 500)]

print(sorted(produits, key=lambda p: p[1]))  # par prix croissant
print(sorted(produits, key=lambda p: p[0]))  # par nom
print(sorted(produits, key=lambda p: p[1], reverse=True))  # par prix décroissant
print(max(produits, key=lambda p: p[1]))  # ('Riz', 800)
```

Trier une liste de dictionnaires :

```python
eleves = [{"nom": "Jean", "note": 12}, {"nom": "Grâce", "note": 17}]
meilleurs = sorted(eleves, key=lambda e: e["note"], reverse=True)
```

### 3.5 `map` et `filter`

```python
nombres = [1, 2, 3, 4, 5, 6]
print(list(map(lambda n: n * n, nombres)))  # [1, 4, 9, 16, 25, 36]
print(list(filter(lambda n: n % 2 == 0, nombres)))  # [2, 4, 6]
```

Les compréhensions (leçon 4.5) sont souvent plus lisibles :
`[n * n for n in nombres]` et `[n for n in nombres if n % 2 == 0]`.

### 3.6 Retourner une fonction (fonction fabrique)

```python
def multiplicateur(facteur):
    def multiplier(x):
        return x * facteur  # « se souvient » de facteur

    return multiplier


triple = multiplicateur(3)
print(triple(5))  # 15
```

C'est une **fermeture** (*closure*) : la fonction intérieure garde l'accès aux variables de la fonction qui l'a créée.

### 3.7 Un dictionnaire de fonctions : une calculatrice

```python
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
}
print(operations["*"](6, 7))  # 42
```

C'est une alternative élégante à une longue chaîne de `if/elif` ou à un `match`.

### 3.8 Fonctions de rappel (*callbacks*)

Tu donnes une fonction à une autre pour qu'elle l'appelle **plus tard**, à un moment précis (clic sur un bouton
dans une application graphique, fin d'un téléchargement…). Tu rencontreras beaucoup ce motif dans le parcours P04.

## 4. ⚠️ Pièges courants

**Appeler au lieu de passer**

```python
sorted(produits, key=prix())  # ❌ appelle prix() tout de suite
sorted(produits, key=prix)  # ✅ passe la fonction
```

**`lambda` trop complexe** : si tu hésites, écris une vraie fonction avec un nom clair.

**`map` / `filter` paresseux**

```python
map(len, ["a", "bb"])  # <map object ...> : il faut list(...) pour voir le résultat
```

## 5. À retenir

- Une fonction est une valeur : on peut la passer, la ranger, la retourner.
- `lambda x: expression` pour une règle courte.
- `sorted(coll, key=...)`, `max(coll, key=...)` : la clé indique **quoi comparer**.
- `map` / `filter` existent, mais les compréhensions sont souvent plus claires.

## 6. Exercices

Fichier : [`exercices/ex19_fonctions_comme_valeurs.py`](../exercices/ex19_fonctions_comme_valeurs.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex19_fonctions_comme_valeurs.py -v
```

## 7. Mini-projet du module 5 — La caisse en fonctions

Reprends la **caisse du marché** (module 1) et le **stock** (module 4) : réorganise le code en petites fonctions
(`lire_commande`, `calculer_total`, `formater_recu`, …) et ajoute un **journal des ventes** sous forme de liste
de dictionnaires. Solution : [`../projets/m5_caisse_en_fonctions.py`](../projets/m5_caisse_en_fonctions.py).

## 8. Quiz

1. Quelle différence entre `f` et `f()` ?
2. Que fait `sorted(L, key=len)` ?
3. Écris une `lambda` qui renvoie le double de `x`.
4. Qu'est-ce qu'une fermeture ?

<details>
<summary>Réponses</summary>

1. `f` désigne la fonction ; `f()` l'exécute.
2. Il trie les éléments de `L` selon leur longueur.
3. `lambda x: x * 2`
4. Une fonction intérieure qui garde l'accès aux variables de la fonction qui l'a créée.

</details>
