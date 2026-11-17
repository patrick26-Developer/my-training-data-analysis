# Leçon 5.1 — Définir et appeler une fonction

⏱ 60 min · 🎯 Débutant · 📦 Prérequis : module 4

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Écris une fois, utilise cent fois : les fonctions vont transformer ton code en briques réutilisables.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Écrire une fonction avec `def`, des paramètres et `return`
- Distinguer **afficher** (`print`) et **retourner** (`return`)
- Retourner plusieurs valeurs
- Documenter une fonction avec une docstring

---

## 1. Le problème

Tu calcules le prix TTC à dix endroits de ton programme. Si la TVA change, tu dois modifier dix lignes — et tu
risques d'en oublier une. Une **fonction** regroupe un calcul sous un nom : tu l'écris **une fois**, tu l'utilises
**partout**. Tu en as déjà utilisé : `print`, `len`, `input`. Maintenant, tu écris les tiennes.

## 2. L'idée en images

Une fonction est une **machine** : on met des ingrédients (arguments), elle produit un résultat.

```
   prix = 1000 ─┐
                ├─►  [ prix_ttc ]  ─►  1180.0
   taux = 18  ──┘
```

## 3. Pas à pas

### 3.1 Définir et appeler

```python
def prix_ttc(prix_ht, taux):
    return prix_ht * (1 + taux / 100)


resultat = prix_ttc(1000, 18)
print(resultat)  # 1180.0
```

- `def nom(paramètres):` puis un bloc **indenté** ;
- `return valeur` renvoie le résultat à l'appelant et **termine** la fonction ;
- **Paramètres** : les noms dans la définition (`prix_ht`) ; **arguments** : les valeurs à l'appel (`1000`).

### 3.2 `print` ≠ `return`

```python
def double_print(n):
    print(n * 2)  # affiche, mais ne rend rien


def double_return(n):
    return n * 2  # rend la valeur : on peut la réutiliser


x = double_print(5)  # affiche 10, mais x vaut None
y = double_return(5) + 1  # y vaut 11
```

Règle : **une fonction qui calcule doit `return`** ; `print` est réservé à l'affichage final.

### 3.3 Une fonction sans `return` renvoie `None`

```python
def saluer(nom):
    print(f"Mbote, {nom} !")


resultat = saluer("Grâce")  # affiche le message
print(resultat)  # None
```

### 3.4 Plusieurs valeurs

```python
def stats(nombres):
    return min(nombres), max(nombres), sum(nombres) / len(nombres)


petit, grand, moyenne = stats([4, 9, 2])
```

### 3.5 Retours anticipés

```python
def mention(note):
    if note < 0 or note > 20:
        return "Note invalide"
    if note >= 10:
        return "Admis"
    return "Ajourné"
```

`return` à l'intérieur d'un `if` permet de sortir tôt : le code reste plat et lisible.

### 3.6 Docstring et annotations

```python
def prix_ttc(prix_ht: float, taux: float) -> float:
    """Retourne le prix TTC.

    prix_ht : prix hors taxe en FCFA
    taux    : taux de TVA en pourcentage
    """
    return prix_ht * (1 + taux / 100)


help(prix_ttc)  # affiche la docstring
```

Les annotations (`: float`, `-> float`) sont facultatives mais précieuses : elles documentent. Elles sont étudiées
en profondeur en Python avancé (parcours P03).

### 3.7 Une fonction peut en appeler une autre

```python
def total_panier(prix):
    return sum(prix_ttc(p, 18) for p in prix)
```

Décomposer un gros problème en petites fonctions est **la** compétence clé du programmeur.

## 4. ⚠️ Pièges courants

**Oublier de `return`**

```python
def carre(n):
    n * n  # calcule mais jette le résultat !


print(carre(3))  # None
```

**Appeler sans parenthèses** : `prix_ttc` est la fonction ; `prix_ttc(1000, 18)` l'exécute.

**Mauvais nombre d'arguments**

```python
prix_ttc(1000)
```
```
TypeError: prix_ttc() missing 1 required positional argument: 'taux'
```

**Du code après `return`** n'est jamais exécuté.

## 5. À retenir

- `def nom(param1, param2):` + `return résultat`.
- `return` renvoie une valeur ; sans `return`, on obtient `None`.
- Une fonction = un rôle précis, un nom clair, une docstring.
- Retourner plusieurs valeurs = retourner un tuple.

## 6. Exercices

Fichier : [`exercices/ex16_definir_et_appeler.py`](../exercices/ex16_definir_et_appeler.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex16_definir_et_appeler.py -v
```

## 7. Quiz

1. Que renvoie une fonction sans `return` ?
2. Quelle différence entre paramètre et argument ?
3. Que se passe-t-il après un `return` ?
4. Pourquoi préférer `return` à `print` dans un calcul ?

<details>
<summary>Réponses</summary>

1. `None`.
2. Le paramètre est le nom dans la définition ; l'argument est la valeur fournie à l'appel.
3. La fonction s'arrête : le code suivant n'est pas exécuté.
4. Parce qu'on peut réutiliser le résultat (le stocker, le tester, le combiner), alors qu'un `print` ne fait qu'afficher.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu écris tes premières fonctions : tu ne copieras plus jamais le même code deux fois.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 5.2 — Paramètres : défauts, mots-clés, `*args`, `**kwargs`](l17_parametres.md).
<!-- /cadre:fin -->
