# Leçon 5.3 — Portée des variables et récursivité

⏱ 55 min · 🎯 Intermédiaire · 📦 Prérequis : leçons 5.1 et 5.2

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Pourquoi une variable disparaît-elle parfois ? Et comment une fonction peut-elle s'appeler elle-même ? Deux idées fascinantes.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Expliquer où vit une variable (portée locale et globale)
- Éviter `global` en passant des paramètres et en retournant des résultats
- Écrire une fonction **récursive** simple (factorielle, Fibonacci)
- Reconnaître le **cas de base** et ses dangers

---

## 1. Le problème

```python
total = 0


def ajouter(n):
    total = total + n  # UnboundLocalError !
```

Pourquoi cette erreur ? Parce que chaque fonction a son **propre espace de noms**. Comprendre cet espace évite
une grande partie des bugs de débutant.

## 2. L'idée en images

Chaque fonction est une **pièce fermée** avec ses propres étiquettes. Elle peut **regarder** par la fenêtre dans la pièce
extérieure (lire), mais pas y **écrire** sans autorisation.

```
┌──────────── programme (global) ────────────┐
│ TVA = 18                                     │
│   ┌──── fonction prix_ttc ────┐              │
│   │ prix_ht = 1000  (local)   │              │
│   │ lit TVA : OK              │              │
│   └───────────────────────────┘              │
└──────────────────────────────────────────────┘
```

## 3. Pas à pas

### 3.1 Variables locales

```python
def calcul():
    resultat = 10  # locale : n'existe que dans la fonction
    return resultat


calcul()
print(resultat)  # NameError: name 'resultat' is not defined
```

### 3.2 Lire une variable globale

```python
TVA = 18  # constante : MAJUSCULES par convention


def prix_ttc(prix_ht):
    return prix_ht * (1 + TVA / 100)  # lecture : OK
```

### 3.3 Modifier une variable globale : à éviter

```python
compteur = 0


def incrementer():
    global compteur
    compteur += 1
```

`global` fonctionne, mais rend le code **imprévisible** (qui a modifié `compteur` ?). Préfère passer la valeur
en paramètre et **retourner** le nouveau résultat :

```python
def incrementer(compteur):
    return compteur + 1


compteur = incrementer(compteur)
```

### 3.4 Ombrage

```python
x = 5


def f():
    x = 99  # crée une NOUVELLE variable locale x
    return x


f()
print(x)  # 5 : la globale n'a pas changé
```

### 3.5 Les objets modifiables sont partagés

```python
def ajouter(liste, element):
    liste.append(element)  # modifie la liste de l'appelant !


panier = []
ajouter(panier, "Riz")
print(panier)  # ['Riz']
```

Une fonction qui reçoit une liste peut la **modifier** (*effet de bord*). Documente-le, ou travaille sur une copie.

### 3.6 Récursivité : une fonction qui s'appelle elle-même

Idée : résoudre un problème en le réduisant à une **version plus petite du même problème**.

```python
def factorielle(n):
    if n <= 1:  # cas de base : on s'arrête
        return 1
    return n * factorielle(n - 1)  # cas récursif : problème plus petit
```

Déroulé de `factorielle(4)` :

```
factorielle(4) = 4 * factorielle(3)
               = 4 * (3 * factorielle(2))
               = 4 * (3 * (2 * factorielle(1)))
               = 4 * 3 * 2 * 1 = 24
```

Une fonction récursive a **toujours** :
1. un **cas de base** (qui arrête) ;
2. un **appel récursif** qui se rapproche du cas de base.

Fibonacci : 0, 1, 1, 2, 3, 5, 8…

```python
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

⚠️ Cette version est **très lente** pour de grandes valeurs (elle refait les mêmes calculs). On verra la mémoïsation
en Python avancé ; la version avec boucle est préférable en pratique.

### 3.7 Quand utiliser la récursivité ?

Utile pour les structures **arborescentes** (dossiers, expressions) et certains algorithmes (tri fusion, parcours).
Pour un simple compteur, une boucle est plus claire et plus rapide.

## 4. ⚠️ Pièges courants

**Pas de cas de base**

```python
def infini(n):
    return infini(n - 1)
```
```
RecursionError: maximum recursion depth exceeded
```
Python limite la profondeur à environ 1 000 appels.

**Modifier un argument sans le vouloir** (liste partagée) : copie avant de modifier.

**Utiliser `global` partout** : le code devient impossible à tester.

## 5. À retenir

- Variables **locales** : propres à la fonction ; **globales** : visibles partout en lecture.
- Évite `global` : passe des paramètres, retourne des résultats.
- Les listes et dictionnaires passés en paramètre peuvent être modifiés par la fonction.
- Récursivité = cas de base + appel plus petit.

## 6. Exercices

Fichier : [`exercices/ex18_portee_et_recursivite.py`](../exercices/ex18_portee_et_recursivite.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex18_portee_et_recursivite.py -v
```

## 7. Quiz

1. Une variable créée dans une fonction est-elle visible à l'extérieur ?
2. Que faut-il toujours prévoir dans une fonction récursive ?
3. Que fait `global x` ?
4. Pourquoi `fibonacci` récursif est-il lent ?

<details>
<summary>Réponses</summary>

1. Non, elle est locale.
2. Un cas de base qui arrête les appels.
3. Il indique que `x` désigne la variable globale, que l'on peut alors modifier.
4. Il recalcule plusieurs fois les mêmes valeurs.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu comprends la portée des variables et la récursivité : tu as dépassé le niveau de beaucoup de débutants.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 5.4 — Les fonctions sont des valeurs](l19_fonctions_comme_valeurs.md).
<!-- /cadre:fin -->
