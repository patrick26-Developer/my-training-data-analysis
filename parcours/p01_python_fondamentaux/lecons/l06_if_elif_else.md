# Leçon 2.2 — `if`, `elif`, `else` : choisir quoi faire

⏱ 60 min · 🎯 Débutant · 📦 Prérequis : leçon 2.1

## 🎯 Ce que tu sauras faire

- Exécuter du code **seulement si** une condition est vraie
- Gérer plusieurs cas avec `elif` et `else`
- Imbriquer des conditions proprement
- Écrire une condition sur une seule ligne (expression conditionnelle)

---

## 1. Le problème

Au marché, le prix change selon la quantité : moins de 10 sacs, plein tarif ; de 10 à 49, 5 % de remise ;
à partir de 50, 10 %. Le programme doit **choisir** une branche selon la situation.

## 2. L'idée en images

Une condition est un **carrefour** :

```
            quantité >= 50 ?
             /           \
          oui             non
      remise 10 %     quantité >= 10 ?
                       /          \
                    oui            non
                 remise 5 %     pas de remise
```

## 3. Pas à pas

### 3.1 `if`

```python
age = 20
if age >= 18:
    print("Accès autorisé")
print("Fin du programme")
```

Règles :
- la condition est suivie de **deux-points `:`** ;
- le bloc à exécuter est **indenté de 4 espaces** ;
- la ligne `print("Fin…")`, non indentée, s'exécute **toujours**.

### 3.2 `else` : l'autre cas

```python
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

### 3.3 `elif` : plusieurs cas

```python
quantite = 25

if quantite >= 50:
    remise = 10
elif quantite >= 10:
    remise = 5
else:
    remise = 0

print(f"Remise : {remise} %")  # Remise : 5 %
```

Python teste de haut en bas et **s'arrête à la première condition vraie**. L'ordre compte !
Si on avait mis `quantite >= 10` en premier, 60 sacs ne recevraient que 5 %.

### 3.4 Conditions combinées

```python
age = 30
resident = True
if age >= 18 and resident:
    print("Carte électeur possible")
```

### 3.5 Conditions imbriquées

```python
if age >= 18:
    if resident:
        print("OK")
    else:
        print("Résidence requise")
else:
    print("Trop jeune")
```

Évite plus de 2 niveaux : combine avec `and` quand c'est possible.

### 3.6 Expression conditionnelle (une seule ligne)

```python
statut = "majeur" if age >= 18 else "mineur"
```

### 3.7 Exemple complet : la note et la mention

```python
note = float(input("Note sur 20 : "))

if note >= 16:
    mention = "Très bien"
elif note >= 14:
    mention = "Bien"
elif note >= 12:
    mention = "Assez bien"
elif note >= 10:
    mention = "Passable"
else:
    mention = "Ajourné"

print(f"Mention : {mention}")
```

## 4. ⚠️ Pièges courants

**Oublier les deux-points**

```python
if age >= 18
    print("Majeur")
```
```
SyntaxError: expected ':'
```

**Mauvaise indentation**

```python
if age >= 18:
print("Majeur")
```
```
IndentationError: expected an indented block after 'if' statement on line 1
```

**Tests dans le mauvais ordre** (cf. 3.3) : toujours du plus restrictif au plus large.

**Répéter la variable**

```python
if jour == "sam" or "dim":     # ❌ toujours vrai !
if jour == "sam" or jour == "dim":   # ✅
if jour in ("sam", "dim"):           # ✅ encore mieux
```

## 5. À retenir

- `if condition:` + bloc indenté ; `elif` pour d'autres cas ; `else` pour le reste.
- Une seule branche est exécutée : la première dont la condition est vraie.
- Ne pas oublier `:` ni l'indentation.
- `a if cond else b` pour choisir une valeur en une ligne.

## 6. Exercices

Fichier : [`exercices/ex06_if_elif_else.py`](../exercices/ex06_if_elif_else.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex06_if_elif_else.py -v
```

## 7. Quiz

1. Que fait un `elif` quand une condition précédente est déjà vraie ?
2. Combien de branches d'un `if/elif/else` s'exécutent au maximum ?
3. Pourquoi `if x == 1 or 2:` est-il faux ?
4. Réécris `if a > b: m = a else: m = b` en une ligne.

<details>
<summary>Réponses</summary>

1. Il est ignoré : seule la première branche vraie s'exécute.
2. Une seule.
3. `2` est toujours « vrai » : la condition l'est donc toujours. Il faut `x == 1 or x == 2` (ou `x in (1, 2)`).
4. `m = a if a > b else b`

</details>
