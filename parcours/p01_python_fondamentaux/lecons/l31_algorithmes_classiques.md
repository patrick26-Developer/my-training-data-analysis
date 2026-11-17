# Leçon 8.4 — Algorithmes classiques

⏱ 70 min · 🎯 Intermédiaire · 📦 Prérequis : modules 3 à 5

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Comment trouver un nom parmi dix millions en 24 étapes seulement ? C'est la magie des algorithmes.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Expliquer ce qu'est un **algorithme** et comment on le décrit
- Écrire une recherche linéaire et une **recherche dichotomique**
- Écrire des tris simples (à bulles, par sélection, par insertion) et comprendre le tri de Python
- Estimer le coût d'un algorithme avec la notation **O(n)**
- Résoudre quelques problèmes classiques : nombres premiers (crible), Fibonacci, palindromes

---

## 1. Le problème

Chercher un nom dans une liste de 10 millions de contacts : lire les contacts un par un peut prendre des secondes ;
une méthode plus intelligente trouve le nom en **24 comparaisons**. La différence entre un bon et un mauvais
algorithme se compte en **ordres de grandeur**.

Un **algorithme** est une suite finie et précise d'étapes pour résoudre un problème.

## 2. Pas à pas

### 2.1 Recherche linéaire — O(n)

On regarde les éléments un par un.

```python
def chercher(liste, cible):
    for i, valeur in enumerate(liste):
        if valeur == cible:
            return i
    return -1
```

Dans le pire des cas, on lit **les n éléments**.

### 2.2 Recherche dichotomique — O(log n)

Sur une liste **triée**, on regarde le milieu et on élimine la moitié à chaque étape.

```python
def dichotomie(liste_triee, cible):
    bas, haut = 0, len(liste_triee) - 1
    while bas <= haut:
        milieu = (bas + haut) // 2
        if liste_triee[milieu] == cible:
            return milieu
        if liste_triee[milieu] < cible:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return -1
```

Pour 1 000 000 d'éléments : ≈ 20 comparaisons au lieu de 1 000 000. (Python fournit `bisect` pour cela.)

### 2.3 Tri à bulles — O(n²)

On compare les voisins et on les échange s'ils sont mal rangés ; les plus grands « remontent ».

```python
def tri_a_bulles(liste):
    liste = list(liste)  # on ne modifie pas l'original
    n = len(liste)
    for i in range(n - 1):
        echange = False
        for j in range(n - 1 - i):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                echange = True
        if not echange:
            break
    return liste
```

### 2.4 Tri par sélection et tri par insertion

```python
def tri_selection(liste):
    liste = list(liste)
    for i in range(len(liste)):
        indice_min = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[indice_min]:
                indice_min = j
        liste[i], liste[indice_min] = liste[indice_min], liste[i]
    return liste


def tri_insertion(liste):
    liste = list(liste)
    for i in range(1, len(liste)):
        valeur = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > valeur:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = valeur
    return liste
```

Ces tris sont **pédagogiques**. En pratique : `sorted()` / `.sort()` (algorithme Timsort, O(n log n), très optimisé).

### 2.5 La notation O (ordre de grandeur)

On mesure comment le temps **grandit** avec la taille n des données.

| Notation | Nom | n = 1 000 | Exemple |
|---|---|---|---|
| O(1) | constant | 1 | accès à `liste[i]`, `dict[clé]` |
| O(log n) | logarithmique | 10 | dichotomie |
| O(n) | linéaire | 1 000 | recherche linéaire, `sum` |
| O(n log n) | quasi-linéaire | 10 000 | `sorted` |
| O(n²) | quadratique | 1 000 000 | tri à bulles, deux boucles imbriquées |
| O(2ⁿ) | exponentiel | astronomique | Fibonacci récursif naïf |

Règle d'or : **deux boucles imbriquées sur n éléments → O(n²)**. À 100 000 éléments, c'est 10 milliards d'opérations.

### 2.6 Mesurer le temps

```python
import time

debut = time.perf_counter()
resultat = sorted(range(1_000_000, 0, -1))
print(f"{time.perf_counter() - debut:.3f} s")
```

(Pour des mesures fiables : `timeit`. Voir parcours P03.)

### 2.7 Le crible d'Ératosthène — nombres premiers jusqu'à n

```python
def crible(n):
    est_premier = [True] * (n + 1)
    est_premier[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if est_premier[i]:
            for multiple in range(i * i, n + 1, i):
                est_premier[multiple] = False
    return [i for i, p in enumerate(est_premier) if p]
```

Bien plus rapide que de tester chaque nombre un par un.

### 2.8 Fibonacci, version efficace

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

O(n), contre O(2ⁿ) pour la version récursive naïve.

### 2.9 Palindrome, anagramme, doublons

```python
def est_palindrome(texte):
    propre = [c.lower() for c in texte if c.isalnum()]
    return propre == propre[::-1]


def a_des_doublons(liste):
    return len(set(liste)) != len(liste)  # O(n)
```

### 2.10 Méthode pour concevoir un algorithme

1. **Comprendre** le problème (entrées, sorties, cas limites).
2. **Résoudre à la main** sur un petit exemple.
3. **Décrire** les étapes en français (pseudo-code).
4. **Coder**, puis **tester** sur des cas simples *et* des cas limites (liste vide, un seul élément, doublons).
5. **Améliorer** : peut-on faire moins d'opérations ?

## 3. ⚠️ Pièges courants

- Dichotomie sur une liste **non triée** : résultat faux.
- Boucle `while` dont les bornes ne se rapprochent jamais : boucle infinie.
- Oublier les cas limites : liste vide, un seul élément, tous les éléments égaux.
- Optimiser trop tôt : d'abord correct, ensuite rapide.

## 4. À retenir

- Un algorithme est une suite d'étapes ; sa qualité se mesure en **O(...)**.
- Recherche : linéaire O(n), dichotomique O(log n) sur liste triée.
- Tris maison O(n²) ; `sorted` O(n log n) → utilise celui de Python.
- Crible d'Ératosthène pour les nombres premiers.
- Teste toujours les cas limites.

## 5. Exercices

Fichier : [`exercices/ex31_algorithmes_classiques.py`](../exercices/ex31_algorithmes_classiques.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex31_algorithmes_classiques.py -v
```

## 6. Quiz

1. Combien de comparaisons au maximum pour une dichotomie sur 1 024 éléments ?
2. Quelle est la complexité de deux boucles imbriquées sur n éléments ?
3. Pourquoi utiliser `sorted` plutôt que son propre tri ?
4. Quelle condition doit remplir la liste pour une dichotomie ?

<details>
<summary>Réponses</summary>

1. 11 environ (log₂ 1024 = 10, plus une).
2. O(n²).
3. Il est écrit en C, très optimisé et en O(n log n).
4. Elle doit être triée.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Le module 8 est terminé. Tu as compris que la qualité d'un algorithme se mesure en ordres de grandeur — un vrai réflexe d'ingénieur.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 9.1 — Dessiner avec `turtle`](l32_turtle.md).
<!-- /cadre:fin -->
