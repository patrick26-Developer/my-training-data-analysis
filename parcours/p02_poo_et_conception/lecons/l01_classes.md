# Leçon 1.1 — Classes, instances et méthodes

⏱ Durée : 60 min · 🎯 Niveau : Débutant → Intermédiaire · 📦 Prérequis : P01

## 🎯 Ce que tu sauras faire

- Construire deux instances indépendantes.
- Lire et modifier un attribut.
- Appeler une méthode qui retourne un résultat.

## 1. Le problème (accroche)

La boutique répète les clés nom, prix et quantite dans chaque dictionnaire. Comment regrouper les données et leurs opérations ?

## 2. L’idée en images

Une classe est un modèle ; une instance est un objet construit avec ce modèle. Un attribut est une donnée de cet objet. Une méthode est une fonction attachée à la classe.

## 3. Explication pas à pas

```python
class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def valeur(self):
        return self.prix * self.quantite


riz = Produit("Riz", 800, 3)
print(riz.valeur())  # 2400
```

`__init__` initialise chaque nouvel objet. `self` désigne cet objet : Python le transmet quand on appelle `riz.valeur()`. Les trois affectations créent ses attributs. `valeur` retourne un calcul sans modifier le produit.

## 4. ⚠️ Pièges courants

Oublier self dans une méthode provoque un TypeError à son appel. Deux variables peuvent désigner le même objet : modifier cet objet est visible par les deux variables.

Exemple autonome : constater le problème, puis le corriger.

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

Construire deux instances indépendantes. Lire et modifier un attribut. Appeler une méthode qui retourne un résultat.

## 6. Exercices

Complète les trois tâches dans [le fichier d’exercices](../exercices/ex01_classes.py).
Vérifie avec `python -m pytest parcours/p02_poo_et_conception/exercices/test_ex01_classes.py -v`.
Puis compare au [corrigé commenté](../solutions/sol01_classes.py).

## 7. Quiz

1. Que représente self ?
2. Quand __init__ est-il appelé ?
3. Une classe est-elle une instance ?
4. Que retourne valeur pour un prix de 500 et une quantité de 4 ?
5. Deux noms peuvent-ils désigner le même objet ?

<details>
<summary>Réponses</summary>

1. L’instance courante.
2. Lors de la construction de l’instance.
3. Non : elle sert de modèle.
4. 2000.
5. Oui.

</details>
