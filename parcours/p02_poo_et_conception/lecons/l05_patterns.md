# Leçon 5.1 — Stratégie et injection de dépendance

⏱ Durée : 60 min · 🎯 Niveau : Débutant → Intermédiaire · 📦 Prérequis : leçon 4.1

## 🎯 Ce que tu sauras faire

- Déléguer une règle variable.
- Injecter un objet dans un constructeur.
- Tester une caisse avec une politique de remplacement.

## 1. Le problème (accroche)

Modifier la caisse à chaque nouvelle promotion fragilise les ventes. Comment changer la règle sans réécrire le calcul de la caisse ?

## 2. L’idée en images

Un pattern est une solution récurrente à un problème de conception. Stratégie signifie confier un calcul variable à un objet remplaçable. L’injection consiste à fournir cet objet depuis l’extérieur.

## 3. Explication pas à pas

```python
class SansRemise:
    def calculer(self, montant):
        return 0


class Caisse:
    def __init__(self, politique):
        self.politique = politique

    def total(self, montant):
        return montant - self.politique.calculer(montant)


caisse = Caisse(SansRemise())
print(caisse.total(20000))  # 20000
```

Le constructeur reçoit la politique au lieu de la créer. total lui délègue le calcul de la remise. Un test peut fournir une petite politique prévisible. Le projet ajoute ensuite le stock et le journal. Une fonction passée en paramètre serait suffisante si la règle ne nécessite aucun état : les classes restent un choix à justifier.

## 4. ⚠️ Pièges courants

Inventer un framework de patterns pour une seule formule complique la lecture. Une stratégie qui lève une erreur ne doit pas laisser un stock déjà diminué. Valider la remise et préparer la vente avant de modifier le stock.

Exemple autonome : constater le problème, puis le corriger.

```python
class Politique:
    def calculer(self, montant):
        return montant + 1  # erreur : dépasse le sous-total


montant = 500
remise = Politique().calculer(montant)
try:
    if not 0 <= remise <= montant:
        raise ValueError("Remise invalide.")
except ValueError as erreur:
    assert str(erreur) == "Remise invalide."


class PolitiqueCorrigee:
    def calculer(self, montant):
        return min(100, montant)


assert montant - PolitiqueCorrigee().calculer(montant) == 400
```

## 5. À retenir

Déléguer une règle variable. Injecter un objet dans un constructeur. Tester une caisse avec une politique de remplacement.

## 6. Exercices

Complète les trois tâches dans [le fichier d’exercices](../exercices/ex05_patterns.py).
Vérifie avec `python -m pytest parcours/p02_poo_et_conception/exercices/test_ex05_patterns.py -v`.
Puis compare au [corrigé commenté](../solutions/sol05_patterns.py).

## 7. Quiz

1. Qui choisit la stratégie ?
2. Quel appel utilise la caisse ?
3. Une fonction peut-elle suffire ?
4. Quand modifier le stock ?
5. Pourquoi tester une stratégie qui échoue ?

<details>
<summary>Réponses</summary>

1. Le code qui construit la caisse.
2. politique.calculer(montant).
3. Oui, pour une règle simple.
4. Après les validations et la préparation de la vente.
5. Pour vérifier l’absence de modification partielle.

</details>
