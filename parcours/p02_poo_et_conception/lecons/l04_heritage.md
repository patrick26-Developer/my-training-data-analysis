# Leçon 4.1 — Héritage et polymorphisme

⏱ Durée : 60 min · 🎯 Niveau : Débutant → Intermédiaire · 📦 Prérequis : leçon 3.1

## 🎯 Ce que tu sauras faire

- Spécialiser une méthode.
- Utiliser deux objets par le même contrat.
- Choisir entre héritage et composition.

## 1. Le problème (accroche)

Une boutique applique une remise, une autre aucune. La caisse doit pouvoir utiliser les deux règles avec le même appel.

## 2. L’idée en images

L’héritage permet à une classe enfant de spécialiser une classe parente. Le polymorphisme permet d’utiliser plusieurs objets par la même opération publique.

## 3. Explication pas à pas

```python
class SansRemise:
    def calculer(self, montant):
        return 0


class RemiseSeuil(SansRemise):
    def calculer(self, montant):
        if montant > 10000:
            return montant * 0.05
        return 0


for politique in (SansRemise(), RemiseSeuil()):
    print(politique.calculer(20000))  # 0 puis 1000.0
```

RemiseSeuil(SansRemise) déclare le parent. Redéfinir calculer remplace son comportement. Chaque politique accepte le même sous-total et retourne un montant de remise. Le contrat comprend aussi la promesse de ne pas modifier le stock. super() permettrait de réutiliser une méthode du parent ; ici ce serait inutile.

## 4. ⚠️ Pièges courants

Hériter seulement pour récupérer quelques lignes crée souvent une mauvaise relation. Une classe enfant doit conserver le contrat du parent. Python autorise aussi un objet sans parent commun s’il fournit calculer : c’est le duck typing.

Exemple autonome : constater le problème, puis le corriger.

```python
class MauvaisePolitique:
    def calculer(self):  # contrat incompatible avec calculer(montant)
        return 0


try:
    MauvaisePolitique().calculer(1000)
except TypeError as erreur:
    assert "positional argument" in str(erreur)


class PolitiqueCorrigee:
    def calculer(self, montant):
        return 0


assert PolitiqueCorrigee().calculer(1000) == 0
```

## 5. À retenir

Spécialiser une méthode. Utiliser deux objets par le même contrat. Choisir entre héritage et composition.

## 6. Exercices

Complète les trois tâches dans [le fichier d’exercices](../exercices/ex04_heritage.py).
Vérifie avec `python -m pytest parcours/p02_poo_et_conception/exercices/test_ex04_heritage.py -v`.
Puis compare au [corrigé commenté](../solutions/sol04_heritage.py).

## 7. Quiz

1. Quelle méthode est redéfinie ?
2. Faut-il tester le type dans la caisse ?
3. Quel est le seuil exact ?
4. Un parent commun est-il obligatoire en Python ?
5. Stock est-il une sorte de Produit ?

<details>
<summary>Réponses</summary>

1. calculer.
2. Non, appeler calculer suffit.
3. La remise s’applique strictement au-dessus de 10000.
4. Non, le comportement peut suffire.
5. Non, préférer la composition.

</details>
