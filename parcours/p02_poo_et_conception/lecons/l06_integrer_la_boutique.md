# Leçon 6.1 — Relier les objets, la console et les fichiers

⏱ 90 min · 🎯 Intermédiaire · 📦 Prérequis : leçons 1.1 à 5.1, fichiers et JSON de P01

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — C'est le moment où tout s'assemble : ta boutique en objets va **retenir** son stock d'un jour à l'autre, résister aux erreurs de saisie et passer les mêmes tests que ta version de P01. Un vrai petit logiciel, solide et organisé.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- **Séparer** le métier, la saisie à la console et le stockage dans des fichiers
- **Transformer** des objets en JSON, puis les **reconstruire** proprement
- **Protéger** les données quand une opération échoue
- **Prouver** qu'une évolution n'a rien cassé, en comparant avec le comportement de P01

---

## 1. Le problème

Les objets de P02 fonctionnent… dans les tests. Mais Mama Nzoni éteint son ordinateur le soir et veut retrouver
son stock le lendemain matin. Elle fait aussi des fautes de frappe : une quantité mal saisie ne doit pas fermer la
boutique, ni faire disparaître les ventes précédentes.

Trois questions se posent :

1. **Où** ranger le code qui lit le clavier ? Celui qui enregistre les fichiers ? Celui qui applique les règles ?
2. **Comment** sauvegarder des objets Python dans un fichier ?
3. **Comment** être sûr de ne rien avoir cassé par rapport à la version de P01 ?

## 2. L'idée en images

Le secret d'un projet qui reste agréable à faire évoluer : **chaque fichier a une seule raison de changer.**

```text
main.py       -> modele.py       : opérations métier
main.py       -> stockage.py     : charger, sauvegarder, exporter
stockage.py   -> modele.py       : reconstruire des objets valides
modele.py                        : aucune dépendance à la console ou aux fichiers
```

Une **responsabilité** est une raison de modifier un fichier :

- une nouvelle règle de remise → c'est du **métier** (`modele.py`) ;
- un nouveau format de fichier → c'est du **stockage** (`stockage.py`) ;
- un nouveau menu → c'est de la **présentation** (`main.py`).

Le métier ne sait pas qu'il existe une console, et la console ne connaît pas les détails des règles. Chacun
travaille de son côté.

> 💡 Les fonctions pour lire et écrire des fichiers restent de **simples fonctions** : pas besoin d'en faire une
> classe sous prétexte que le reste du projet utilise des objets. On choisit l'outil le plus simple qui convient.

## 3. Pas à pas

### Étape 1 — Faire une vente avec les objets

Ces exemples se lancent depuis la **racine du dépôt**. `asdict`, de `dataclasses`, transforme un objet dataclass en
dictionnaire (copie des champs).

```python
from dataclasses import asdict
from datetime import date
from parcours.p02_poo_et_conception.projets.boutique_objets.modele import Caisse, Produit, Stock

stock = Stock()
stock.ajouter(Produit("Riz", 800, 3))
caisse = Caisse(stock)
vente = caisse.vendre("Grâce", "riz", 2, date(2026, 1, 15))
assert asdict(vente)["total"] == 1600
assert stock.trouver("riz").quantite == 1
```

Deux choses à remarquer :

- Le prix de la vente est une **copie** : changer le prix dans le stock ne modifiera pas le ticket (c'est
  l'instantané de la leçon 3.1).
- La propriété `journal` renvoie un **tuple** : le code extérieur ne peut pas y ajouter de fausse vente.

### Étape 2 — Pourquoi JSON ne suffit pas à lui seul

JSON ne connaît que les textes, les nombres, les listes et les dictionnaires. Il **ne sait pas** reconstruire une
classe Python. Il faut donc :

1. à l'enregistrement : **convertir** les objets en valeurs simples ;
2. au chargement : **reconstruire** les objets en appelant les constructeurs.

C'est ce que font `sauvegarder` et `charger` dans `stockage.py`. Le fichier contient aussi un champ `version`, pour
reconnaître le format si on le change plus tard.

### Étape 3 — Revalider au chargement

Un fichier peut avoir été modifié à la main, abîmé ou écrit par une ancienne version. Les objets reconstruits
doivent donc **re-vérifier** leurs données : c'est le rôle de `Vente.__post_init__`, une méthode que `dataclass`
appelle juste après l'initialisation. Elle contrôle les champs et la cohérence du total. N'oublie pas que les
annotations (`prix: float`) seules ne valident rien !

### Étape 4 — Une sauvegarde qui ne détruit jamais l'ancienne

La sauvegarde écrit d'abord dans un **fichier temporaire** du même dossier, puis **remplace** l'ancien fichier.
Si quelque chose échoue avant le remplacement (coupure d'électricité, disque plein), l'ancienne sauvegarde est
encore là, intacte.

Autre décision importante :

- fichier **absent** → c'est un premier lancement : on démarre avec une boutique vide ;
- fichier **corrompu** → on signale une erreur claire, on ne le remplace **pas** silencieusement par une boutique
  vide (ce serait perdre toutes les données sans prévenir).

### Étape 5 — Un aller-retour complet

```python
from pathlib import Path
from tempfile import TemporaryDirectory
from parcours.p02_poo_et_conception.projets.boutique_objets.modele import Caisse, Produit, Stock
from parcours.p02_poo_et_conception.projets.boutique_objets.stockage import charger, sauvegarder

with TemporaryDirectory() as dossier:
    chemin = Path(dossier) / "boutique.json"
    stock = Stock()
    stock.ajouter(Produit("Manioc", 500, 10))
    sauvegarder(chemin, Caisse(stock))
    copie = charger(chemin)
    assert copie.stock.valeur() == 5000
```

On sauvegarde, on recharge, et on retrouve exactement la même valeur de stock : c'est le test de
l'« aller-retour ».

### Étape 6 — Le menu, simple chef d'orchestre

Le menu convertit les textes saisis en nombres, puis **demande aux objets** de faire le travail. Les règles restent
dans les objets : une autre interface (un site web, une application mobile) utiliserait exactement les mêmes
validations.

Précisions honnêtes sur cette petite application :

- seul le choix « q » sauvegarde : une interruption peut perdre les opérations faites depuis le dernier lancement ;
- elle est **locale et mono-utilisateur** : elle ne gère pas plusieurs caisses qui écrivent en même temps.

Savoir ce qu'un programme **ne fait pas** fait partie du métier !

## 4. ⚠️ Pièges courants

**Sauvegarder un objet directement en JSON**

```python
import json
from dataclasses import asdict, dataclass


@dataclass
class Ticket:
    total: int


ticket = Ticket(1600)
try:
    json.dumps(ticket)
except TypeError as erreur:
    assert "not JSON serializable" in str(erreur)

assert json.loads(json.dumps(asdict(ticket))) == {"total": 1600}
```

**Autres pièges**

- Une sauvegarde n'est **pas** une validation : il faut revérifier les champs au chargement.
- Construire la vente **avant** de diminuer le stock : si la remise est invalide, rien n'est à moitié appliqué.
- Les montants décimaux restent des `float`, comme en P01 : dans un vrai logiciel financier, on choisit une
  représentation monétaire exacte et une règle d'arrondi.

## 5. À retenir

- Le **métier** ne lit pas la console ; le **stockage** convertit des valeurs ; le **menu** orchestre.
- JSON ne sait pas reconstruire une classe : on convertit puis on reconstruit, en **revalidant**.
- Une erreur ne doit jamais effacer une bonne sauvegarde.
- Des **tests de comparaison** avec P01 sécurisent une transformation sans changer les résultats attendus.

## 6. Exercices

Les trois exercices forment le [projet de synthèse](../projets/boutique_objets/README.md) :

1. **Porter le noyau métier**, puis faire passer les tests de comportement.
2. **Ajouter la sauvegarde**, le rechargement et l'export CSV ; vérifier un aller-retour.
3. **Construire le menu** et simuler une session comprenant une vente refusée.

Les corrigés sont `modele.py`, `stockage.py` et `main.py` dans ce dossier. Les tests `test_modele.py` et
`test_integration.py` vérifient automatiquement ces tâches. Depuis la racine :

```powershell
python -m pytest parcours/p02_poo_et_conception/projets -v
```

## 7. Quiz

1. Pourquoi garder le stockage hors de `Produit` ?
2. JSON peut-il directement enregistrer une instance quelconque ?
3. Quand `__post_init__` est-il appelé ?
4. Pourquoi distinguer fichier absent et fichier corrompu ?
5. Les tests de comparaison prouvent-ils la qualité de la conception ?

<details>
<summary>Réponses</summary>

1. Un changement de format de fichier ne doit pas changer les règles du produit.
2. Non : il faut d'abord convertir l'objet en valeurs simples.
3. Juste après l'initialisation générée par `dataclass`.
4. L'absence permet un premier lancement ; la corruption doit être signalée pour protéger les données.
5. Non : ils vérifient des comportements ; la conception demande aussi une relecture humaine.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu as construit une application organisée, qui se souvient de ses données et résiste aux erreurs. C'est la forme d'un vrai projet professionnel, et tu viens de terminer l'essentiel du parcours P02.

💬 *Bloqué(e) ? C'est normal : l'intégration est la partie la plus exigeante. Avance une tâche à la fois et fais passer les tests un par un.*

**Prochaine étape :** passe l'[examen final](../examen_final.md) du parcours.
<!-- /cadre:fin -->
