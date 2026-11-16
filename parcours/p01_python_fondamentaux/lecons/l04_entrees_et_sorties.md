# Leçon 1.4 — Entrées et sorties : dialoguer avec l'utilisateur

⏱ 60 min · 🎯 Débutant · 📦 Prérequis : leçons 1.1 à 1.3

## 🎯 Ce que tu sauras faire

- Demander une information à l'utilisateur avec `input()`
- Convertir ce qu'il tape (toujours du texte) en nombre
- Afficher un résultat bien présenté
- Écrire un petit programme interactif complet

---

## 1. Le problème

Jusqu'ici, tes programmes affichent toujours la même chose. Un vrai programme **pose des questions**
et réagit aux réponses : « Combien de sacs ? » → calcule la facture.

## 2. L'idée en images

Un programme interactif suit toujours trois temps :

```
 ENTRÉE            TRAITEMENT           SORTIE
 (input)    →      (calculs)     →      (print)
 "3 sacs"          3 × 2500             "Total : 7 500 FCFA"
```

## 3. Pas à pas

### 3.1 `input()`

```python
nom = input("Quel est ton nom ? ")
print(f"Mbote, {nom} !")
```

Exécution :

```
Quel est ton nom ? Grâce
Mbote, Grâce !
```

Le texte entre parenthèses est la **question** affichée. Le programme **s'arrête** et attend que
l'utilisateur tape sa réponse puis Entrée.

### 3.2 Règle d'or : `input()` renvoie TOUJOURS du texte

```python
quantite = input("Combien de sacs ? ")  # l'utilisateur tape 3
print(quantite * 2)  # 33  (le texte "3" répété 2 fois !)
```

Pour calculer, il faut **convertir** :

```python
quantite = int(input("Combien de sacs ? "))
prix = float(input("Prix d'un sac : "))
print(quantite * prix)
```

- `int(...)` pour un entier, `float(...)` pour un nombre à virgule.
- Si l'utilisateur tape `"trois"`, Python plante avec `ValueError`. Tu apprendras à gérer ça au module 6 ;
  pour l'instant, on suppose qu'il tape correctement.

### 3.3 Un programme complet : la facture

```python
print("=== Boutique Mama Nzoni ===")

produit = input("Produit : ").strip().title()
prix = float(input("Prix unitaire (FCFA) : "))
quantite = int(input("Quantité : "))

total = prix * quantite

print()  # ligne vide
print(f"Produit  : {produit}")
print(f"Quantité : {quantite}")
print(f"Total    : {total:,.0f} FCFA")
```

Exécution :

```
=== Boutique Mama Nzoni ===
Produit : manioc
Prix unitaire (FCFA) : 2500
Quantité : 3

Produit  : Manioc
Quantité : 3
Total    : 7,500 FCFA
```

On retrouve : **entrées** (`input`), **traitement** (`prix * quantite`), **sorties** (`print`).

### 3.4 Bien présenter

```python
print("=" * 30)
print(f"{'Produit':<12}{'Qté':>5}{'Total':>10}")  # < gauche, > droite
print(f"{'Manioc':<12}{3:>5}{7500:>10,}")
print("=" * 30)
```

```
==============================
Produit       Qté     Total
Manioc          3     7,500
==============================
```

### 3.5 Écrire une fonction qui utilise `input`

Dans les exercices, on te demandera parfois de coder une fonction qui appelle `input()`.
Les tests simulent la saisie de l'utilisateur à ta place : tu n'as rien à taper.

```python
def demander_prenom():
    prenom = input("Prénom : ")
    return prenom.strip().title()
```

## 4. ⚠️ Pièges courants

**Oublier la conversion**

```python
age = input("Âge : ")
print(age + 1)
```
```
TypeError: can only concatenate str (not "int") to str
```
Correction : `age = int(input("Âge : "))`.

**Convertir un nombre décimal avec `int`**

```python
int("2.5")
```
```
ValueError: invalid literal for int() with base 10: '2.5'
```
Utilise `float("2.5")` (ou `int(float("2.5"))` pour couper la partie décimale).

**Virgule à la place du point**

`float("2,5")` échoue. Les nombres à virgule s'écrivent avec un **point** en Python.
Astuce : `float(texte.replace(",", "."))` accepte les deux écritures.

## 5. À retenir

- Programme interactif = **entrée → traitement → sortie**.
- `input("question")` renvoie **toujours du texte**.
- Convertis avec `int()` ou `float()` avant de calculer.
- Les f-strings (`{valeur:,.2f}`, `{texte:<10}`) présentent proprement les résultats.

## 6. Exercices

Fichier : [`exercices/ex04_entrees_et_sorties.py`](../exercices/ex04_entrees_et_sorties.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex04_entrees_et_sorties.py -v
```

## 7. Mini-projet du module 1 — La caisse du marché

Dans un fichier `caisse.py`, écris un programme qui :

1. demande le nom du client, le nom du produit, le prix unitaire et la quantité ;
2. calcule le total, puis applique une remise de 5 % si le total dépasse 10 000 FCFA ;
   *(les conditions arrivent au module 2 : fais d'abord sans la remise, puis reviens l'ajouter)* ;
3. affiche un **reçu** aligné, avec le nom de la boutique, le client, le détail et le total en FCFA
   *et* en euros (1 € = 655,957 FCFA).

Une solution de référence est dans [`../projets/m1_caisse_du_marche.py`](../projets/m1_caisse_du_marche.py).
Essaie d'abord seul(e) !

## 8. Quiz

1. Quel est le type de `input("Âge : ")` si l'utilisateur tape `25` ?
2. Que fait `int(input("N : ")) * 2` si l'utilisateur tape `4` ?
3. Pourquoi `float("2,5")` échoue-t-il ?
4. Quelles sont les trois étapes d'un programme interactif ?
5. Que produit `f"{7500:,}"` ?

<details>
<summary>Réponses</summary>

1. `str` (du texte `"25"`).
2. `8`
3. Python attend un point décimal : `"2.5"`.
4. Entrée, traitement, sortie.
5. `7,500`

</details>
