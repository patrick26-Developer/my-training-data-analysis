# Leçon 3.2 — Des objets qui protègent leurs données

⏱ Durée : 60 min · 🎯 Niveau : intermédiaire · 📦 Prérequis : P02 et leçon 3.1

## 🔥 Une boutique qui refuse les prix impossibles

Un article à prix négatif fausse toutes les factures. Tu vas construire un objet qui
refuse cette valeur dès sa création, puis une collection que tu peux parcourir avec `for`.

## 🎯 Ce que tu sauras faire

- Valider un attribut avec une propriété.
- Définir un contrat avec une classe abstraite.
- Donner un sens à `len()`, à l'indexation et à `for` pour tes objets.
- Choisir entre composition et héritage.

## 1. Le problème

Avec un attribut public, chaque partie du programme doit penser à vérifier le prix.
Une **propriété** centralise cette vérification tout en gardant l'écriture `article.prix`.
Une **classe abstraite** précise les méthodes qu'une sous-classe devra fournir.

## 2. L'idée en images

Pense à un guichet : tu demandes une modification, le guichet vérifie les règles avant
de l'accepter. Ici, la propriété joue ce rôle. Le catalogue, lui, contient des articles :
c'est une composition, pas une relation d'héritage.

## 3. Pas à pas

### Étape 1 — Placer la validation au même endroit

```python
class Article:
    def __init__(self, nom: str, prix: int) -> None:
        self.nom = nom
        self.prix = prix

    @property
    def prix(self) -> int:
        return self._prix

    @prix.setter
    def prix(self, valeur: int) -> None:
        if valeur < 0:
            raise ValueError("Le prix doit être positif ou nul")
        self._prix = valeur


article = Article("Cahier", 1000)
article.prix = 1500
assert article.prix == 1500
```

`@property` transforme une méthode en lecture d'attribut. Le *setter* est la méthode
appelée lors de l'affectation. Le constructeur passe lui aussi par ce setter.
Le préfixe `_` signale un attribut interne par convention ; il ne bloque pas son accès.

### Étape 2 — Voir une erreur, puis vérifier que l'objet reste valide

```python
article.prix = -100
```
```
ValueError: Le prix doit être positif ou nul
```

```python
assert article.prix == 1500
```

La valeur précédente reste intacte : la validation précède l'affectation.

### Étape 3 — Exiger une méthode dans les sous-classes

```python
from abc import ABC, abstractmethod


class Paiement(ABC):
    @abstractmethod
    def payer(self, montant: int) -> str:
        """Retourne une confirmation de paiement."""
        raise NotImplementedError


class PaiementSimulation(Paiement):
    def payer(self, montant: int) -> str:
        if montant < 0:
            raise ValueError("Montant négatif")
        return f"Simulation : {montant} FCFA"


assert PaiementSimulation().payer(article.prix) == "Simulation : 1500 FCFA"
```

`ABC` et `@abstractmethod` empêchent de construire une classe qui n'implémente pas
toutes les méthodes abstraites. Cette simulation ne transfère aucun argent.
Un `Protocol`, vu en 3.1, permet un contrat sans imposer cet héritage ; choisis une
classe abstraite quand tu souhaites organiser explicitement une famille de classes.

### Étape 4 — Faire participer ton objet au langage

Les méthodes à deux tirets bas sont des **méthodes spéciales** : Python les appelle
pour des opérations précises. `__len__` sert à `len()`, `__getitem__` à l'accès par indice,
et `__iter__` à la boucle `for`.

```python
from collections.abc import Iterable, Iterator


class Catalogue:
    def __init__(self, articles: Iterable[Article]) -> None:
        self._articles = list(articles)

    def __len__(self) -> int:
        return len(self._articles)

    def __getitem__(self, indice: int) -> Article:
        return self._articles[indice]

    def __iter__(self) -> Iterator[Article]:
        return iter(self._articles)


catalogue = Catalogue([article, Article("Stylo", 500)])
assert len(catalogue) == 2
assert catalogue[0].nom == "Cahier"
assert [objet.nom for objet in catalogue] == ["Cahier", "Stylo"]
```

`Iterable[Article]` désigne une source parcourable d'articles. `Iterator[Article]`
désigne l'objet qui fournit les articles un à un. Nous approfondirons cette différence
en 3.4. Le catalogue copie la liste reçue, mais conserve les mêmes objets articles.

## 4. ⚠️ Pièges courants

- Écrire `self.prix = valeur` dans le setter le rappelle sans fin : cela produit un
  `RecursionError`. Écris `self._prix = valeur` après la validation.
- Construire `Paiement()` produit un `TypeError` : sa méthode abstraite manque.
- Un indice trop grand produit un `IndexError`, comme avec une liste.
- Le catalogue contient des articles ; en faire une sous-classe d'`Article` décrirait
  mal cette relation. Utilise la composition.

## 5. À retenir

Une propriété protège une règle à chaque affectation prévue par l'interface.
Une classe abstraite impose des méthodes aux sous-classes.
Les méthodes spéciales intègrent tes objets aux opérations Python.
La composition exprime « contient », l'héritage exprime « est un ».

## 6. Exercices — à toi de jouer

Ouvre [le fichier d'exercices](../exercices/ex02_poo_avancee.py).

1. Termine `Article` : refuse un prix négatif à la création et à la modification.
2. Termine `PaiementSimulation` en respectant le contrat de `Paiement`.
3. Termine `Catalogue` pour parcourir les articles et accéder aux indices négatifs.

Défi de 10 à 20 minutes : crée deux articles, modifie un prix, puis calcule le total
avec `sum(article.prix for article in catalogue)`. Vérifie qu'une modification invalide
ne change pas le total.

```powershell
python -m pytest parcours/p03_python_avance/exercices/test_ex02_poo_avancee.py -v
```

Compare ensuite avec [le corrigé commenté](../solutions/sol02_poo_avancee.py).

## 7. Quiz

1. Le préfixe `_` rend-il un attribut inaccessible ?
2. Pourquoi le constructeur affecte-t-il `self.prix` ?
3. Peut-on instancier `Paiement` directement ?
4. Quelle méthode Python appelle-t-il pour `len(catalogue)` ?
5. Le catalogue copie-t-il les articles eux-mêmes ?

<details>
<summary>Voir les réponses</summary>

1. Non, c'est une convention pour signaler un détail interne.
2. Pour utiliser la même validation que lors des modifications.
3. Non, sa méthode abstraite n'a pas d'implémentation concrète.
4. `__len__`.
5. Non. Il copie le conteneur, les objets articles restent partagés.

</details>

## 🎉 Bravo

Tu viens de protéger une règle métier et de rendre une collection utilisable avec
les opérations Python habituelles. En 3.3, tu découvriras comment adapter des fonctions
sans répéter leur logique.
