# Leçon 3.1 — La boucle `while`

⏱ 50 min · 🎯 Débutant · 📦 Prérequis : module 2

## 🎯 Ce que tu sauras faire

- Répéter des instructions **tant qu'une condition est vraie**
- Utiliser un compteur et un accumulateur
- Écrire une boucle de saisie qui redemande tant que la réponse est invalide
- Éviter la boucle infinie

---

## 1. Le problème

Tu veux afficher les nombres de 1 à 100, ou redemander un code PIN tant qu'il est faux.
Écrire 100 `print` serait absurde : on **répète** une action. C'est le rôle des boucles.

## 2. L'idée en images

```
          ┌──────────────┐
   ┌────► │ condition ?  │──non──► sortie
   │      └──────┬───────┘
   │            oui
   │      ┌──────▼───────┐
   └──────│ faire le bloc│
          └──────────────┘
```

Python teste la condition **avant chaque tour**. Tant qu'elle est vraie, il exécute le bloc.

## 3. Pas à pas

### 3.1 Un compteur

```python
n = 1
while n <= 5:
    print(n)
    n += 1
print("Fini")
```
```
1
2
3
4
5
Fini
```

Trois éléments à toujours vérifier :
1. **Initialisation** : `n = 1` ;
2. **Condition** : `n <= 5` ;
3. **Progression** : `n += 1` (sans elle, la boucle ne s'arrête jamais).

### 3.2 Un accumulateur : additionner

```python
total = 0
n = 1
while n <= 100:
    total += n
    n += 1
print(total)  # 5050
```

### 3.3 Saisie contrôlée

```python
age = int(input("Âge : "))
while age < 0 or age > 120:
    print("Âge invalide.")
    age = int(input("Âge : "))
```

### 3.4 Boucle jusqu'à un mot de sortie (sentinelle)

```python
total = 0
saisie = input("Prix (ou 'fin') : ")
while saisie != "fin":
    total += float(saisie)
    saisie = input("Prix (ou 'fin') : ")
print(f"Total : {total} FCFA")
```

### 3.5 Exemple : la suite de Collatz

On part d'un nombre ; s'il est pair on le divise par 2, sinon on fait ×3 + 1. On compte les étapes jusqu'à 1.

```python
n = 6
etapes = 0
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    etapes += 1
print(etapes)  # 8
```

## 4. ⚠️ Pièges courants

**Boucle infinie**

```python
n = 1
while n <= 5:
    print(n)  # on a oublié n += 1 !
```
Le programme tourne sans fin. Arrête-le avec **Ctrl + C**.

**Décalage d'une unité** (*off-by-one*) : `while n < 5` s'arrête à 4 ; `while n <= 5` s'arrête à 5.

**Condition jamais vraie au départ** : le bloc ne s'exécute alors **aucune fois**.

## 5. À retenir

- `while condition:` répète tant que la condition est vraie.
- Pense : **initialisation, condition, progression**.
- Compteur (`+= 1`) et accumulateur (`total += x`).
- Ctrl + C interrompt une boucle infinie.

## 6. Exercices

Fichier : [`exercices/ex08_while.py`](../exercices/ex08_while.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex08_while.py -v
```

## 7. Quiz

1. Combien de fois s'exécute `n = 0; while n < 3: n += 1` ?
2. Que se passe-t-il si on oublie `n += 1` ?
3. Comment arrêter un programme bloqué ?
4. À quoi sert une « sentinelle » ?

<details>
<summary>Réponses</summary>

1. 3 fois.
2. La boucle est infinie.
3. Ctrl + C dans le terminal.
4. C'est une valeur spéciale (comme `"fin"`) qui signale la fin de la saisie.

</details>
