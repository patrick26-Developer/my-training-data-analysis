# Leçon 6.1 — Relier les objets, la console et les fichiers

⏱ Durée : 90 min · 🎯 Niveau : Intermédiaire · 📦 Prérequis : leçons 1.1 à 5.1, fichiers et JSON de P01

## 🎯 Ce que tu sauras faire

- Séparer le métier, la saisie et le stockage.
- Transformer des objets en valeurs JSON et les reconstruire.
- Préserver les données lorsqu'une opération échoue.
- Tester une évolution contre le comportement de P01.

## 1. Le problème (accroche)

La caisse fonctionne dans les tests. Mais Mama Nzoni doit fermer son ordinateur et
retrouver son stock demain. Il faut aussi gérer une quantité mal saisie sans fermer
la boutique et sans perdre les ventes précédentes.

## 2. L'idée en images

```text
main.py       -> modele.py       : opérations métier
main.py       -> stockage.py     : charger, sauvegarder, exporter
stockage.py   -> modele.py       : reconstruire des objets valides
modele.py                        : aucune dépendance à la console ou aux fichiers
```

Une responsabilité est une raison pour laquelle du code devra changer. Une nouvelle
règle de remise concerne le métier ; une nouvelle présentation concerne la console.
On garde des fonctions pour lire et écrire des fichiers : elles ne nécessitent pas
une classe simplement parce que le reste du projet utilise des objets.

## 3. Explication pas à pas

Depuis la racine du dépôt, cet exemple autonome construit des objets et les convertit
en dictionnaire. `asdict`, fourni par `dataclasses`, copie les champs de la dataclass.
JSON stocke des textes, nombres, listes et dictionnaires ; il ne sait pas reconstruire
une classe Python tout seul.

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

Le prix de cette vente est une copie. Changer le prix dans le stock ne changera pas
le ticket. La propriété `journal` retourne un tuple : on ne peut pas y ajouter une
vente depuis l'extérieur.

Dans `stockage.py`, `sauvegarder` convertit les produits et ventes en valeurs simples.
Un champ `version` distingue le format enregistré. `charger` appelle les constructeurs
pour reconstruire des objets. `Vente.__post_init__` est une méthode que dataclass
appelle après son initialisation : elle vérifie les champs et la cohérence du total.
Les annotations seules n'effectuent pas cette validation.

La sauvegarde écrit d'abord un fichier temporaire dans le même dossier puis remplace
l'ancien fichier. Un échec avant le remplacement conserve l'ancienne sauvegarde.
Un fichier absent démarre une boutique vide. Un fichier corrompu provoque une erreur
explicite : le programme évite de le remplacer silencieusement par une boutique vide.

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

Le menu convertit les textes saisis en nombres, puis demande aux objets d'effectuer
les opérations. Les objets restent responsables des règles : une autre interface
utiliserait exactement les mêmes validations. Seul le choix « q » sauvegarde les
changements ; une interruption peut perdre les opérations depuis le dernier lancement.
Cette petite application est locale, mono-utilisateur. Elle ne gère pas les écritures
simultanées de plusieurs caisses.

## 4. ⚠️ Pièges courants

Erreur avant correction, dans un exemple autonome :

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

Une sauvegarde n'est pas une validation métier : il faut encore vérifier les champs
au chargement. Une vente doit être construite avant de diminuer le stock ; ainsi,
une politique de remise invalide ne laisse pas une transaction à moitié appliquée.
Les nombres décimaux restent des `float`, comme en P01 : pour un logiciel financier
de production, choisir une représentation monétaire exacte et une règle d'arrondi.

## 5. À retenir

Le métier ne lit pas la console. Le stockage convertit des valeurs.
La reconstruction revalide les données. Une erreur ne doit pas effacer une sauvegarde.
Les tests de comparaison sécurisent une transformation sans changer les résultats attendus.

## 6. Exercices

Les trois exercices forment le [projet de synthèse](../projets/boutique_objets/README.md) :

1. Porter le noyau métier, puis faire passer les tests de comportement.
2. Ajouter la sauvegarde, le rechargement et l'export CSV ; vérifier un aller-retour.
3. Construire le menu et simuler une session comprenant une vente refusée.

Les corrigés sont `modele.py`, `stockage.py` et `main.py` dans ce dossier.
Les tests `test_modele.py` et `test_integration.py` vérifient automatiquement ces tâches.
Depuis la racine : `python -m pytest parcours/p02_poo_et_conception/projets -v`.

## 7. Quiz

1. Pourquoi garder le stockage hors de Produit ?
2. JSON peut-il directement enregistrer une instance quelconque ?
3. Quand __post_init__ est-il appelé ?
4. Pourquoi distinguer fichier absent et fichier corrompu ?
5. Les tests de comparaison prouvent-ils la qualité de la conception ?

<details>
<summary>Réponses</summary>

1. Un changement de format ne doit pas changer les règles du produit.
2. Non : convertir d'abord en valeurs simples.
3. Après l'initialisation générée par dataclass.
4. L'absence permet un premier lancement ; la corruption doit être signalée pour protéger les données.
5. Non : ils vérifient des comportements ; la conception demande aussi une relecture humaine.

</details>
