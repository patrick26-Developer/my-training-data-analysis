# Leçon 5.2 — Paramètres : défauts, mots-clés, `*args`, `**kwargs`

⏱ 50 min · 🎯 Débutant+ · 📦 Prérequis : leçon 5.1

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Des fonctions souples, qui s'adaptent : valeurs par défaut, arguments nommés et nombre variable d'arguments.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Donner une **valeur par défaut** à un paramètre
- Appeler une fonction par **mot-clé**
- Accepter un nombre variable d'arguments (`*args`, `**kwargs`)
- Éviter le piège du paramètre par défaut modifiable

---

## 1. Le problème

La TVA est presque toujours de 18 %. Obliger l'appelant à la répéter à chaque fois est pénible. Et une fonction
`additionner` devrait accepter 2, 3 ou 10 nombres. Python offre des paramètres souples pour cela.

## 2. Pas à pas

### 2.1 Valeur par défaut

```python
def prix_ttc(prix_ht, taux=18):
    return prix_ht * (1 + taux / 100)


print(prix_ttc(1000))  # 1180.0   (taux = 18)
print(prix_ttc(1000, 5))  # 1050.0
```

Les paramètres **avec** défaut se placent **après** ceux sans défaut.

### 2.2 Arguments nommés

```python
def facture(client, produit, quantite=1, remise=0):
    return f"{client} : {quantite} x {produit} (remise {remise} %)"


print(facture("Grâce", "Riz"))
print(facture("Grâce", "Riz", remise=10))  # on saute quantite
print(facture(produit="Sel", client="Jean", quantite=3))  # ordre libre
```

Les arguments nommés rendent l'appel **lisible**, surtout avec beaucoup de paramètres.

### 2.3 `*args` : nombre variable d'arguments positionnels

```python
def additionner(*nombres):
    return sum(nombres)  # nombres est un tuple


print(additionner(1, 2))  # 3
print(additionner(1, 2, 3, 4, 5))  # 15
```

On peut aussi **déballer** une liste à l'appel :

```python
valeurs = [4, 5, 6]
print(additionner(*valeurs))  # 15
```

### 2.4 `**kwargs` : arguments nommés libres

```python
def fiche(**infos):
    return ", ".join(f"{cle}={valeur}" for cle, valeur in infos.items())


print(fiche(nom="Grâce", ville="Brazzaville"))  # nom=Grâce, ville=Brazzaville
```

`infos` est un dictionnaire. On déballe un dictionnaire avec `**` : `fiche(**{"nom": "Jean"})`.

### 2.5 Tout combiner

Ordre : positionnels, `*args`, nommés avec défaut, `**kwargs`.

```python
def commande(client, *produits, livraison=False, **options): ...
```

### 2.6 Paramètres « mot-clé seulement »

Ce qui suit `*` ne peut être donné que par nom — pratique pour éviter les erreurs :

```python
def arrondir(valeur, *, decimales=2):
    return round(valeur, decimales)


arrondir(3.14159, decimales=3)  # ✅
arrondir(3.14159, 3)  # ❌ TypeError
```

## 3. ⚠️ Pièges courants

**Défaut modifiable partagé** — LE piège classique de Python :

```python
def ajouter(element, liste=[]):  # ❌ la liste est créée UNE SEULE FOIS
    liste.append(element)
    return liste


print(ajouter(1))  # [1]
print(ajouter(2))  # [1, 2]   !!
```

Correction :

```python
def ajouter(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste
```

**Paramètre donné deux fois**

```python
prix_ttc(1000, prix_ht=500)
```
```
TypeError: prix_ttc() got multiple values for argument 'prix_ht'
```

## 4. À retenir

- `def f(a, b=valeur)` : valeur par défaut, après les paramètres obligatoires.
- Appel par nom : `f(b=3, a=1)`.
- `*args` → tuple ; `**kwargs` → dictionnaire.
- Jamais de défaut modifiable (`[]`, `{}`) : utilise `None`.

## 5. Exercices

Fichier : [`exercices/ex17_parametres.py`](../exercices/ex17_parametres.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex17_parametres.py -v
```

## 6. Quiz

1. Que vaut `prix_ttc(100)` si `taux=18` par défaut ?
2. Que contient `args` dans `def f(*args)` appelée avec `f(1, 2)` ?
3. Pourquoi `def f(x=[])` est-il dangereux ?
4. Comment passer les éléments d'une liste `L` comme arguments séparés ?

<details>
<summary>Réponses</summary>

1. `118.0`
2. Le tuple `(1, 2)`.
3. La liste par défaut est créée une seule fois et partagée entre tous les appels.
4. `f(*L)`

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tes fonctions sont désormais flexibles et lisibles. Tu connais même le piège classique de `liste=[]` !

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 5.3 — Portée des variables et récursivité](l18_portee_et_recursivite.md).
<!-- /cadre:fin -->
