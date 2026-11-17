# Leçon 5.1 — Stratégie et injection de dépendance

⏱ 60 min · 🎯 Débutant → Intermédiaire · 📦 Prérequis : leçon 4.1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Soldes de rentrée, promo du week-end, remise fidélité : tu vas apprendre à changer la règle de calcul **en une ligne**, sans toucher à la caisse. C'est le genre de conception qui évite les nuits blanches avant chaque promotion.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- **Déléguer** une règle qui change à un objet remplaçable (le pattern « Stratégie »)
- **Injecter** cet objet dans une classe par son constructeur
- Tester une caisse avec une règle de **remplacement** simple et prévisible
- Savoir quand une simple fonction suffit

---

## 1. Le problème

Chaque promotion oblige à rouvrir le code de la caisse :

```python
def total(montant, promotion):
    if promotion == "rentree":
        return montant * 0.9
    elif promotion == "weekend":
        return montant - 500
    elif promotion == "fidelite":
        ...
```

À chaque nouvelle règle : un `elif` de plus, un risque de plus de casser les anciennes. La caisse est fragilisée
par des changements qui ne la concernent pas. Comment **changer la règle sans réécrire le calcul de la caisse** ?

## 2. L'idée en images

Un **pattern** (patron de conception) est une solution éprouvée à un problème qui revient souvent. Ici :

- **Stratégie** : on confie la règle variable (la remise) à un **objet séparé** qui peut être remplacé.
- **Injection de dépendance** : au lieu que la caisse *fabrique* elle-même sa règle, on la lui **donne** de
  l'extérieur, à la construction.

```
   code qui assemble                  la caisse (stable)
 ┌─────────────────────┐          ┌──────────────────────────┐
 │ Caisse(RemiseFixe(500)) ─────► │ total(montant)           │
 └─────────────────────┘          │   → politique.calculer() │
                                    └──────────────────────────┘
```

La caisse ne change jamais. C'est l'assembleur (par exemple `main.py`) qui décide de la règle.

## 3. Pas à pas

### Étape 1 — Une caisse qui reçoit sa règle

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

- Le constructeur **reçoit** la politique au lieu de la créer : c'est l'injection.
- `total` **délègue** le calcul de la remise à la politique, puis soustrait.

### Étape 2 — Changer de règle sans toucher à la caisse

```python
class RemiseFixe:
    def __init__(self, montant):
        self.montant = montant

    def calculer(self, sous_total):
        return min(self.montant, sous_total)  # jamais plus que le total


caisse_promo = Caisse(RemiseFixe(500))
print(caisse_promo.total(20000))  # 19500
print(caisse_promo.total(300))  # 0   (la remise est plafonnée au sous-total)
```

Nouvelle promotion = **nouvelle classe**, et la classe `Caisse` reste exactement la même. Aucun risque de casser
les anciennes règles.

### Étape 3 — Une règle de remplacement pour tester

Pour vérifier que la caisse fonctionne, on n'a pas besoin des vraies règles compliquées : on fabrique une
règle **minuscule et prévisible**.

```python
class RemiseDeTest:
    def calculer(self, montant):
        return 100


caisse_test = Caisse(RemiseDeTest())
assert caisse_test.total(1000) == 900
```

L'injection rend les tests **simples et rapides** : on remplace une dépendance par un « double » de test.

### Étape 4 — Se protéger d'une règle défaillante

Une stratégie peut se tromper (une remise supérieure au montant, par exemple). La caisse doit donc **vérifier
le résultat de son collaborateur** :

```python
class Caisse:
    def __init__(self, politique):
        self.politique = politique

    def total(self, montant):
        remise = self.politique.calculer(montant)
        if not 0 <= remise <= montant:
            raise ValueError("Remise invalide.")
        return montant - remise
```

Et surtout : **valider avant de modifier quoi que ce soit** (comme le stock dans le projet). Si la remise est
invalide, rien ne doit avoir bougé.

### Étape 5 — Une fonction suffit parfois

Si la règle est simple et n'a **pas besoin de mémoriser un état**, une simple fonction fait l'affaire :

```python
def remise_weekend(montant):
    return 500


def total_avec(montant, regle):
    return montant - regle(montant)


print(total_avec(20000, remise_weekend))  # 19500
```

Inutile d'inventer des classes dès qu'une fonction convient. Les patterns sont des outils, pas une obligation :
choisis le plus simple qui fait le travail.

## 4. ⚠️ Pièges courants

**Une stratégie qui renvoie n'importe quoi**

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

**Autres pièges**

- Construire un « framework de patterns » pour une seule formule : c'est inutilement compliqué.
- Modifier le stock **avant** d'avoir validé la remise : en cas d'erreur, le stock reste abîmé.
- Créer la politique **dans** la caisse (`self.politique = RemiseSeuil()`) : on perd la souplesse de l'injection.

## 5. À retenir

- **Stratégie** : confier une règle variable à un objet remplaçable.
- **Injection** : fournir cet objet par le constructeur, depuis l'extérieur.
- Une règle de **remplacement** simple rend les tests faciles.
- Valider la remise puis préparer la vente **avant** de modifier le stock.
- Une simple **fonction** suffit pour une règle sans état.

## 6. Exercices

Complète les trois tâches dans [le fichier d'exercices](../exercices/ex05_patterns.py), puis vérifie avec :

```powershell
python -m pytest parcours/p02_poo_et_conception/exercices/test_ex05_patterns.py -v
```

Compare ensuite avec le [corrigé commenté](../solutions/sol05_patterns.py).

## 7. Quiz

1. Qui choisit la stratégie utilisée par la caisse ?
2. Quel appel la caisse utilise-t-elle sur la politique ?
3. Une fonction peut-elle suffire à la place d'une classe ?
4. Quand faut-il modifier le stock ?
5. Pourquoi tester une stratégie qui échoue ?

<details>
<summary>Réponses</summary>

1. Le code qui construit la caisse (l'assembleur), pas la caisse elle-même.
2. `politique.calculer(montant)`.
3. Oui, pour une règle simple sans état.
4. Après les validations et la préparation de la vente, jamais avant.
5. Pour vérifier qu'une erreur ne laisse pas de modification partielle (un stock à moitié modifié).

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu viens de découvrir ton premier pattern de conception. Tu peux désormais faire évoluer un programme sans le fragiliser : une compétence qui distingue les développeurs expérimentés.

💬 *Bloqué(e) ? C'est normal. Écris une `RemiseFidelite` de ton invention et branche-la sur la caisse, sans toucher à `Caisse`.*

**Prochaine étape :** [Leçon 6.1 — Intégrer la boutique](l06_integrer_la_boutique.md).
<!-- /cadre:fin -->
