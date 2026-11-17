# Leçon 3.3 — `break`, `continue` et boucles imbriquées

⏱ 50 min · 🎯 Débutant · 📦 Prérequis : leçons 3.1 et 3.2

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Chercher, sauter, s'arrêter au bon moment : tu vas apprendre à piloter tes boucles avec précision, et même à dessiner des motifs.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Sortir d'une boucle avec `break`, sauter un tour avec `continue`
- Utiliser `else` sur une boucle
- Écrire des boucles imbriquées (tableaux, motifs)
- Comprendre ce que coûte une boucle dans une boucle

---

## 1. Le problème

Tu cherches un client dans une liste : dès que tu l'as trouvé, inutile de continuer. Tu veux aussi ignorer les
lignes vides d'un fichier. Et pour dessiner un tableau, il faut des lignes **et** des colonnes.

## 2. Pas à pas

### 2.1 `break` : sortir immédiatement

```python
for n in range(1, 100):
    if n * n > 50:
        print("Premier carré > 50 :", n * n)  # 64
        break
```

### 2.2 `continue` : passer au tour suivant

```python
for n in range(1, 8):
    if n % 2 == 0:
        continue  # on saute les pairs
    print(n)  # 1 3 5 7
```

### 2.3 `for ... else`

Le bloc `else` d'une boucle s'exécute **si la boucle n'a pas été interrompue par `break`**.

```python
for diviseur in range(2, 7):
    if 7 % diviseur == 0:
        print("7 n'est pas premier")
        break
else:
    print("7 est premier")  # affiché : aucun break
```

### 2.4 Boucles imbriquées

Une boucle **dans** une boucle : pour chaque tour de la boucle extérieure, la boucle intérieure tourne en entier.

```python
for ligne in range(1, 4):
    for colonne in range(1, 4):
        print(ligne * colonne, end="\t")
    print()  # retour à la ligne après chaque ligne
```
```
1	2	3	
2	4	6	
3	6	9	
```

Motif en étoiles :

```python
for i in range(1, 5):
    print(" " * (4 - i) + "*" * (2 * i - 1))
```
```
   *
  ***
 *****
*******
```

### 2.5 `break` dans une boucle imbriquée

`break` ne sort que de la boucle **la plus proche**. Pour tout quitter, mets la recherche dans une fonction et
utilise `return` (module 5).

### 2.6 Combien ça coûte ?

Une boucle de 1000 tours dans une boucle de 1000 tours = **1 000 000** d'opérations. Les boucles imbriquées
deviennent vite lentes : retiens-le, on y reviendra en Python avancé.

### 2.7 Aperçu : listes et couples

Les exercices 5 et 6 retournent une **liste** (`[2, 3, 5]`) et des **couples** (`(1, 4)`), vus en détail au
module 4. Pour l'instant : `resultat = []` crée une liste vide, `resultat.append(x)` y ajoute `x`,
et `(a, b)` est un couple de deux valeurs.

## 3. ⚠️ Pièges courants

**`continue` dans un `while` sans progression**

```python
n = 0
while n < 5:
    if n == 2:
        continue  # n n'augmente plus : boucle infinie !
    n += 1
```
Fais la progression **avant** le `continue`.

**Croire que `break` sort de toutes les boucles** : il ne sort que de la plus proche.

## 4. À retenir

- `break` : quitte la boucle ; `continue` : passe au tour suivant.
- `else` d'une boucle : exécuté si aucun `break`.
- Boucle imbriquée : l'intérieure tourne entièrement à chaque tour de l'extérieure.

## 5. Exercices

Fichier : [`exercices/ex10_break_continue_imbriquees.py`](../exercices/ex10_break_continue_imbriquees.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex10_break_continue_imbriquees.py -v
```

## 6. Quiz

1. Quelle différence entre `break` et `continue` ?
2. Quand le `else` d'une boucle s'exécute-t-il ?
3. Combien d'itérations totales pour deux `for` imbriqués de `range(4)` ?
4. Pourquoi `continue` peut-il créer une boucle infinie dans un `while` ?

<details>
<summary>Réponses</summary>

1. `break` quitte la boucle, `continue` passe directement au tour suivant.
2. Quand la boucle se termine normalement, sans `break`.
3. 16 (4 × 4).
4. Si la ligne qui fait progresser le compteur est après le `continue`, elle n'est jamais exécutée.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu contrôles tes boucles comme un chef d'orchestre. Le module 3 est terminé : bravo pour ta régularité !

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 4.1 — Les listes](l11_listes.md).
<!-- /cadre:fin -->
