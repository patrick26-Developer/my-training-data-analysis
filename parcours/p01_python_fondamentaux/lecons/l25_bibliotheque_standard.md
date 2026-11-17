# Leçon 7.2 — La bibliothèque standard : un tour d'horizon

⏱ 60 min · 🎯 Intermédiaire · 📦 Prérequis : leçon 7.1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Dates, hasard, statistiques, système : un tour d'horizon des trésors cachés de Python, sans rien installer.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Manipuler des **dates et heures** (`datetime`)
- Générer du **hasard** (`random`) et des statistiques simples (`statistics`)
- Compter et regrouper (`collections`)
- Combiner des itérables (`itertools`)
- Interagir avec le système (`os`, `sys`, `argparse`)

> Python est livré « piles incluses » : avant d'installer un paquet, regarde si la bibliothèque standard
> ne fait pas déjà le travail.

---

## 1. `datetime` — dates et heures

```python
from datetime import date, datetime, timedelta

aujourdhui = date.today()
print(aujourdhui)  # 2026-11-16
print(aujourdhui.year, aujourdhui.month, aujourdhui.day)
print(aujourdhui.strftime("%d/%m/%Y"))  # 16/11/2026
print(aujourdhui.strftime("%A"))  # jour de la semaine (en anglais par défaut)

independance = date(1960, 8, 15)  # indépendance du Congo
age_du_pays = aujourdhui - independance  # un timedelta
print(age_du_pays.days // 365)  # nombre d'années approximatif

dans_30_jours = aujourdhui + timedelta(days=30)
echeance = datetime.strptime("25/12/2026", "%d/%m/%Y").date()  # texte -> date
print((echeance - aujourdhui).days)
```

Codes de format : `%d` jour, `%m` mois, `%Y` année, `%H` heure, `%M` minute, `%S` seconde.

## 2. `random` — le hasard

```python
import random

random.randint(1, 6)  # un dé : entier entre 1 et 6 inclus
random.random()  # flottant entre 0 et 1
random.choice(["pile", "face"])  # un élément au hasard
random.sample(range(1, 50), 6)  # 6 nombres distincts (loto)
liste = [1, 2, 3, 4]
random.shuffle(liste)  # mélange en place
random.seed(42)  # résultats reproductibles
```

⚠️ `random` n'est **pas** sûr pour la sécurité (mots de passe, jetons) : utilise le module `secrets`.

```python
import secrets

mot_de_passe = secrets.token_urlsafe(12)
```

## 3. `statistics` — calculs statistiques

```python
import statistics

notes = [12, 15, 9, 18, 15]
print(statistics.mean(notes))  # moyenne : 13.8
print(statistics.median(notes))  # médiane : 15
print(statistics.mode(notes))  # valeur la plus fréquente : 15
print(statistics.stdev(notes))  # écart-type
```

## 4. `collections` — des conteneurs spécialisés

```python
from collections import Counter, defaultdict, deque

print(Counter("banane").most_common(2))  # [('a', 2), ('n', 2)]

regroupement = defaultdict(list)  # dictionnaire à valeur par défaut
for jour, montant in [("lun", 5), ("mar", 3), ("lun", 2)]:
    regroupement[jour].append(montant)
print(dict(regroupement))  # {'lun': [5, 2], 'mar': [3]}

file = deque([1, 2, 3])  # file efficace aux deux bouts
file.append(4)
file.popleft()  # 1
```

## 5. `itertools` — combiner des itérables

```python
from itertools import combinations, permutations, product, chain

print(list(combinations("ABC", 2)))  # [('A','B'), ('A','C'), ('B','C')]
print(list(permutations([1, 2, 3], 2)))  # arrangements ordonnés
print(list(product([0, 1], repeat=2)))  # [(0,0), (0,1), (1,0), (1,1)]
print(list(chain([1, 2], [3])))  # [1, 2, 3]
```

## 6. `os`, `sys`, `argparse` — le système

```python
import os, sys

print(os.name)  # 'nt' sous Windows, 'posix' sous Linux
print(os.environ.get("USERNAME"))  # variable d'environnement
print(sys.version)  # version de Python
print(sys.argv)  # arguments de la ligne de commande
```

`argparse` construit une interface de ligne de commande propre :

```python
import argparse

parser = argparse.ArgumentParser(description="Calcule un prix TTC")
parser.add_argument("prix", type=float, help="prix hors taxe")
parser.add_argument("--taux", type=float, default=18, help="taux de TVA (%%)")
args = parser.parse_args()
print(args.prix * (1 + args.taux / 100))
```

```powershell
python ttc.py 1000 --taux 5
```

## 7. Autres modules à connaître

| Module | Rôle |
|---|---|
| `math` | fonctions mathématiques |
| `decimal`, `fractions` | calculs exacts (argent, fractions) |
| `re` | expressions régulières |
| `string` | constantes (`ascii_letters`, `digits`) |
| `time` | pause (`time.sleep`), chronomètre (`time.perf_counter`) |
| `logging` | journal d'événements professionnel |
| `sqlite3` | base de données intégrée (parcours P05) |
| `urllib`, `http` | accès réseau de base |
| `shutil`, `tempfile`, `zipfile` | copie, fichiers temporaires, archives |
| `hashlib`, `secrets` | hachage, aléa sécurisé |
| `unittest`, `doctest` | tests |

Ressource officielle : <https://docs.python.org/fr/3/library/index.html>

## 8. ⚠️ Pièges courants

- `random` n'est pas fait pour la sécurité (voir `secrets`).
- `date.today()` dépend de l'horloge de l'ordinateur.
- `statistics.mode` sur des valeurs à égalité : renvoie la première rencontrée (Python 3.8+).
- `strptime` échoue (`ValueError`) si le texte ne correspond pas **exactement** au format.

## 9. À retenir

- La bibliothèque standard est vaste : cherche avant d'installer.
- `datetime` (dates), `random`/`secrets` (hasard), `statistics`, `collections`, `itertools`, `os`/`sys`/`argparse`.
- Consulte la documentation officielle en français.

## 10. Exercices

Fichier : [`exercices/ex25_bibliotheque_standard.py`](../exercices/ex25_bibliotheque_standard.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex25_bibliotheque_standard.py -v
```

## 11. Quiz

1. Quel module pour calculer la médiane ?
2. Comment obtenir la date de demain ?
3. Quel module utiliser pour générer un jeton de sécurité ?
4. Que fait `Counter("banane").most_common(1)` ?

<details>
<summary>Réponses</summary>

1. `statistics`.
2. `date.today() + timedelta(days=1)`
3. `secrets`.
4. `[('a', 2)]` : l'élément le plus fréquent avec son nombre d'apparitions.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu connais maintenant les principaux outils de la bibliothèque standard. Avant d'installer quoi que ce soit, tu sauras où chercher.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 7.3 — Environnements virtuels et `pip`](l26_venv_et_pip.md).
<!-- /cadre:fin -->
