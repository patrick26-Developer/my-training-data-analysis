# Leçon 6.1 — Les exceptions : gérer les erreurs

⏱ 55 min · 🎯 Intermédiaire · 📦 Prérequis : module 5

## 🎯 Ce que tu sauras faire

- Lire une **trace d'erreur** (*traceback*) et en déduire la cause
- Attraper une erreur avec `try / except`
- Utiliser `else` et `finally`
- **Lever** tes propres erreurs avec `raise`
- Valider les saisies d'un utilisateur sans faire planter le programme

---

## 1. Le problème

```python
age = int(input("Âge : "))  # l'utilisateur tape "vingt"
```
```
ValueError: invalid literal for int() with base 10: 'vingt'
```

Le programme s'arrête brutalement. Un bon programme **prévoit** ce qui peut mal tourner et réagit proprement :
message clair, nouvelle tentative, fichier fermé correctement…

## 2. L'idée en images

Une exception est un **signal d'alarme** : quand une erreur survient, Python interrompt le déroulement normal et
remonte à la recherche d'un `except` capable de la traiter.

```
   code normal ──► ERREUR ──► saute au except ──► le programme continue
                        └─ (sans except : le programme s'arrête)
```

## 3. Pas à pas

### 3.1 Lire un traceback

```
Traceback (most recent call last):
  File "caisse.py", line 12, in <module>
    total = calculer(prix, quantite)
  File "caisse.py", line 5, in calculer
    return prix / quantite
ZeroDivisionError: division by zero
```

Lis **de bas en haut** : la dernière ligne donne le **type** et le **message** ; au-dessus, la ligne de code fautive,
puis les appels qui y ont mené.

Les erreurs les plus fréquentes : `ValueError`, `TypeError`, `KeyError`, `IndexError`, `NameError`,
`ZeroDivisionError`, `FileNotFoundError`.

### 3.2 `try` / `except`

```python
try:
    age = int(input("Âge : "))
except ValueError:
    print("Merci de taper un nombre entier.")
```

On peut attraper **plusieurs** types et récupérer le message :

```python
try:
    resultat = a / b
except ZeroDivisionError:
    resultat = None
except (TypeError, ValueError) as erreur:
    print("Données invalides :", erreur)
    resultat = None
```

### 3.3 `else` et `finally`

```python
try:
    n = int(texte)
except ValueError:
    print("Invalide")
else:
    print("Converti :", n)  # seulement si AUCUNE erreur
finally:
    print("Terminé")  # TOUJOURS exécuté (nettoyage)
```

### 3.4 Boucle de saisie robuste

```python
def lire_entier(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Ce n'est pas un entier, recommence.")
```

### 3.5 Lever une exception avec `raise`

```python
def retirer(solde, montant):
    if montant <= 0:
        raise ValueError("Le montant doit être positif")
    if montant > solde:
        raise ValueError("Solde insuffisant")
    return solde - montant


try:
    retirer(1000, 5000)
except ValueError as e:
    print("Refusé :", e)  # Refusé : Solde insuffisant
```

Lever une exception, c'est dire : « Je ne peux pas faire ce qu'on me demande, et ce n'est pas à moi de deviner. »

### 3.6 Créer ses propres exceptions

```python
class SoldeInsuffisant(Exception):
    pass


raise SoldeInsuffisant("Il manque 4 000 FCFA")
```

(Les classes sont étudiées dans le parcours P02 ; retiens seulement cette forme.)

### 3.7 `assert`

```python
assert quantite > 0, "La quantité doit être positive"
```

`assert` sert à vérifier des **hypothèses de développement** (et dans les tests). Ne l'utilise pas pour valider des
saisies d'utilisateurs : il peut être désactivé.

## 4. ⚠️ Pièges courants

**`except:` nu** attrape **tout**, même `Ctrl + C` : cache les vrais bugs. Précise toujours le type.

**Un `try` trop grand** : n'entoure que la ligne qui peut échouer.

**Avaler l'erreur en silence**

```python
except Exception:
    pass          # ❌ tu ne sauras jamais ce qui s'est passé
```

**Utiliser des exceptions pour tout** : un simple `if` est souvent plus clair (`if b != 0:`).

## 5. À retenir

- Traceback : lis la dernière ligne, puis remonte.
- `try / except Type as e / else / finally`.
- `raise Type("message")` signale une erreur.
- Attrape des erreurs **précises**, jamais `except:` nu.

## 6. Exercices

Fichier : [`exercices/ex20_exceptions.py`](../exercices/ex20_exceptions.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex20_exceptions.py -v
```

## 7. Quiz

1. Quelle ligne d'un traceback donne le type d'erreur ?
2. Quand le bloc `else` d'un `try` s'exécute-t-il ?
3. Quand le bloc `finally` s'exécute-t-il ?
4. Pourquoi éviter `except:` sans type ?

<details>
<summary>Réponses</summary>

1. La dernière.
2. Seulement si aucune exception n'a été levée dans le `try`.
3. Toujours, qu'il y ait eu une erreur ou non.
4. Il attrape toutes les erreurs, y compris celles qu'on ne prévoyait pas, et masque les vrais bugs.

</details>
