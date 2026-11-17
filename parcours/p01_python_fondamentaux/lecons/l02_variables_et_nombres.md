# Leçon 1.2 — Variables et nombres

⏱ 60 min · 🎯 Débutant · 📦 Prérequis : leçon 1.1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — À la fin de cette leçon, ton ordinateur calculera une facture à ta place — sans jamais se tromper dans les additions de Mama Nzoni.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Stocker une information dans une **variable** et la réutiliser
- Distinguer `int`, `float`, `str` et `bool`
- Faire des calculs avec `+ - * / // % **`
- Arrondir un résultat et éviter les pièges du calcul sur les nombres décimaux

---

## 1. Le problème

Au marché, tu vends 3 sacs de manioc à 2 500 FCFA. Demain le prix passe à 2 800 FCFA.
Si le prix est écrit à dix endroits de ton programme, tu dois le changer dix fois. Avec une **variable**,
tu le changes **une seule fois**.

## 2. L'idée en images

Une variable est une **étiquette collée sur une boîte** :

```
   ┌──────────┐
   │   2500   │  ← la valeur (dans la boîte)
   └──────────┘
   prix_sac       ← le nom (l'étiquette)
```

On écrit `prix_sac = 2500` : « colle l'étiquette `prix_sac` sur la valeur 2500 ».
Le signe `=` n'est **pas** « égal » comme en mathématiques : il veut dire « range dans ».

## 3. Pas à pas

### 3.1 Créer et utiliser une variable

```python
prix_sac = 2500
quantite = 3
total = prix_sac * quantite
print(total)  # 7500
```

On peut changer le contenu d'une variable (d'où son nom) :

```python
prix_sac = 2800
print(prix_sac * quantite)  # 8400
```

### 3.2 Bien nommer

Règles obligatoires : lettres, chiffres et `_`, **ne commence pas par un chiffre**, pas d'espace.
Convention (PEP 8) : minuscules avec `_` → `prix_sac`, `nombre_de_clients`.
Choisis des noms qui **expliquent** : `prix_sac` vaut mieux que `p` ou `x`.

### 3.3 Les types de base

Chaque valeur a un **type**. La fonction `type()` le révèle.

| Type | Signification | Exemples |
|---|---|---|
| `int` | nombre entier | `3`, `-12`, `2500` |
| `float` | nombre à virgule (on écrit un **point**) | `3.5`, `0.18` |
| `str` | texte | `"Manioc"` |
| `bool` | vrai ou faux | `True`, `False` |

```python
print(type(2500))  # <class 'int'>
print(type(18.5))  # <class 'float'>
print(type("Manioc"))  # <class 'str'>
print(type(True))  # <class 'bool'>
```

### 3.4 Les opérations

```python
print(7 + 2)  # 9     addition
print(7 - 2)  # 5     soustraction
print(7 * 2)  # 14    multiplication
print(7 / 2)  # 3.5   division (résultat toujours float)
print(7 // 2)  # 3     division entière (quotient)
print(7 % 2)  # 1     modulo (reste)
print(2**10)  # 1024  puissance
```

**Exemple concret** : partager 10 000 FCFA entre 3 personnes.

```python
part = 10000 // 3  # 3333 FCFA chacun
reste = 10000 % 3  # 1 FCFA qui reste
print(part, reste)  # 3333 1
```

La fonction `divmod(10000, 3)` donne les deux d'un coup : `(3333, 1)`.

**Priorité des opérations** : comme en mathématiques, `**` puis `* / // %` puis `+ -`.
Utilise des parenthèses pour être clair : `(prix + taxe) * quantite`.

### 3.5 Raccourcis

```python
stock = 100
stock = stock - 5  # 95
stock -= 5  # 90   (même chose, en plus court)
stock += 20  # 110
stock *= 2  # 220
```

### 3.6 Un pourcentage

Une remise de 15 % sur 20 000 FCFA :

```python
prix = 20000
remise = 15
prix_final = prix - prix * remise / 100
print(prix_final)  # 17000.0
```

### 3.7 Convertir et arrondir

```python
int(17.9)  # 17      (coupe, n'arrondit pas)
float(3)  # 3.0
round(3.14159, 2)  # 3.14    (arrondi à 2 décimales)
round(17000.0)  # 17000
```

## 4. ⚠️ Pièges courants

**Variable utilisée avant d'être créée**

```python
print(total)
```
```
NameError: name 'total' is not defined
```

**Mélanger texte et nombre**

```python
age = 25
print("J'ai " + age + " ans")
```
```
TypeError: can only concatenate str (not "int") to str
```
Solution : `print("J'ai", age, "ans")` (la leçon 1.3 montre aussi les f-strings).

**Les décimaux ne sont pas exacts**

```python
print(0.1 + 0.2)  # 0.30000000000000004
```
Les ordinateurs stockent les décimaux en binaire, ce qui crée de minuscules écarts. Pour afficher,
on **arrondit** : `round(0.1 + 0.2, 2)` → `0.3`. (Pour l'argent en production, on utilisera plus tard
le module `decimal`.)

**Diviser par zéro**

```python
print(5 / 0)
```
```
ZeroDivisionError: division by zero
```

## 5. À retenir

- `nom = valeur` range une valeur dans une variable.
- Types de base : `int`, `float`, `str`, `bool`.
- `/` donne toujours un `float` ; `//` le quotient entier ; `%` le reste.
- `+=`, `-=`, `*=` modifient une variable en place.
- `round(x, n)` arrondit ; `int()` coupe.
- Les décimaux sont approximatifs : arrondis à l'affichage.

## 6. Exercices

Fichier : [`exercices/ex02_variables_et_nombres.py`](../exercices/ex02_variables_et_nombres.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex02_variables_et_nombres.py -v
```

## 7. Quiz

1. Que contient `x` après `x = 5` puis `x += 3` ?
2. Quel est le résultat de `17 // 5` ? et de `17 % 5` ?
3. Quel est le type de `7 / 2` ?
4. Pourquoi `2variable = 1` est-il interdit ?
5. Que vaut `round(2.675, 1)` ? (réponds sans exécuter, puis vérifie)

<details>
<summary>Réponses</summary>

1. `8`
2. `3` et `2`
3. `float` (le résultat est `3.5`)
4. Un nom de variable ne peut pas commencer par un chiffre.
5. `2.7`. Essaie ensuite `round(2.675, 2)` : tu obtiens `2.67` et non `2.68`, à cause de l'imprécision des décimaux.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu sais maintenant mémoriser des valeurs et faire des calculs. C'est le socle de tout ce qui va suivre.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 1.3 — Le texte (chaînes de caractères)](l03_le_texte.md).
<!-- /cadre:fin -->
