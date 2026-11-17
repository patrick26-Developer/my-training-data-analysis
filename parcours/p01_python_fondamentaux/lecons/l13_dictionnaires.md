# Leçon 4.3 — Les dictionnaires

⏱ 60 min · 🎯 Débutant · 📦 Prérequis : leçons 4.1 et 4.2

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Retrouver le prix d'un produit à partir de son nom, instantanément : bienvenue dans le monde des dictionnaires.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Associer des **clés** à des **valeurs**
- Lire, ajouter, modifier, supprimer des entrées
- Parcourir un dictionnaire
- Compter des occurrences et regrouper des données

---

## 1. Le problème

Tu veux retrouver le prix d'un produit **à partir de son nom**. Avec deux listes (`noms` et `prix`), il faut chercher
l'indice à chaque fois. Un **dictionnaire** fonctionne comme un annuaire : tu donnes le nom, il te rend la valeur.

## 2. L'idée en images

```
prix = {  "Manioc" : 500 ,
          "Riz"    : 800 ,
          "Sel"    : 100 }
            clé      valeur
```

Les **clés** sont uniques et servent d'index (texte, nombre ou tuple). Les valeurs peuvent être n'importe quoi.

## 3. Pas à pas

### 3.1 Créer et lire

```python
prix = {"Manioc": 500, "Riz": 800}
print(prix["Riz"])  # 800
print(prix.get("Sel"))  # None   (pas d'erreur si absent)
print(prix.get("Sel", 0))  # 0      (valeur par défaut)
print("Riz" in prix)  # True   (teste les clés)
print(len(prix))  # 2
```

### 3.2 Ajouter, modifier, supprimer

```python
prix["Sel"] = 100  # ajoute
prix["Riz"] = 850  # modifie
del prix["Manioc"]  # supprime (erreur si absent)
valeur = prix.pop("Sel", None)  # supprime et renvoie
prix.update({"Sucre": 700, "Riz": 900})  # fusionne
```

### 3.3 Parcourir

```python
for produit in prix:  # les clés
    print(produit)
for produit, p in prix.items():  # clés et valeurs
    print(f"{produit} : {p} FCFA")
print(list(prix.keys()), list(prix.values()))
```

### 3.4 Compter des occurrences

```python
texte = "banane"
compteur = {}
for lettre in texte:
    compteur[lettre] = compteur.get(lettre, 0) + 1
print(compteur)  # {'b': 1, 'a': 2, 'n': 2, 'e': 1}
```

Le module `collections` offre `Counter` pour faire la même chose en une ligne : `Counter("banane")`.

### 3.5 Regrouper

```python
ventes = [("lundi", 500), ("mardi", 300), ("lundi", 200)]
par_jour = {}
for jour, montant in ventes:
    par_jour.setdefault(jour, 0)
    par_jour[jour] += montant
print(par_jour)  # {'lundi': 700, 'mardi': 300}
```

### 3.6 Dictionnaires imbriqués (fiches)

```python
eleve = {
    "nom": "Grâce",
    "notes": {"maths": 14, "info": 17},
    "ville": "Brazzaville",
}
print(eleve["notes"]["info"])  # 17
```

Une **liste de dictionnaires** est la forme classique d'une petite base de données :

```python
clients = [
    {"nom": "Jean", "age": 30},
    {"nom": "Marie", "age": 25},
]
```

### 3.7 Trier un dictionnaire

```python
prix = {"Manioc": 500, "Riz": 800, "Sel": 100}
par_prix = sorted(prix.items(), key=lambda item: item[1])
print(par_prix)  # [('Sel', 100), ('Manioc', 500), ('Riz', 800)]
```

(`lambda` sera expliqué au module 5 ; pour l'instant, recopie le motif.)

## 4. ⚠️ Pièges courants

**Clé absente**

```python
prix["Sucre"]
```
```
KeyError: 'Sucre'
```
Utilise `.get("Sucre")` ou teste avec `in`.

**Clé modifiable** : une liste ne peut pas servir de clé (`TypeError: unhashable type: 'list'`) ; un tuple oui.

**Modifier le dictionnaire pendant le parcours** : `RuntimeError: dictionary changed size during iteration`.
Parcours une copie : `for k in list(d):`.

## 5. À retenir

- `{clé: valeur}` ; `d[clé]`, `d.get(clé, défaut)`, `clé in d`.
- `items()`, `keys()`, `values()` pour parcourir.
- Motif de comptage : `d[k] = d.get(k, 0) + 1`.
- Liste de dictionnaires = petite table de données.

## 6. Exercices

Fichier : [`exercices/ex13_dictionnaires.py`](../exercices/ex13_dictionnaires.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex13_dictionnaires.py -v
```

## 7. Quiz

1. Que renvoie `d.get("x", 0)` si `"x"` est absent ?
2. Que teste `"a" in d` : les clés ou les valeurs ?
3. Pourquoi une liste ne peut-elle pas être une clé ?
4. Comment ajouter 1 à un compteur qui n'existe peut-être pas encore ?

<details>
<summary>Réponses</summary>

1. `0`
2. Les clés.
3. Elle est modifiable, donc non « hachable ».
4. `d[k] = d.get(k, 0) + 1`

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu sais maintenant associer des clés à des valeurs, compter et regrouper. Tu tiens là l'outil préféré des data scientists.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 4.4 — Les ensembles (`set`)](l14_ensembles.md).
<!-- /cadre:fin -->
