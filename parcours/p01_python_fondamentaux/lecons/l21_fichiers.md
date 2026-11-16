# Leçon 6.2 — Lire et écrire des fichiers

⏱ 55 min · 🎯 Intermédiaire · 📦 Prérequis : leçon 6.1

## 🎯 Ce que tu sauras faire

- Ouvrir un fichier texte en lecture, écriture, ajout
- Utiliser `with` pour fermer automatiquement les fichiers
- Lire ligne par ligne un gros fichier
- Gérer l'absence d'un fichier et l'encodage

---

## 1. Le problème

Jusqu'ici, tout ce que ton programme sait disparaît quand il s'arrête : le stock, les ventes, les notes.
Pour **conserver** des données entre deux exécutions, on les écrit dans un **fichier**.

## 2. L'idée en images

Un fichier est un **cahier** : on l'ouvre, on lit ou on écrit, **on le referme**. Oublier de le refermer peut
perdre des données.

```
   open(...)  ──►  lire / écrire  ──►  close()
        └────────── with fait tout cela pour toi ──────────┘
```

## 3. Pas à pas

### 3.1 Écrire

```python
with open("ventes.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Manioc;500;12\n")
    fichier.write("Riz;800;3\n")
```

- Mode `"w"` : **écrase** le contenu s'il existe, crée sinon ;
- `with ... as fichier` : le fichier est **fermé automatiquement** à la sortie du bloc, même en cas d'erreur ;
- `encoding="utf-8"` : toujours le préciser, pour que `é`, `ç`, `à` s'enregistrent correctement ;
- `\n` : retour à la ligne, à écrire soi-même avec `write`.

### 3.2 Les modes d'ouverture

| Mode | Effet |
|---|---|
| `"r"` | lecture (par défaut) ; erreur si le fichier n'existe pas |
| `"w"` | écriture ; **efface** l'existant |
| `"a"` | ajout à la fin (*append*) |
| `"x"` | création ; erreur si le fichier existe déjà |

### 3.3 Lire

```python
with open("ventes.txt", encoding="utf-8") as fichier:
    contenu = fichier.read()  # tout le fichier dans un seul texte

with open("ventes.txt", encoding="utf-8") as fichier:
    lignes = fichier.readlines()  # liste de lignes (avec \n)

with open("ventes.txt", encoding="utf-8") as fichier:
    for ligne in fichier:  # ligne par ligne : économe en mémoire
        produit, prix, quantite = ligne.strip().split(";")
        print(produit, int(prix) * int(quantite))
```

Pour un gros fichier, privilégie la boucle `for ligne in fichier` : une ligne à la fois en mémoire.

### 3.4 Ajouter à la fin

```python
with open("journal.txt", "a", encoding="utf-8") as f:
    f.write("Vente de 3 sacs de manioc\n")
```

### 3.5 Écrire plusieurs lignes

```python
lignes = ["a", "b", "c"]
with open("liste.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lignes) + "\n")
    # ou : print(*lignes, sep="\n", file=f)
```

### 3.6 Fichier absent

```python
try:
    with open("inconnu.txt", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    contenu = ""
    print("Fichier introuvable, on repart de zéro.")
```

### 3.7 Un petit « carnet » persistant

```python
def charger(chemin):
    try:
        with open(chemin, encoding="utf-8") as f:
            return [ligne.strip() for ligne in f if ligne.strip()]
    except FileNotFoundError:
        return []


def sauvegarder(chemin, elements):
    with open(chemin, "w", encoding="utf-8") as f:
        for e in elements:
            f.write(e + "\n")
```

## 4. ⚠️ Pièges courants

**Mode `"w"` sur un fichier à conserver** : il est vidé **immédiatement** à l'ouverture. Pour ajouter, utilise `"a"`.

**Oublier `encoding="utf-8"`** : sous Windows, les accents peuvent être mal lus ou écrits.

**Oublier `\n`** : toutes les lignes se collent.

**Chemin relatif** : `open("ventes.txt")` cherche dans le **dossier courant du terminal**, pas forcément à côté du
script. La leçon 6.4 (`pathlib`) règle ce problème.

**Lire après la fin** : un fichier se lit une fois ; pour relire, rouvre-le ou utilise `fichier.seek(0)`.

## 5. À retenir

- `with open(chemin, mode, encoding="utf-8") as f:` — toujours.
- `"r"` lire, `"w"` écrire (écrase), `"a"` ajouter.
- `for ligne in f` pour les gros fichiers ; `.strip()` retire le `\n`.
- `FileNotFoundError` : prévois le cas.

## 6. Exercices

Fichier : [`exercices/ex21_fichiers.py`](../exercices/ex21_fichiers.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex21_fichiers.py -v
```

## 7. Quiz

1. Quelle différence entre `"w"` et `"a"` ?
2. Pourquoi utiliser `with` ?
3. Comment lire un très gros fichier sans tout charger en mémoire ?
4. Quelle exception se produit si le fichier n'existe pas ?

<details>
<summary>Réponses</summary>

1. `"w"` efface le contenu existant ; `"a"` ajoute à la fin.
2. Il ferme automatiquement le fichier, même en cas d'erreur.
3. Avec `for ligne in fichier:` qui lit une ligne à la fois.
4. `FileNotFoundError`.

</details>
