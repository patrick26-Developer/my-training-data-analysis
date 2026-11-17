# Leçon 3.1 — Dataclasses et ventes immuables

⏱ Durée : 60 min · 🎯 Niveau : Débutant → Intermédiaire · 📦 Prérequis : leçon 2.1

## 🎯 Ce que tu sauras faire

- Déclarer une dataclass.
- Comparer deux valeurs métier.
- Conserver un instantané indépendant du produit.

## 1. Le problème (accroche)

Le prix du riz change demain. La vente d’hier doit conserver son ancien prix. Comment enregistrer cet instantané ?

## 2. L’idée en images

Une dataclass génère des méthodes usuelles à partir de champs déclarés : initialisation, représentation et égalité. Un instantané copie les valeurs utiles à un moment donné.

## 3. Explication pas à pas

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
print(vente.total())  # 2400
print(vente == Vente("Riz", 800, 3))  # True
```

Les annotations nomment ici les champs : str pour du texte, float pour un nombre, int pour un entier. Elles ne vérifient pas les valeurs à l’exécution. dataclass fabrique __init__, __repr__ et __eq__. frozen=True empêche la réaffectation des champs. Copier le nom et le prix évite de conserver un lien vers le produit mutable.

## 4. ⚠️ Pièges courants

Modifier un champ gelé lève FrozenInstanceError. frozen=True ne rend pas immuable une liste contenue dans un champ. Pour une liste par instance, utiliser field(default_factory=list), jamais une liste partagée.

Exemple autonome : constater le problème, puis le corriger.

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

## 5. À retenir

Déclarer une dataclass. Comparer deux valeurs métier. Conserver un instantané indépendant du produit.

## 6. Exercices

Complète les trois tâches dans [le fichier d’exercices](../exercices/ex03_dataclasses.py).
Vérifie avec `python -m pytest parcours/p02_poo_et_conception/exercices/test_ex03_dataclasses.py -v`.
Puis compare au [corrigé commenté](../solutions/sol03_dataclasses.py).

## 7. Quiz

1. Que génère dataclass ?
2. Les annotations valident-elles un prix positif ?
3. Pourquoi copier le prix ?
4. frozen=True gèle-t-il une liste interne ?
5. Deux ventes de mêmes champs sont-elles égales ?

<details>
<summary>Réponses</summary>

1. Notamment __init__, __repr__ et __eq__.
2. Non, il faut une validation explicite.
3. Pour préserver le passé.
4. Non.
5. Oui, si elles ont la même classe.

</details>
