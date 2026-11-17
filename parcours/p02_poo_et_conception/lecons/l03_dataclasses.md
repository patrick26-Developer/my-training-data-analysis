# Leçon 3.1 — Dataclasses et ventes immuables

⏱ 60 min · 🎯 Débutant → Intermédiaire · 📦 Prérequis : leçon 2.1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Écrire une classe de données demande beaucoup de code répétitif… sauf avec `@dataclass` : trois lignes, et Python fabrique le reste. Tu vas aussi apprendre à garder la trace du passé : le prix d'hier ne changera jamais.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Déclarer une **dataclass** en quelques lignes
- Comparer deux objets « de valeur » avec `==`
- Rendre un objet **immuable** (« gelé ») avec `frozen=True`
- Garder un **instantané** d'une vente qui ne change plus jamais

---

## 1. Le problème

Mardi, le kilo de riz coûte 800 FCFA. Mama Nzoni enregistre une vente. Mercredi, le prix passe à 900 FCFA.
Si la vente de mardi *pointe* encore vers le produit, elle affichera 900 FCFA : l'**historique est faussé** !

Il faut donc **photographier** la vente au moment où elle a lieu : copier le nom, le prix, la quantité, et ne
plus jamais les modifier. Cette « photo » est un **instantané**.

Et pour représenter simplement ce genre de petit objet de données, Python a une aide précieuse : `@dataclass`.

## 2. L'idée en images

Une classe « ordinaire » qui ne fait que porter des données demande beaucoup d'écriture :

```python
class VenteLongue:
    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return (
            f"VenteLongue(produit={self.produit!r}, prix={self.prix!r}, quantite={self.quantite!r})"
        )

    def __eq__(self, autre):
        return (self.produit, self.prix, self.quantite) == (
            autre.produit,
            autre.prix,
            autre.quantite,
        )
```

Avec `@dataclass`, on **déclare seulement les champs** et Python écrit tout cela à notre place :
l'initialisation, l'affichage lisible et la comparaison.

## 3. Pas à pas

### Étape 1 — Déclarer la dataclass

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Vente:
    produit: str
    prix: float
    quantite: int

    def total(self):
        return self.prix * self.quantite


vente = Vente("Riz", 800, 3)
print(vente)  # Vente(produit='Riz', prix=800, quantite=3)
print(vente.total())  # 2400
```

Ce qui se passe :

- `@dataclass` est un **décorateur** : il transforme la classe en y ajoutant des méthodes toutes prêtes.
- Les lignes `produit: str` sont des **annotations** : elles nomment les champs et indiquent le type attendu
  (`str` texte, `float` nombre décimal, `int` entier).
- ⚠️ Python **ne vérifie pas** ces types à l'exécution. `Vente("Riz", "beaucoup", 3)` ne protestera pas. Les
  annotations servent à documenter et aux outils comme `mypy` (vu en P03). Pour valider, il faut écrire du code.
- Tu peux ajouter des **méthodes ordinaires** (ici `total`) comme dans n'importe quelle classe.

### Étape 2 — Comparer des valeurs

```python
print(vente == Vente("Riz", 800, 3))  # True
print(vente == Vente("Riz", 900, 3))  # False
```

Deux ventes sont **égales** quand elles ont **le même type et les mêmes champs**. C'est ce qu'on attend d'une
« valeur » (comme deux billets de 1000 FCFA : ils sont équivalents).

### Étape 3 — Geler l'objet avec `frozen=True`

```python
from dataclasses import FrozenInstanceError

try:
    vente.prix = 1
except FrozenInstanceError:
    print("Impossible de modifier une vente gelée.")
```

Une vente gelée est **immuable** : on ne peut plus changer ses champs. Pour « modifier » une vente, on en crée
une **nouvelle**. Pratique pour un historique : ce qui est passé reste passé.

### Étape 4 — Prendre un instantané

Voici comment transformer un produit en vente, en **copiant** les valeurs :

```python
produit = {"nom": "Riz", "prix": 800, "quantite": 3}


def creer_vente(produit):
    return Vente(produit["nom"], produit["prix"], produit["quantite"])


vente = creer_vente(produit)
produit["prix"] = 900  # le prix change demain…
print(vente.prix)  # 800  → la vente d'hier est intacte
```

Comme `Vente` reçoit des **valeurs simples** (un texte, deux nombres), elle ne garde aucun lien avec le dictionnaire
d'origine. C'est exactement l'instantané voulu.

### Étape 5 — Une liste dans une dataclass ? Attention

```python
from dataclasses import field


@dataclass
class Panier:
    client: str
    articles: list = field(default_factory=list)  # une NOUVELLE liste pour chaque panier


p1, p2 = Panier("Grâce"), Panier("Jean")
p1.articles.append("Riz")
print(p2.articles)  # []
```

`field(default_factory=list)` crée une liste vide **par instance**. Écrire `articles: list = []` est interdit : ce
serait la même liste partagée par tous (Python le refuse d'ailleurs avec une erreur).

## 4. ⚠️ Pièges courants

**Modifier un champ gelé**

```python
from dataclasses import FrozenInstanceError, dataclass


@dataclass(frozen=True)
class Ticket:
    prix: int


ticket = Ticket(500)
try:
    ticket.prix = 600
except FrozenInstanceError as erreur:
    assert "cannot assign" in str(erreur)

nouveau_ticket = Ticket(600)  # créer une nouvelle valeur
assert ticket.prix == 500
assert nouveau_ticket.prix == 600
```

**Croire que `frozen=True` gèle aussi les listes contenues**

`frozen=True` empêche de **ré-affecter** un champ, mais si le champ contient une liste, on peut toujours faire
`vente.articles.append(...)`. L'immuabilité est **superficielle**.

**Compter sur les annotations pour valider**

`prix: float` n'empêche pas `prix=-5`. Pour refuser une valeur invalide, il faut un contrôle explicite
(par exemple dans `__post_init__`, la méthode appelée juste après la création).

## 5. À retenir

- `@dataclass` génère `__init__`, `__repr__` et `__eq__` à partir des champs déclarés.
- `frozen=True` rend l'objet immuable (en surface).
- Les annotations **ne valident pas** les valeurs.
- Un **instantané** copie des valeurs simples pour préserver le passé.
- `field(default_factory=list)` pour une liste propre à chaque objet.

## 6. Exercices

Complète les trois tâches dans [le fichier d'exercices](../exercices/ex03_dataclasses.py), puis vérifie avec :

```powershell
python -m pytest parcours/p02_poo_et_conception/exercices/test_ex03_dataclasses.py -v
```

Compare ensuite avec le [corrigé commenté](../solutions/sol03_dataclasses.py).

## 7. Quiz

1. Que génère `@dataclass` ?
2. Les annotations valident-elles qu'un prix est positif ?
3. Pourquoi copier le prix dans la vente ?
4. `frozen=True` gèle-t-il une liste interne ?
5. Deux ventes avec les mêmes champs sont-elles égales ?

<details>
<summary>Réponses</summary>

1. Notamment `__init__`, `__repr__` et `__eq__`.
2. Non : il faut une validation explicite.
3. Pour préserver le passé, même si le prix du produit change ensuite.
4. Non : seule la ré-affectation des champs est bloquée.
5. Oui, si elles sont de la même classe et ont les mêmes valeurs.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu sais décrire des données en quelques lignes et garder un historique fiable. Tu viens d'ajouter un outil très apprécié des développeurs Python à ta boîte à outils.

💬 *Bloqué(e) ? C'est normal. Retape les exemples, essaie de modifier une vente gelée pour voir l'erreur, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 4.1 — Héritage et polymorphisme](l04_heritage.md).
<!-- /cadre:fin -->
