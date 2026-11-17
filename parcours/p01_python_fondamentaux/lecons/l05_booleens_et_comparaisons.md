# Leçon 2.1 — Booléens et comparaisons

⏱ 45 min · 🎯 Débutant · 📦 Prérequis : module 1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Oui ou non, vrai ou faux : tu vas apprendre à poser à ton programme les questions qui lui permettront de décider.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Comprendre le type `bool` (`True` / `False`)
- Comparer des valeurs avec `==  !=  <  >  <=  >=`
- Combiner des conditions avec `and`, `or`, `not`
- Tester l'appartenance avec `in`

---

## 1. Le problème

Avant de décider quoi que ce soit, un programme doit pouvoir **poser une question dont la réponse est oui ou non** :
« Le client a-t-il 18 ans ou plus ? » « Le stock est-il vide ? » « Le mot de passe est-il correct ? »
En Python, une telle question produit un **booléen** : `True` (oui) ou `False` (non).

## 2. L'idée en images

Un booléen est un **interrupteur** : allumé (`True`) ou éteint (`False`).

```
age >= 18   →   True  ou  False
```

## 3. Pas à pas

### 3.1 Les opérateurs de comparaison

```python
age = 20
print(age == 20)  # True    égal à
print(age != 20)  # False   différent de
print(age > 18)  # True    strictement supérieur
print(age >= 20)  # True    supérieur ou égal
print(age < 18)  # False
print(age <= 20)  # True
```

⚠️ **`=` range une valeur, `==` compare.** Confondre les deux est l'erreur n°1 des débutants.

Les textes se comparent aussi (en distinguant les majuscules) :

```python
print("manioc" == "manioc")  # True
print("Manioc" == "manioc")  # False
print("Manioc".lower() == "manioc")  # True
```

On peut enchaîner : `0 <= note <= 20` (la note est entre 0 et 20).

### 3.2 Combiner : `and`, `or`, `not`

| Opérateur | Sens | Exemple | Résultat |
|---|---|---|---|
| `and` | les **deux** conditions vraies | `age >= 18 and age < 65` | vrai si adulte non retraité |
| `or` | **au moins une** vraie | `jour == "sam" or jour == "dim"` | vrai le week-end |
| `not` | inverse | `not True` | `False` |

Table de vérité (à connaître) :

| `A` | `B` | `A and B` | `A or B` |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

```python
age = 30
a_carte = True
print(age >= 18 and a_carte)  # True
print(age < 18 or not a_carte)  # False
```

Priorité : `not`, puis `and`, puis `or`. En cas de doute, **mets des parenthèses**.

### 3.3 Appartenance : `in`

```python
print("a" in "Manioc")  # False
print("o" in "Manioc")  # True
print(5 in [1, 5, 9])  # True  (listes : module 4)
print("sam" in ("sam", "dim"))  # True
```

### 3.4 Valeurs « vraies » et « fausses »

Python considère comme **faux** : `False`, `0`, `0.0`, `""` (texte vide), `None`, et les collections vides.
Tout le reste est **vrai**.

```python
print(bool(0))  # False
print(bool(""))  # False
print(bool("Mbote"))  # True
print(bool(-3))  # True
```

C'est pratique : `if nom:` signifie « si nom n'est pas vide ».

## 4. ⚠️ Pièges courants

**`=` au lieu de `==`**

```python
if age = 18:
```
```
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

**Comparer des types différents**

```python
print("5" == 5)  # False  (texte ≠ nombre)
print("5" < 10)
```
```
TypeError: '<' not supported between instances of 'str' and 'int'
```
Convertis avant : `int("5") < 10`.

**Comparer des décimaux avec `==`**

```python
print(0.1 + 0.2 == 0.3)  # False !
```
Utilise `math.isclose(0.1 + 0.2, 0.3)` ou arrondis avec `round`.

## 5. À retenir

- Une comparaison donne un `bool`.
- `==` compare, `=` range.
- `and` : les deux ; `or` : au moins un ; `not` : inverse.
- `in` teste l'appartenance.
- `0`, `""`, `None`, collections vides sont « faux ».

## 6. Exercices

Fichier : [`exercices/ex05_booleens_et_comparaisons.py`](../exercices/ex05_booleens_et_comparaisons.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex05_booleens_et_comparaisons.py -v
```

## 7. Quiz

1. Que vaut `10 > 3 and 2 > 5` ?
2. Que vaut `not (4 == 4)` ?
3. Que vaut `bool("")` ?
4. Quelle différence entre `=` et `==` ?
5. Écris la condition « `note` est entre 10 et 20 inclus ».

<details>
<summary>Réponses</summary>

1. `False`
2. `False`
3. `False`
4. `=` range une valeur dans une variable ; `==` compare deux valeurs et renvoie un booléen.
5. `10 <= note <= 20`

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu sais maintenant poser des questions à tes données. Dans la leçon suivante, ton programme va enfin faire des choix.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 2.2 — `if`, `elif`, `else` : choisir quoi faire](l06_if_elif_else.md).
<!-- /cadre:fin -->
