# Leçon 1.1 — Classes, instances et méthodes

⏱ 60 min · 🎯 Débutant → Intermédiaire · 📦 Prérequis : P01 (fonctions, dictionnaires)

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Aujourd'hui, tes produits cessent d'être de simples dictionnaires : ils deviennent de vrais « objets » qui savent calculer leur propre valeur et s'afficher. C'est le déclic de la programmation orientée objet.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Créer ta première **classe** et en fabriquer plusieurs **objets** indépendants
- Lire et modifier les **attributs** d'un objet
- Écrire des **méthodes** (des fonctions qui appartiennent à l'objet)
- Expliquer à quelqu'un ce que veut dire `self`

---

## 1. Le problème

Dans le projet boutique de P01, chaque produit était un dictionnaire :

```python
riz = {"nom": "Riz", "prix": 800, "quantite": 3}
sel = {"nom": "Sel", "prix": 100, "quantite": 10}
```

Ça marche, mais regarde ce qui se répète : à chaque produit, il faut réécrire les mêmes clés `"nom"`, `"prix"`,
`"quantite"`. Une faute de frappe (`"quantité"` au lieu de `"quantite"`) et le programme plante. Et pour calculer la
valeur d'un produit, il faut une fonction à part, quelque part ailleurs dans le code.

Et si le produit **savait lui-même** calculer sa valeur ? Et si Python vérifiait pour nous que tous les produits ont
bien les mêmes champs ? C'est exactement ce que permet une **classe**.

## 2. L'idée en images

Pense à un **moule à gâteaux** :

```
        le MOULE (la classe)                les GÂTEAUX (les objets)
      ┌──────────────────────┐             ┌──────────┐  ┌──────────┐
      │  Produit             │   ───►      │ Riz      │  │ Sel      │
      │  nom, prix, quantite │             │ 800 × 3  │  │ 100 × 10 │
      │  valeur(), etiquette()│            └──────────┘  └──────────┘
      └──────────────────────┘
```

- La **classe** décrit *comment est fait* un produit (quels champs, quelles actions). C'est le plan, le moule.
- Une **instance** (ou **objet**) est un produit *réel* fabriqué avec ce moule. On peut en fabriquer autant qu'on veut.
- Un **attribut** est une donnée de l'objet (son nom, son prix…).
- Une **méthode** est une fonction qui appartient à l'objet (par exemple `valeur()`).

Chaque gâteau a sa propre garniture, mais tous suivent le même moule.

## 3. Pas à pas

### Étape 1 — Écrire la classe

```python
class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
```

Prenons-la ligne par ligne :

- `class Produit:` déclare la classe. Par convention, son nom commence par une **majuscule**.
- `__init__` est la méthode spéciale appelée **automatiquement** à la création d'un objet : c'est le « constructeur »,
  celui qui installe les données de départ.
- `self` désigne **l'objet en train d'être créé** (ou utilisé). Python le passe tout seul : tu ne l'écris jamais
  quand tu appelles la méthode, mais tu dois toujours le mettre comme **premier paramètre** dans la définition.
- `self.nom = nom` range la valeur reçue dans l'attribut `nom` **de cet objet-là**.

### Étape 2 — Fabriquer des objets

```python
riz = Produit("Riz", 800, 3)
sel = Produit("Sel", 100, 10)

print(riz.nom)  # Riz
print(sel.prix)  # 100
```

`Produit("Riz", 800, 3)` appelle `__init__` en lui donnant `"Riz"`, `800` et `3`. Chaque objet garde **ses propres**
valeurs, indépendantes de celles des autres.

### Étape 3 — Modifier un attribut

```python
riz.quantite = riz.quantite - 1  # un client achète un sac
print(riz.quantite)  # 2
print(sel.quantite)  # 10   (le sel n'a pas bougé)
```

### Étape 4 — Ajouter des méthodes

Une méthode se définit comme une fonction, **à l'intérieur** de la classe, avec `self` en premier paramètre :

```python
class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def valeur(self):
        return self.prix * self.quantite

    def etiquette(self):
        return f"{self.nom} : {self.prix} FCFA"


riz = Produit("Riz", 800, 3)
print(riz.valeur())  # 2400
print(riz.etiquette())  # Riz : 800 FCFA
```

Regarde l'appel : `riz.valeur()`. Python le traduit en `Produit.valeur(riz)` : l'objet `riz` devient `self`
à l'intérieur de la méthode. Voilà pourquoi `self.prix` vaut ici `800`.

Une méthode qui **calcule** (comme `valeur`) ne modifie pas l'objet : elle rend un résultat et laisse les attributs
tranquilles.

### Étape 5 — Pourquoi c'est mieux qu'un dictionnaire ?

| Avec des dictionnaires | Avec une classe |
|---|---|
| clés répétées à la main, risque de faute de frappe | champs déclarés une seule fois |
| fonctions éparpillées | méthodes rangées avec les données |
| aucune garantie de structure | tous les produits ont la même forme |

Ce n'est pas magique : un objet *contient* un dictionnaire de ses attributs (`riz.__dict__`). Mais le code devient
plus clair, plus sûr et plus facile à faire grandir.

## 4. ⚠️ Pièges courants

**Oublier `self` dans une méthode**

Le message est un peu déroutant : Python dit qu'il a reçu un argument « en trop », alors que tu n'en as donné aucun !
C'est `self`, passé automatiquement, qui n'a nulle part où aller.

**Deux noms pour le même objet**

```python
a = Produit("Riz", 800, 3)
b = a  # b n'est PAS une copie : c'est le même objet
b.quantite = 0
print(a.quantite)  # 0 !
```

Pour deux objets indépendants, il faut appeler `Produit(...)` deux fois.

**Exemple complet : constater l'erreur, puis la corriger**

```python
class Produit:
    def valeur():  # erreur : le paramètre d'instance manque
        return 100


try:
    Produit().valeur()
except TypeError as erreur:
    assert "positional argument" in str(erreur)


class ProduitCorrige:
    def valeur(self):
        return 100


assert ProduitCorrige().valeur() == 100
```

## 5. À retenir

- Une **classe** est un moule ; une **instance** est un objet fabriqué avec ce moule.
- `__init__` prépare chaque nouvel objet ; `self` est l'objet courant.
- Les **attributs** sont les données de l'objet, les **méthodes** ses actions.
- `b = a` ne copie pas l'objet : il lui donne un deuxième nom.

## 6. Exercices

Complète les trois tâches dans [le fichier d'exercices](../exercices/ex01_classes.py), puis vérifie avec :

```powershell
python -m pytest parcours/p02_poo_et_conception/exercices/test_ex01_classes.py -v
```

Compare ensuite avec le [corrigé commenté](../solutions/sol01_classes.py). Essaie d'abord seul(e) !

## 7. Quiz

1. Que représente `self` ?
2. Quand `__init__` est-elle appelée ?
3. Une classe est-elle une instance ?
4. Que retourne `valeur()` pour un prix de 500 et une quantité de 4 ?
5. Deux noms peuvent-ils désigner le même objet ?

<details>
<summary>Réponses</summary>

1. L'objet courant, celui sur lequel on appelle la méthode.
2. Automatiquement, au moment où on crée l'objet avec `Produit(...)`.
3. Non : la classe est le moule, l'instance est l'objet fabriqué.
4. `2000`.
5. Oui : `b = a` donne un deuxième nom au même objet.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu viens de créer ta première classe et tes premiers objets. Tu es entré(e) dans la programmation orientée objet, celle que tu retrouveras dans presque tous les projets professionnels.

💬 *Bloqué(e) ? C'est normal. Relis l'étape qui te pose problème, retape l'exemple toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 2.1 — Composition et encapsulation](l02_composition.md).
<!-- /cadre:fin -->
