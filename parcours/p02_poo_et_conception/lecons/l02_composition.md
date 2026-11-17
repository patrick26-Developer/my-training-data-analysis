# Leçon 2.1 — Composition et encapsulation

⏱ 60 min · 🎯 Débutant → Intermédiaire · 📦 Prérequis : leçon 1.1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Tu vas construire un `Stock` qui refuse tout seul les quantités absurdes, comme un bon magasinier qui ne laisse personne fausser les comptes. Plus jamais de stock négatif !
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Construire un objet qui **contient** d'autres données (la **composition**)
- **Protéger** une donnée pour qu'elle reste toujours valide (l'**encapsulation**)
- Offrir une lecture contrôlée avec `@property`
- Faire la différence entre une simple convention (`_nom`) et une vraie protection

---

## 1. Le problème

Mama Nzoni gère son stock avec un simple dictionnaire. Un matin, elle tape par erreur `-50` en quantité de riz.
Résultat : la valeur totale de la boutique diminue au lieu d'augmenter, et personne ne comprend pourquoi.

```python
stock = {"Riz": 3}
stock["Riz"] = stock["Riz"] + (-50)  # personne ne t'arrête
print(stock)  # {'Riz': -47}
```

Le dictionnaire accepte **tout**, sans broncher. Il faudrait un « gardien » qui vérifie chaque modification.
C'est le rôle d'un objet **bien conçu** : il regroupe les données **et** les règles qui les protègent.

## 2. L'idée en images

Deux idées à retenir :

- **Composition** : un objet en *contient* d'autres. Un `Stock` *contient* des produits ; il n'est pas un produit.
  (On dit « a un », pas « est un ».)
- **Encapsulation** : on enferme les données dans l'objet et on n'autorise leur modification que par des
  méthodes qui **vérifient** les règles. Ces règles qui doivent toujours rester vraies s'appellent des **invariants**
  (ici : « une quantité est toujours un entier strictement positif »).

```
   dehors                       dedans l'objet Stock
 ┌─────────┐   ajouter("Riz", 3)  ┌──────────────────────────┐
 │ le code │ ───────────────────► │ vérifie → puis modifie   │
 │ appelant│ ◄─────────────────── │ _quantites = {...}       │
 └─────────┘   quantite("Riz")    └──────────────────────────┘
```

## 3. Pas à pas

### Étape 1 — Un stock avec un gardien

```python
class Stock:
    def __init__(self):
        self._quantites = {}

    def ajouter(self, nom, quantite):
        if quantite <= 0:
            raise ValueError("Quantité strictement positive requise.")
        self._quantites[nom] = self._quantites.get(nom, 0) + quantite

    def quantite(self, nom):
        return self._quantites.get(nom, 0)


stock = Stock()
stock.ajouter("Riz", 3)
print(stock.quantite("Riz"))  # 3
```

Ce que fait chaque partie :

- Le dictionnaire `_quantites` est créé **dans `__init__`** : chaque stock reçoit **le sien**.
- Le tiret bas `_` devant le nom est une **convention** : « ceci est interne, ne le touche pas directement ».
  Python ne l'interdit pas, mais tout lecteur du code comprend le message.
- `ajouter` **vérifie avant de modifier**. Si la quantité est invalide, il lève une exception et **ne change rien**.
- `quantite` rend la quantité d'un produit, ou `0` s'il n'existe pas.

### Étape 2 — Voir le gardien à l'œuvre

```python
try:
    stock.ajouter("Riz", -50)
except ValueError as erreur:
    print("Refusé :", erreur)  # Refusé : Quantité strictement positive requise.

print(stock.quantite("Riz"))  # 3  (rien n'a changé)
```

C'est tout l'intérêt : le stock **reste valide**, quoi qu'on tente.

### Étape 3 — Lire sans pouvoir casser : `@property`

Parfois, on veut laisser *lire* une information, sans permettre de la modifier. On utilise une **propriété** :

```python
class Stock:
    def __init__(self):
        self._quantites = {}

    def ajouter(self, nom, quantite):
        if quantite <= 0:
            raise ValueError("Quantité strictement positive requise.")
        self._quantites[nom] = self._quantites.get(nom, 0) + quantite

    @property
    def produits(self):
        return dict(self._quantites)  # on rend une COPIE


stock = Stock()
stock.ajouter("Riz", 3)
print(stock.produits)  # {'Riz': 3}   (sans parenthèses : comme un attribut)

copie = stock.produits
copie["Riz"] = 999  # on modifie la copie…
print(stock.produits)  # {'Riz': 3}   …le vrai stock est intact
```

Deux détails importants :

1. `@property` permet d'écrire `stock.produits` (sans parenthèses) tout en exécutant du code.
2. On renvoie `dict(...)`, **une copie**. Si on renvoyait directement `self._quantites`, le code extérieur pourrait
   le modifier et contourner nos vérifications.

Une propriété **sans setter** refuse l'affectation :

```python
try:
    stock.produits = {}
except AttributeError:
    print("On ne peut pas remplacer les produits de l'extérieur.")
```

### Étape 4 — Convention ou vraie protection ?

En Python, `_quantites` est une **politesse**, pas un cadenas : n'importe qui peut écrire `stock._quantites["Riz"] = -5`.
Python fait confiance aux programmeurs (« nous sommes tous des adultes consentants »). La vraie protection vient de
la discipline de l'équipe, de la revue de code et des tests.

## 4. ⚠️ Pièges courants

**Un dictionnaire défini dans le corps de la classe est partagé**

```python
class MauvaisStock:
    produits = []  # partagé entre toutes les instances


a, b = MauvaisStock(), MauvaisStock()
a.produits.append("Riz")
assert b.produits == ["Riz"]  # comportement indésirable constaté


class StockCorrige:
    def __init__(self):
        self.produits = []


a, b = StockCorrige(), StockCorrige()
a.produits.append("Riz")
assert b.produits == []
```

La règle d'or : **les données propres à chaque objet se créent dans `__init__`**, jamais dans le corps de la classe.

**Autres pièges**

- Retourner directement une collection interne : le code extérieur peut la modifier.
- Valider **après** avoir modifié : si une erreur survient, le stock est déjà abîmé. Toujours vérifier **avant**.
- Croire que `_nom` empêche l'accès : c'est une convention, pas une protection absolue.

## 5. À retenir

- **Composition** : un objet en contient d'autres (« a un »).
- **Encapsulation** : les données sont protégées par des méthodes qui vérifient les règles (les invariants).
- `_nom` = « usage interne » ; `@property` = lecture contrôlée ; renvoyer une **copie** protège l'état interne.
- Toujours **valider avant de modifier**.

## 6. Exercices

Complète les trois tâches dans [le fichier d'exercices](../exercices/ex02_composition.py), puis vérifie avec :

```powershell
python -m pytest parcours/p02_poo_et_conception/exercices/test_ex02_composition.py -v
```

Compare ensuite avec le [corrigé commenté](../solutions/sol02_composition.py).

## 7. Quiz

1. `Stock` doit-il hériter de `Produit` ?
2. Que signifie `_quantites` ?
3. Pourquoi vérifier avant de modifier ?
4. Où créer le dictionnaire de chaque stock ?
5. Une propriété sans setter accepte-t-elle une affectation ?

<details>
<summary>Réponses</summary>

1. Non : un stock *contient* des produits, il n'est pas un produit (composition).
2. Un détail interne, par convention : on n'y touche pas depuis l'extérieur.
3. Pour que l'objet reste valide même si l'opération échoue.
4. Dans `__init__`, pour que chaque instance ait le sien.
5. Non, elle lève `AttributeError`.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu sais maintenant construire un objet qui se protège lui-même. C'est la différence entre un code fragile et un code fiable.

💬 *Bloqué(e) ? C'est normal. Retape les exemples, essaie de les « casser » volontairement pour voir les erreurs, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 3.1 — Dataclasses et ventes immuables](l03_dataclasses.md).
<!-- /cadre:fin -->
