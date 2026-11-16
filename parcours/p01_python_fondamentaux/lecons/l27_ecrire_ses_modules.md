# Leçon 7.4 — Écrire ses propres modules et packages

⏱ 50 min · 🎯 Intermédiaire · 📦 Prérequis : leçons 7.1 à 7.3

## 🎯 Ce que tu sauras faire

- Découper un programme en plusieurs fichiers
- Utiliser `if __name__ == "__main__":`
- Créer un **package** (dossier avec `__init__.py`)
- Choisir entre imports absolus et relatifs

---

## 1. Le problème

Ton programme de boutique dépasse 500 lignes dans un seul fichier. Impossible de s'y retrouver, et ton collègue
ne peut pas réutiliser ton calcul de TVA sans copier-coller. La solution : **découper en modules**, chacun ayant
une responsabilité claire.

## 2. L'idée en images

```
boutique/
├── main.py            ← point d'entrée : lit les saisies
├── calculs.py         ← prix, TVA, remises
├── stock.py           ← gestion du stock
└── affichage.py       ← mise en forme des reçus
```

## 3. Pas à pas

### 3.1 Un module = un fichier

`calculs.py` :

```python
TVA = 18


def prix_ttc(prix_ht):
    return prix_ht * (1 + TVA / 100)
```

`main.py` (dans le même dossier) :

```python
import calculs
from calculs import prix_ttc

print(calculs.TVA)
print(prix_ttc(1000))
```

### 3.2 `if __name__ == "__main__":`

Quand on **exécute** un fichier, Python met `__name__` à `"__main__"`. Quand on l'**importe**, `__name__`
vaut le nom du module. Ce test sépare le « code réutilisable » du « programme principal » :

```python
def prix_ttc(prix_ht):
    return prix_ht * 1.18


def main():
    print(prix_ttc(1000))


if __name__ == "__main__":
    main()
```

- `python calculs.py` → `main()` s'exécute ;
- `import calculs` → rien ne s'exécute : on importe seulement les fonctions.

**Toujours** écrire le programme principal dans une fonction `main()` appelée sous ce test.

### 3.3 Un package : un dossier de modules

```
boutique/
├── __init__.py
├── calculs.py
└── stock.py
main.py
```

```python
# main.py
from boutique import calculs
from boutique.stock import ajouter
```

`__init__.py` (peut être vide) marque le dossier comme package. On peut y exposer l'API publique :

```python
# boutique/__init__.py
from .calculs import prix_ttc

__all__ = ["prix_ttc"]
```

Alors : `from boutique import prix_ttc`.

### 3.4 Imports absolus et relatifs

Dans un package :

```python
# boutique/stock.py
from boutique.calculs import prix_ttc  # absolu (recommandé)
from .calculs import prix_ttc  # relatif (même package)
```

### 3.5 Exécuter un package

```powershell
python -m boutique.main      # exécute le module boutique/main.py correctement
```

Un fichier `__main__.py` dans le package permet `python -m boutique`.

### 3.6 Bonnes pratiques

- Un module = **une responsabilité** (calculs, stockage, affichage).
- Noms de modules : minuscules, `_` si besoin ; pas de tirets.
- Évite les imports circulaires : fais dépendre les modules « du haut » de ceux « du bas », jamais l'inverse.
- Pas de code qui s'exécute à l'import (en dehors des définitions).
- Utilise des constantes en MAJUSCULES pour les réglages.

### 3.7 Documenter un module

```python
"""Calculs de prix : TVA, remises et conversions de devises."""
```

Cette docstring en tête de fichier apparaît dans `help(calculs)`.

## 4. ⚠️ Pièges courants

**`ModuleNotFoundError`** en lançant un fichier depuis un sous-dossier : lance le programme **depuis la racine**
avec `python -m paquet.module`.

**Oublier `__init__.py`** : fonctionne parfois (paquets « namespace »), mais crée des surprises : mets-le.

**Code exécuté à l'import** (`input()` au niveau du module) : le simple `import` bloque le programme.

**Import circulaire** : `ImportError: cannot import name ... (most likely due to a circular import)`.

## 5. À retenir

- Découpe en modules ; chaque fichier `.py` est importable.
- `if __name__ == "__main__": main()` : séparer réutilisable et exécutable.
- Package = dossier + `__init__.py`.
- Lance avec `python -m paquet.module` depuis la racine.

## 6. Exercices

Fichier : [`exercices/ex27_ecrire_ses_modules.py`](../exercices/ex27_ecrire_ses_modules.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex27_ecrire_ses_modules.py -v
```

## 7. Mini-projet du module 7 — Boîte à outils

Crée un package `outils` contenant `maths.py`, `textes.py` et `dates.py` (fonctions réutilisables), un
`__init__.py` qui expose l'API, et un `main.py` qui les utilise. Lance-le avec `python -m outils.main`.
Une version de référence est dans [`../projets/m7_boite_a_outils/`](../projets/m7_boite_a_outils/).

## 8. Quiz

1. Que vaut `__name__` quand on exécute directement un fichier ?
2. Que contient `__init__.py` ?
3. Pourquoi mettre le programme principal dans `main()` ?
4. Comment exécuter le module `boutique/main.py` ?

<details>
<summary>Réponses</summary>

1. `"__main__"`.
2. Il peut être vide, ou exposer l'API publique du package.
3. Pour que l'import du module n'exécute pas le programme et que le code reste testable.
4. `python -m boutique.main`, depuis la racine du projet.

</details>
