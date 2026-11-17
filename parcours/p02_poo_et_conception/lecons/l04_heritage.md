# Leçon 4.1 — Héritage et polymorphisme

⏱ 60 min · 🎯 Débutant → Intermédiaire · 📦 Prérequis : leçon 3.1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Une boutique fait des remises, une autre non, une troisième offre un jour de promo… et ta caisse doit les gérer toutes avec **le même code**. C'est la magie du polymorphisme : une seule façon de demander, plusieurs façons de répondre.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- **Spécialiser** une classe existante grâce à l'héritage
- Utiliser plusieurs objets différents **avec le même appel** (le polymorphisme)
- Reconnaître un **contrat** entre une classe et ceux qui l'utilisent
- Choisir avec discernement entre **héritage** et **composition**

---

## 1. Le problème

La caisse doit calculer une remise. Selon la boutique :

- une boutique n'accorde **aucune** remise ;
- une autre accorde **5 %** au-dessus de 10 000 FCFA.

Première idée (mauvaise) : un gros `if` dans la caisse qui teste le type de boutique. À chaque nouvelle règle,
on rouvre la caisse, on risque de tout casser. Existe-t-il une façon de **brancher** n'importe quelle règle de
remise, sans toucher à la caisse ?

## 2. L'idée en images

Imagine une prise électrique : peu importe l'appareil (lampe, ventilateur, chargeur), il suffit qu'il ait la bonne
fiche. De même, la caisse n'a besoin que d'une chose : un objet qui sache répondre à `calculer(montant)`.

```
          ┌─────────────┐
          │ SansRemise  │ ◄──── la règle de base : calculer(montant) → 0
          └──────┬──────┘
                 │ hérite de
          ┌──────┴──────┐
          │ RemiseSeuil │      redéfinit calculer(montant) → 5 % au-dessus de 10 000
          └─────────────┘
```

- **Héritage** : une classe *enfant* reprend tout ce que fait sa classe *parent*, et peut **redéfinir** certaines
  méthodes. On dit « un `RemiseSeuil` **est une sorte de** `SansRemise` ».
- **Polymorphisme** : « plusieurs formes ». On appelle la même méthode sur des objets différents, et chacun
  répond à sa façon.
- **Contrat** : ce que tout le monde s'engage à respecter (même nom de méthode, mêmes paramètres, même type de
  résultat).

## 3. Pas à pas

### Étape 1 — La règle de base

```python
class SansRemise:
    def calculer(self, montant):
        return 0
```

### Étape 2 — Une règle plus riche, par héritage

```python
class RemiseSeuil(SansRemise):
    def calculer(self, montant):
        if montant > 10000:
            return montant * 0.05
        return 0
```

`class RemiseSeuil(SansRemise):` : les parenthèses indiquent le **parent**. En redéfinissant `calculer`, l'enfant
remplace le comportement du parent, mais **garde la même signature** : même nom, même paramètre `montant`.

### Étape 3 — Le polymorphisme en action

```python
for politique in (SansRemise(), RemiseSeuil()):
    print(politique.calculer(20000))  # 0 puis 1000.0
```

La boucle ne se demande **jamais** « quel type d'objet est-ce ? ». Elle appelle `calculer` et chaque objet fait
ce qui lui convient. C'est le polymorphisme.

### Étape 4 — Une fonction qui accepte toutes les règles

```python
def total_net(montant, politique):
    return montant - politique.calculer(montant)


print(total_net(20000, SansRemise()))  # 20000
print(total_net(20000, RemiseSeuil()))  # 19000.0
```

`total_net` ne sait pas — et n'a pas besoin de savoir — quelle règle elle reçoit. Si demain on invente
`RemiseFidelite`, `total_net` fonctionnera **sans changer**. On a *ouvert* le programme aux nouveautés sans le
*modifier* : c'est un principe central de la bonne conception.

### Étape 5 — Réutiliser le parent avec `super()`

Quand l'enfant veut **compléter** le parent plutôt que le remplacer, il appelle `super()` :

```python
class RemiseWeekend(RemiseSeuil):
    def calculer(self, montant):
        remise_de_base = super().calculer(montant)  # on réutilise la règle du parent
        return remise_de_base + 100  # on ajoute 100 FCFA
```

Dans notre exemple de base, `super()` ne servait pas ; mais tu le rencontreras souvent.

## 4. Héritage ou composition ?

> Règle d'or : **hérite seulement si la phrase « est une sorte de » est vraie ET que l'enfant respecte tout le
> contrat du parent.**

| Situation | Bon choix |
|---|---|
| `RemiseSeuil` **est une sorte de** règle de remise | héritage |
| un `Stock` **contient** des produits | composition (leçon 2.1) |
| je veux juste réutiliser quelques lignes d'une autre classe | composition ou fonction |

En Python, l'héritage n'est même pas obligatoire pour le polymorphisme : un objet qui possède une méthode
`calculer(montant)` convient, qu'il ait un parent commun ou non. On appelle cela le **duck typing**
(« s'il marche comme un canard et cancane comme un canard, c'est un canard »).

## 5. ⚠️ Pièges courants

**Une classe enfant qui casse le contrat**

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

**Autres pièges**

- Hériter uniquement pour récupérer quelques lignes : on crée une relation « est une sorte de » **fausse**.
  Un `Stock` n'est pas un `Produit` !
- Tester le type avec `isinstance` partout dans la caisse : on perd tout l'intérêt du polymorphisme.
- Chaînes d'héritage trop longues (parent → enfant → petit-enfant → …) : le code devient difficile à suivre.

## 6. À retenir

- **Héritage** : `class Enfant(Parent):` ; l'enfant peut redéfinir des méthodes.
- **Polymorphisme** : même appel, comportements différents selon l'objet.
- Respecte le **contrat** (mêmes noms, mêmes paramètres, mêmes promesses).
- Teste « est une sorte de » avant d'hériter ; sinon préfère la **composition**.
- `super()` réutilise la méthode du parent.

## 7. Exercices

Complète les trois tâches dans [le fichier d'exercices](../exercices/ex04_heritage.py), puis vérifie avec :

```powershell
python -m pytest parcours/p02_poo_et_conception/exercices/test_ex04_heritage.py -v
```

Compare ensuite avec le [corrigé commenté](../solutions/sol04_heritage.py).

## 8. Quiz

1. Quelle méthode est redéfinie par `RemiseSeuil` ?
2. Faut-il tester le type de la politique dans la caisse ?
3. Quel est le seuil exact de la remise ?
4. Un parent commun est-il obligatoire en Python pour le polymorphisme ?
5. `Stock` est-il une sorte de `Produit` ?

<details>
<summary>Réponses</summary>

1. `calculer`.
2. Non : appeler `calculer` suffit, c'est tout l'intérêt du polymorphisme.
3. La remise s'applique **strictement au-dessus** de 10 000 FCFA (10 000 exactement : pas de remise).
4. Non : un objet qui possède la bonne méthode convient (duck typing).
5. Non : un stock *contient* des produits ; on préfère la composition.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu sais écrire du code qui accepte des règles différentes sans jamais être modifié. C'est l'une des idées les plus puissantes de la programmation.

💬 *Bloqué(e) ? C'est normal : le polymorphisme se comprend en l'essayant. Écris une troisième règle de remise de ton invention et branche-la sur `total_net`.*

**Prochaine étape :** [Leçon 5.1 — Stratégie et injection de dépendance](l05_patterns.md).
<!-- /cadre:fin -->
