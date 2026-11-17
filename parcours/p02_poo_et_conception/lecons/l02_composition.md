# Leçon 2.1 — Composition et encapsulation

⏱ Durée : 60 min · 🎯 Niveau : Débutant → Intermédiaire · 📦 Prérequis : leçon 1.1

## 🎯 Ce que tu sauras faire

- Composer des objets.
- Protéger une quantité contre une modification invalide.
- Distinguer convention interne et protection absolue.

## 1. Le problème (accroche)

Une quantité négative fausse la valeur du magasin. Comment centraliser la règle et regrouper plusieurs produits ?

## 2. L’idée en images

La composition signifie qu’un objet contient d’autres objets. L’encapsulation regroupe les données avec les opérations qui protègent leurs règles, appelées invariants.

## 3. Explication pas à pas

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

Le dictionnaire est créé dans __init__ : chaque stock a le sien. Le préfixe _ indique une utilisation interne par convention ; Python ne bloque pas son accès. La méthode ajouter vérifie avant de modifier. Une propriété, définie avec @property, permet une lecture comme un attribut tout en contrôlant l’accès ; voir Produit dans le projet.

## 4. ⚠️ Pièges courants

Un dictionnaire défini directement dans le corps de la classe est partagé entre instances. Une propriété sans setter refuse une affectation avec AttributeError. Retourner directement une collection interne permet au code appelant de la modifier.

Exemple autonome : constater le problème, puis le corriger.

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

## 5. À retenir

Composer des objets. Protéger une quantité contre une modification invalide. Distinguer convention interne et protection absolue.

## 6. Exercices

Complète les trois tâches dans [le fichier d’exercices](../exercices/ex02_composition.py).
Vérifie avec `python -m pytest parcours/p02_poo_et_conception/exercices/test_ex02_composition.py -v`.
Puis compare au [corrigé commenté](../solutions/sol02_composition.py).

## 7. Quiz

1. Stock doit-il hériter de Produit ?
2. Que signifie _quantites ?
3. Pourquoi vérifier avant de modifier ?
4. Où créer le dictionnaire de chaque stock ?
5. Une propriété sans setter accepte-t-elle une affectation ?

<details>
<summary>Réponses</summary>

1. Non, il contient des produits.
2. Un détail interne par convention.
3. Pour conserver un état valide en cas d’erreur.
4. Dans __init__.
5. Non, elle lève AttributeError.

</details>
