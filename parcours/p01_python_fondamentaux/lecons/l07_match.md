# Leçon 2.3 — `match` : choisir parmi plusieurs valeurs

⏱ 40 min · 🎯 Débutant · 📦 Prérequis : leçon 2.2

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Un menu clair et lisible en quelques lignes : `match` va rendre tes choix multiples bien plus élégants.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Utiliser `match / case` pour remplacer une longue chaîne de `elif`
- Regrouper plusieurs valeurs avec `|`
- Ajouter une condition avec `if` (garde)
- Choisir entre `match` et `if`

---

## 1. Le problème

Un menu de console : `1` ajouter, `2` supprimer, `3` afficher, `q` quitter. Avec des `elif`,
on répète `choix == ...` à chaque ligne. `match` rend le code plus lisible quand on compare
**une même variable à plusieurs valeurs**.

## 2. Pas à pas

### 2.1 Syntaxe de base

```python
choix = "2"

match choix:
    case "1":
        print("Ajouter")
    case "2":
        print("Supprimer")
    case "3":
        print("Afficher")
    case _:
        print("Choix inconnu")
```

- `case _:` est le cas **par défaut** (comme `else`) : `_` accepte n'importe quoi.
- Python exécute le **premier** `case` qui correspond, puis sort du `match`.

### 2.2 Plusieurs valeurs avec `|`

```python
jour = "sam"

match jour:
    case "sam" | "dim":
        type_jour = "week-end"
    case "lun" | "mar" | "mer" | "jeu" | "ven":
        type_jour = "semaine"
    case _:
        type_jour = "inconnu"
```

### 2.3 Une garde avec `if`

```python
note = 14

match note:
    case n if n >= 16:
        mention = "Très bien"
    case n if n >= 10:
        mention = "Admis"
    case _:
        mention = "Ajourné"
```

Ici `n` capture la valeur et le `if` ajoute une condition.

### 2.4 Aperçu : reconnaître la forme d'une donnée

`match` sait aussi décomposer des structures (listes, dictionnaires, objets) : on y reviendra
aux modules 4 et au parcours POO. Un avant-goût :

```python
commande = ("deplacer", 3, 4)

match commande:
    case ("deplacer", x, y):
        print(f"Aller en ({x}, {y})")
    case ("quitter",):
        print("Au revoir")
```

## 3. `match` ou `if` ?

| Situation | Choix |
|---|---|
| Comparer une variable à des valeurs précises (menu, jours, codes) | `match` |
| Conditions sur des intervalles ou des combinaisons (`age >= 18 and ...`) | `if / elif` |

## 4. ⚠️ Pièges courants

**Le nom nu capture tout**

```python
SEUIL = 10
match valeur:
    case SEUIL:  # ❌ ne compare pas : capture n'importe quelle valeur dans SEUIL !
        ...
```
Un nom simple dans un `case` est une **capture**. Pour comparer à une constante, écris-la avec un point
(`case Config.SEUIL:`) ou utilise un `if` / une garde.

**Oublier `case _`** : si aucune valeur ne correspond, il ne se passe rien, sans message d'erreur.

**Python plus ancien que 3.10** : `match` n'existe pas (ce cours utilise Python 3.13).

## 5. À retenir

- `match variable:` + des `case valeur:` ; `case _:` = par défaut.
- `|` regroupe plusieurs valeurs ; `case n if ...` ajoute une condition.
- Idéal pour les menus et les codes ; sinon `if / elif`.

## 6. Exercices

Fichier : [`exercices/ex07_match.py`](../exercices/ex07_match.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex07_match.py -v
```

## 7. Quiz

1. Que représente `case _:` ?
2. Comment écrire « samedi ou dimanche » dans un `case` ?
3. Combien de `case` s'exécutent au maximum ?
4. Pour tester `age >= 18`, préfères-tu `match` ou `if` ? Pourquoi ?

<details>
<summary>Réponses</summary>

1. Le cas par défaut, qui accepte toute valeur.
2. `case "samedi" | "dimanche":`
3. Un seul.
4. `if` : c'est une comparaison sur un intervalle, pas sur des valeurs précises.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu as ajouté un outil élégant à ta boîte : tes menus seront désormais propres et faciles à lire.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 3.1 — La boucle `while`](l08_while.md).
<!-- /cadre:fin -->
