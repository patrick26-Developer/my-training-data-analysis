# Leçon 10.4 — Documenter son code

⏱ 45 min · 🎯 Intermédiaire · 📦 Prérequis : leçon 10.3

## 🎯 Ce que tu sauras faire

- Écrire de bonnes **docstrings** (fonctions, modules)
- Ajouter des exemples **testables** avec `doctest`
- Rédiger un **README** utile
- Générer une aide en ligne de commande avec `argparse`

---

## 1. Le problème

Dans six mois, tu ne te souviendras plus de ce que fait ta fonction `calc2()`. Un collègue non plus. Une bonne
documentation répond à trois questions : **à quoi ça sert ? comment l'utiliser ? que faut-il savoir ?**

## 2. Pas à pas

### 2.1 La docstring

Une **docstring** est le texte entre triples guillemets placé **juste sous** le `def` (ou en tête d'un fichier).
Elle est accessible avec `help(fonction)` et `fonction.__doc__`.

```python
def prix_ttc(prix_ht, taux=18):
    """Retourne le prix TTC.

    Args:
        prix_ht: prix hors taxe, en FCFA.
        taux: taux de TVA en pourcentage (18 par défaut).

    Returns:
        Le prix toutes taxes comprises.

    Raises:
        ValueError: si prix_ht est négatif.
    """
    if prix_ht < 0:
        raise ValueError("prix_ht doit être positif")
    return prix_ht * (1 + taux / 100)
```

Structure recommandée (style « Google ») :
1. **Une ligne de résumé** à l'impératif/présent, terminée par un point ;
2. une ligne vide, puis le détail (facultatif) ;
3. `Args`, `Returns`, `Raises`, éventuellement `Example`.

Docstring courte pour une fonction évidente : `"""Retourne le carré de x."""`

### 2.2 Documenter un module et une classe

```python
"""Calculs de prix : TVA, remises et conversions de devises."""
```

La docstring d'un module se place **tout en haut** du fichier ; celle d'une classe, juste sous `class`.

### 2.3 Les exemples avec `doctest`

On peut écrire des exemples **dans** la docstring ; Python les exécute et vérifie le résultat !

```python
def est_pair(n):
    """Retourne True si n est pair.

    >>> est_pair(4)
    True
    >>> est_pair(7)
    False
    """
    return n % 2 == 0
```

Lancer la vérification :

```powershell
python -m doctest -v mon_fichier.py
```

Ou avec pytest : `python -m pytest --doctest-modules`.

Avantage : la documentation **ne peut plus mentir**, puisqu'elle est testée.

### 2.4 Les commentaires `#` : quand ?

- Pour expliquer un **pourquoi** non évident, une astuce, un piège, une référence ;
- `# TODO:` pour ce qui reste à faire ; `# FIXME:` pour un bug connu.
- **Pas** pour répéter le code.

### 2.5 Les annotations de type, une documentation vérifiable

```python
def moyenne(notes: list[float]) -> float: ...
```

Elles complètent la docstring (on évite de répéter les types).

### 2.6 Le README : la porte d'entrée du projet

Un bon `README.md` contient :

```markdown
# Nom du projet
Une phrase : à quoi ça sert.

## Installation
python -m venv venv ; pip install -r requirements.txt

## Utilisation
python -m boutique --help   (exemple concret)

## Tests
python -m pytest

## Structure
boutique/ ... (rôle de chaque dossier)

## Licence / Auteur
```

Format **Markdown** : `#` titres, `**gras**`, `` `code` ``, listes avec `-`, blocs de code entre triples accents graves.

### 2.7 Aide en ligne de commande avec `argparse`

```python
import argparse

parser = argparse.ArgumentParser(description="Calcule un prix TTC.")
parser.add_argument("prix", type=float, help="prix hors taxe en FCFA")
parser.add_argument("--taux", type=float, default=18, help="taux de TVA (%%, défaut 18)")
args = parser.parse_args()
print(args.prix * (1 + args.taux / 100))
```

```powershell
python ttc.py --help
python ttc.py 1000 --taux 5
```

`--help` est généré automatiquement à partir de tes descriptions.

### 2.8 Documentation générée

Pour de plus gros projets, des outils (**MkDocs**, **Sphinx**, `pdoc`) transforment docstrings et fichiers
Markdown en **site web de documentation**. Tu les croiseras dans le parcours P07.

### 2.9 Les règles d'or

1. Documente le **contrat** (ce que la fonction promet), pas l'implémentation.
2. Mets à jour la doc **en même temps** que le code.
3. Donne **un exemple** : il vaut mille mots.
4. Écris pour quelqu'un qui **ne connaît pas** le projet.

## 3. ⚠️ Pièges courants

- **Docstring obsolète** : décrit l'ancien comportement.
- **Docstring qui répète le nom** : `"""Calcule le prix."""` pour `calculer_prix()` n'apporte rien.
- **Exemples doctest fragiles** : espaces, ordre d'un dictionnaire, nombres flottants (arrondis !).
- **Commentaire à la place d'un bon nom** : renomme plutôt.

## 4. À retenir

- Docstring : résumé + `Args` / `Returns` / `Raises` + exemple.
- `doctest` : exemples exécutables et vérifiés.
- README : installation, utilisation, tests.
- `argparse` fournit `--help` automatiquement.

## 5. Exercices

Fichier : [`exercices/ex39_documenter.py`](../exercices/ex39_documenter.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex39_documenter.py -v
```

## 6. Quiz

1. Où place-t-on une docstring de fonction ?
2. Que fait `python -m doctest` ?
3. Que doit contenir un README minimal ?
4. Pourquoi une docstring avec exemple est-elle plus fiable ?

<details>
<summary>Réponses</summary>

1. Juste sous la ligne `def`, entre triples guillemets.
2. Il exécute les exemples `>>>` des docstrings et vérifie leur résultat.
3. Ce que fait le projet, comment l'installer, l'utiliser et lancer les tests.
4. Avec `doctest`, l'exemple est exécuté : s'il devient faux, un test échoue.

</details>
