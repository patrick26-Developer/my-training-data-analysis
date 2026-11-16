# Leçon 6.3 — Fichiers CSV et JSON

⏱ 55 min · 🎯 Intermédiaire · 📦 Prérequis : leçons 6.1 et 6.2

## 🎯 Ce que tu sauras faire

- Lire et écrire un fichier **CSV** (tableur) avec le module `csv`
- Sauvegarder et recharger des données structurées en **JSON**
- Choisir le bon format selon les données

---

## 1. Le problème

Écrire `"Manioc;500;12"` à la main et le découper avec `split(";")` marche… jusqu'au jour où un nom contient
un point-virgule ou un retour à la ligne. Il existe des **formats standards** et des modules faits pour eux.

| Format | Pour quoi ? | Exemple |
|---|---|---|
| **CSV** | Tableaux (lignes/colonnes), échange avec Excel | `nom,prix\nRiz,800` |
| **JSON** | Données structurées (listes, dictionnaires imbriqués), API web | `{"nom": "Riz", "prix": 800}` |

## 2. Pas à pas

### 2.1 Écrire un CSV

```python
import csv

produits = [
    {"nom": "Manioc", "prix": 500, "quantite": 12},
    {"nom": "Riz", "prix": 800, "quantite": 3},
]

with open("stock.csv", "w", newline="", encoding="utf-8") as f:
    ecrivain = csv.DictWriter(f, fieldnames=["nom", "prix", "quantite"])
    ecrivain.writeheader()
    ecrivain.writerows(produits)
```

Résultat dans `stock.csv` :

```
nom,prix,quantite
Manioc,500,12
Riz,800,3
```

`newline=""` est **obligatoire** avec `csv` sous Windows (sinon des lignes vides apparaissent).

### 2.2 Lire un CSV

```python
with open("stock.csv", newline="", encoding="utf-8") as f:
    for ligne in csv.DictReader(f):
        print(ligne["nom"], int(ligne["prix"]) * int(ligne["quantite"]))
```

⚠️ **Tout est lu comme du texte** : convertis avec `int()` ou `float()`.

Sans en-tête, on utilise `csv.reader` (lignes = listes) et `csv.writer`.

### 2.3 Autre séparateur

Les fichiers français exportés d'Excel utilisent souvent `;` :

```python
csv.DictReader(f, delimiter=";")
```

### 2.4 JSON : écrire

```python
import json

boutique = {
    "nom": "Mama Nzoni",
    "ouverte": True,
    "produits": [{"nom": "Riz", "prix": 800}, {"nom": "Sel", "prix": 100}],
    "adresse": None,
}

with open("boutique.json", "w", encoding="utf-8") as f:
    json.dump(boutique, f, ensure_ascii=False, indent=2)
```

- `indent=2` : fichier lisible ;
- `ensure_ascii=False` : garde les accents au lieu de `é`.

### 2.5 JSON : lire

```python
with open("boutique.json", encoding="utf-8") as f:
    boutique = json.load(f)
print(boutique["produits"][0]["nom"])  # Riz
```

### 2.6 Correspondance Python ↔ JSON

| Python | JSON |
|---|---|
| `dict` | objet `{}` |
| `list`, `tuple` | tableau `[]` |
| `str` | texte |
| `int`, `float` | nombre |
| `True` / `False` / `None` | `true` / `false` / `null` |

Un `tuple` revient en `list` ; un `set`, une date ou une classe ne sont **pas** convertibles directement.

### 2.7 Texte ↔ JSON sans fichier : `dumps` / `loads`

```python
texte = json.dumps({"a": 1})  # '{"a": 1}'
objet = json.loads(texte)  # {'a': 1}
```

C'est ce qu'on utilise pour dialoguer avec une API web (parcours P06).

### 2.8 Gérer les erreurs

```python
try:
    with open("boutique.json", encoding="utf-8") as f:
        boutique = json.load(f)
except FileNotFoundError:
    boutique = {}
except json.JSONDecodeError:
    print("Fichier corrompu")
    boutique = {}
```

## 3. ⚠️ Pièges courants

**Oublier `newline=""`** avec `csv` : lignes vides entre les lignes.

**Oublier de convertir** : `"500" * 2` donne `"500500"`, pas 1000.

**Virgule décimale** dans un CSV français (`12,5`) : remplace `,` par `.` avant `float`.

**JSON ≠ dictionnaire Python** : les clés d'un objet JSON sont **toujours des textes** (`{1: "a"}` revient avec la clé `"1"`).

## 4. À retenir

- `csv.DictReader` / `DictWriter` : un dictionnaire par ligne ; tout est du texte.
- `json.dump` / `json.load` pour les fichiers, `dumps` / `loads` pour les textes.
- `indent=2, ensure_ascii=False` pour un JSON lisible avec accents.

## 5. Exercices

Fichier : [`exercices/ex22_csv_et_json.py`](../exercices/ex22_csv_et_json.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex22_csv_et_json.py -v
```

## 6. Quiz

1. Pourquoi `newline=""` avec `csv` ?
2. Quel type ont les valeurs lues par `csv.DictReader` ?
3. Que devient `None` en JSON ?
4. Quelle fonction transforme un dictionnaire en texte JSON ?

<details>
<summary>Réponses</summary>

1. Pour éviter des lignes vides parasites (surtout sous Windows).
2. Toujours des `str`.
3. `null`.
4. `json.dumps`.

</details>
