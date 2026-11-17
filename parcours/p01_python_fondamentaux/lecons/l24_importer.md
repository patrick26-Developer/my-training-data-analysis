# Leçon 7.1 — Importer des modules

⏱ 40 min · 🎯 Débutant+ · 📦 Prérequis : module 6

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Python contient des milliers d'outils prêts à l'emploi : tu vas apprendre à aller les chercher.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Utiliser `import`, `from ... import`, `as`
- Explorer un module avec `dir()` et `help()`
- Éviter les imports qui masquent des noms

---

## 1. Le problème

Python ne met pas toutes ses fonctions à portée de main : il en range des milliers dans des **modules**
(des fichiers `.py` thématiques : mathématiques, dates, hasard…). Pour utiliser un outil, on **importe** le module qui
le contient. C'est comme aller chercher une clé à molette dans la bonne boîte à outils.

## 2. Pas à pas

### 2.1 `import module`

```python
import math

print(math.sqrt(16))  # 4.0
print(math.pi)  # 3.141592653589793
```

On écrit `module.nom` : on voit **d'où vient** chaque fonction. C'est la forme à privilégier.

### 2.2 `from module import nom`

```python
from math import sqrt, pi

print(sqrt(25), pi)
```

Pratique pour une ou deux fonctions utilisées souvent. Évite `from math import *` : on ne sait plus d'où vient
chaque nom, et des conflits sont possibles.

### 2.3 Alias avec `as`

```python
import datetime as dt
from collections import Counter as Compteur
```

Conventions : `import numpy as np`, `import pandas as pd` (tu les rencontreras en data).

### 2.4 Explorer un module

```python
import math
import random

print(dir(math))  # liste des noms disponibles
help(math.floor)  # documentation d'une fonction
print(random.__file__)  # où est le fichier du module ?
```

> 💡 Pourquoi `random` et pas `math` pour `__file__` ? Parce que certains modules (comme `math`) sont écrits
> en langage C, à l'intérieur de Python lui-même : ils n'ont pas de fichier `.py` à montrer.
> `random`, lui, est un vrai fichier Python que tu peux ouvrir et lire — très instructif !

### 2.5 Ce qu'est un module

**Un module est simplement un fichier `.py`.** Un **package** est un dossier contenant des modules
(et souvent un fichier `__init__.py`). Quand Python rencontre `import x`, il cherche `x` dans :

1. le dossier du script ;
2. la bibliothèque standard ;
3. les paquets installés (`site-packages`).

```python
import sys

print(sys.path)  # la liste des dossiers consultés
```

### 2.6 Le premier import gagne

Un module n'est **exécuté qu'une fois** : les imports suivants réutilisent la version déjà chargée.

## 3. ⚠️ Pièges courants

**Donner à son fichier le nom d'un module standard**

Un fichier `random.py` ou `math.py` dans ton dossier **masque** le vrai module :
```
AttributeError: partially initialized module 'random' has no attribute 'randint'
```
Choisis des noms de fichiers uniques (`mon_random.py`).

**Module introuvable**

```
ModuleNotFoundError: No module named 'requests'
```
Le paquet n'est pas installé : `pip install requests` (leçon 7.3).

**Import circulaire** : `a.py` importe `b.py` qui importe `a.py` : réorganise le code.

## 4. À retenir

- `import module` → `module.fonction()` ; `from module import fonction` ; `as` pour renommer.
- Un module = un fichier `.py` ; un package = un dossier de modules.
- `dir()` et `help()` pour explorer.
- Ne nomme jamais un fichier comme un module standard.

## 5. Exercices

Fichier : [`exercices/ex24_importer.py`](../exercices/ex24_importer.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex24_importer.py -v
```

## 6. Quiz

1. Quelle forme d'import rend le plus visible l'origine d'une fonction ?
2. Que fait `import numpy as np` ?
3. Que contient `sys.path` ?
4. Que se passe-t-il si on nomme un fichier `math.py` ?

<details>
<summary>Réponses</summary>

1. `import module`, puis `module.fonction()`.
2. Il importe `numpy` en lui donnant l'alias `np`.
3. La liste des dossiers où Python cherche les modules.
4. Il masque le vrai module `math`, ce qui provoque des erreurs.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu sais utiliser les modules : tu n'as plus besoin de tout réinventer.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 7.2 — La bibliothèque standard : un tour d'horizon](l25_bibliotheque_standard.md).
<!-- /cadre:fin -->
