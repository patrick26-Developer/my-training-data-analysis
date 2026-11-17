# Leçon 6.4 — `pathlib` : manipuler les chemins et les dossiers

⏱ 45 min · 🎯 Intermédiaire · 📦 Prérequis : leçons 6.2 et 6.3

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Des chemins qui marchent partout, des dossiers qui se rangent tout seuls : `pathlib` va t'épargner bien des soucis.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Construire des chemins qui marchent sous Windows, Linux et macOS
- Lire / écrire un fichier en une ligne avec `Path`
- Lister, créer, supprimer des fichiers et des dossiers
- Retrouver un fichier **à côté du script**, quel que soit le dossier courant

---

## 1. Le problème

Sous Windows, un chemin s'écrit `C:\Users\Grâce\ventes.txt` ; sous Linux, `/home/grace/ventes.txt`. Concaténer
des textes avec `\` ou `/` est source d'erreurs. Le module `pathlib` représente un chemin comme un **objet** qui sait
se comporter correctement partout.

## 2. Pas à pas

### 2.1 Créer un chemin

```python
from pathlib import Path

dossier = Path("donnees")
fichier = dossier / "ventes.csv"  # l'opérateur / assemble les morceaux
print(fichier)  # donnees\ventes.csv (Windows) ou donnees/ventes.csv
```

### 2.2 Les parties d'un chemin

```python
p = Path("donnees/archive/ventes.2026.csv")
print(p.name)  # ventes.2026.csv
print(p.stem)  # ventes.2026
print(p.suffix)  # .csv
print(p.parent)  # donnees/archive
print(p.parts)  # ('donnees', 'archive', 'ventes.2026.csv')
```

### 2.3 Lire et écrire en une ligne

```python
p = Path("note.txt")
p.write_text("Mbote !\n", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
```

(`read_bytes` / `write_bytes` pour les fichiers binaires, comme les images.)

### 2.4 Tester et créer

```python
p = Path("donnees")
print(p.exists(), p.is_file(), p.is_dir())
p.mkdir(parents=True, exist_ok=True)  # crée le dossier (et ses parents) sans erreur s'il existe
```

### 2.5 Lister des fichiers

```python
for f in Path("donnees").iterdir():  # contenu direct du dossier
    print(f.name)

for f in Path("donnees").glob("*.csv"):  # filtre par motif
    print(f)

for f in Path(".").rglob("*.py"):  # récursif dans tous les sous-dossiers
    print(f)
```

### 2.6 Renommer, copier, supprimer

```python
p = Path("a.txt")
p.rename("b.txt")  # renomme / déplace
Path("b.txt").unlink()  # supprime un fichier
Path("vide").rmdir()  # supprime un dossier VIDE
```

Pour copier ou supprimer un dossier entier : `shutil.copytree` / `shutil.rmtree` (⚠️ irréversible).

### 2.7 Le dossier du script

```python
DOSSIER = Path(__file__).resolve().parent  # dossier qui contient le script
fichier = DOSSIER / "donnees" / "ventes.csv"
```

Ainsi le programme fonctionne **quel que soit le dossier d'où on le lance**.

### 2.8 Autres dossiers utiles

```python
Path.home()  # dossier personnel de l'utilisateur
Path.cwd()  # dossier courant
```

### 2.9 Informations sur un fichier

```python
info = Path("note.txt").stat()
print(info.st_size)  # taille en octets
```

## 3. ⚠️ Pièges courants

**Mélanger texte et `Path`** : `"donnees" + "/x"` marche, `Path("donnees") + "x"` plante.
Utilise `/` avec les `Path`.

**`\` dans les chemins Windows en texte** : `"C:\nouveau"` contient un `\n` (retour à la ligne) !
Utilise `Path`, ou un texte brut : `r"C:\nouveau"`.

**`mkdir` sans `exist_ok=True`** : `FileExistsError` si le dossier existe déjà.

**`rmtree` / `unlink`** : suppression **définitive**, sans corbeille. Vérifie le chemin d'abord.

## 4. À retenir

- `Path("a") / "b" / "c.txt"` : chemins portables.
- `.name`, `.stem`, `.suffix`, `.parent`.
- `.read_text()`, `.write_text()`, `.exists()`, `.mkdir(parents=True, exist_ok=True)`, `.glob()`.
- `Path(__file__).resolve().parent` : le dossier du script.

## 5. Exercices

Fichier : [`exercices/ex23_pathlib.py`](../exercices/ex23_pathlib.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex23_pathlib.py -v
```

## 6. Mini-projet du module 6 — Carnet d'adresses persistant

Programme console avec menu : ajouter / lister / rechercher / supprimer un contact. Les contacts sont enregistrés
dans un fichier **JSON** à côté du script, avec gestion des erreurs (fichier absent ou corrompu, saisie vide).
Solution : [`../projets/m6_carnet_d_adresses.py`](../projets/m6_carnet_d_adresses.py).

## 7. Quiz

1. Quel opérateur assemble des morceaux de chemin ?
2. Que renvoie `Path("a/b.tar.gz").suffix` ?
3. Comment créer un dossier sans erreur s'il existe déjà ?
4. Comment obtenir le dossier du script en cours ?

<details>
<summary>Réponses</summary>

1. `/`
2. `".gz"` (le dernier suffixe).
3. `p.mkdir(parents=True, exist_ok=True)`
4. `Path(__file__).resolve().parent`

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Le module 6 est terminé : erreurs, fichiers, CSV, JSON et chemins. Tu peux maintenant créer un carnet d'adresses qui se souvient.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 7.1 — Importer des modules](l24_importer.md).
<!-- /cadre:fin -->
