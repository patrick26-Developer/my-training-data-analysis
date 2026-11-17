# Leçon 1.1 — Ton premier programme

⏱ 45 min · 🎯 Débutant · 📦 Prérequis : aucun

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Dans 45 minutes, tu auras écrit et lancé ton tout premier programme, et tu sauras lire un message d'erreur sans paniquer.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Expliquer ce qu'est un programme et ce que fait Python
- Lancer Python en mode interactif et exécuter un fichier `.py`
- Afficher du texte avec `print()`
- Écrire des commentaires et lire un message d'erreur sans paniquer

---

## 1. Le problème

Tu tiens une petite boutique à Brazzaville. Chaque soir, tu additionnes les ventes à la main
et tu te trompes parfois. Un ordinateur ne se trompe pas dans les calculs, mais **il faut lui dire quoi faire,
précisément**. Cette liste d'instructions s'appelle un **programme**.

## 2. L'idée en images

Un programme, c'est une **recette de cuisine** :

```
Recette du pain          Programme Python
─────────────────        ─────────────────
1. Mélanger farine, eau  1. print("Bonjour")
2. Pétrir                2. print("Bienvenue")
3. Cuire                 3. ...
```

Le cuisinier suit la recette **ligne après ligne, dans l'ordre**. Python fait pareil :
il lit ton fichier de haut en bas et exécute chaque instruction.

**Python** est un langage qui ressemble à de l'anglais simple. Il est utilisé pour les sites web,
l'analyse de données, l'intelligence artificielle, la cybersécurité… C'est le meilleur premier langage.

## 3. Pas à pas

### 3.1 Vérifier que Python est installé

Ouvre un terminal (PowerShell sous Windows) et tape :

```powershell
python --version
```

Tu dois voir quelque chose comme `Python 3.13.5`. Si le message dit que la commande est introuvable,
installe Python depuis [python.org](https://www.python.org/downloads/) et **coche « Add Python to PATH »**.

### 3.2 Le mode interactif (la calculatrice qui parle)

Tape `python` puis Entrée. Tu vois `>>>` : Python attend tes ordres.

```python
>>> 2 + 3
5
>>> print("Mbote !")
Mbote !
>>> exit()
```

Le mode interactif sert à **essayer**. Pour un vrai programme, on écrit un fichier.

### 3.3 Ton premier fichier

Crée un fichier `bonjour.py` avec ce contenu :

```python
print("Mbote ! Bienvenue à Mayele Python Académie")
```

Lance-le :

```powershell
python bonjour.py
```

Résultat :

```
Mbote ! Bienvenue à Mayele Python Académie
```

Tu viens d'écrire et d'exécuter ton premier programme.

### 3.4 `print()` en détail

`print()` est une **fonction** : un mot suivi de parenthèses, qui fait une action. Ici, afficher.
Ce qu'on met entre les parenthèses s'appelle l'**argument**. Le texte s'écrit entre guillemets
(`"..."` ou `'...'`) : c'est une **chaîne de caractères**.

```python
print("Manioc")
print("Plantain")
```

```
Manioc
Plantain
```

Chaque `print` va à la ligne. On peut afficher plusieurs choses d'un coup, séparées par un espace :

```python
print("Manioc", 500, "FCFA")
```

```
Manioc 500 FCFA
```

Deux options utiles :

```python
print("Manioc", "500", sep=" : ")  # sep : ce qu'on met entre les éléments
print("Total", end=" -> ")  # end : ce qu'on met à la fin (au lieu du retour à la ligne)
print("1500 FCFA")
```

```
Manioc : 500
Total -> 1500 FCFA
```

### 3.5 Les commentaires

Tout ce qui suit `#` est ignoré par Python. C'est une note pour les humains :

```python
# Affiche le nom de la boutique
print("Boutique Mama Nzoni")  # on peut aussi commenter en fin de ligne
```

### 3.6 Retourner une valeur : `return`

Dans les exercices, tu écriras des **fonctions** qui *renvoient* un texte avec `return`, au lieu de
l'afficher. C'est ce qui permet à l'ordinateur de **vérifier ta réponse automatiquement**.
Tu verras les fonctions en détail au module 5 ; pour l'instant, recopie simplement cette forme :

```python
def message_boutique():
    return "Boutique Mama Nzoni"
```

`def` crée la fonction, `return` donne le résultat. Le code de la fonction est **décalé de 4 espaces** :
en Python, l'**indentation** fait partie de la syntaxe.

## 4. ⚠️ Pièges courants

**Oublier un guillemet**

```python
print("Bonjour)
```
```
SyntaxError: unterminated string literal (detected at line 1)
```
Lecture : « erreur de syntaxe : le texte n'est pas fermé ». Ajoute le guillemet manquant.

**Mal écrire `print`**

```python
Print("Bonjour")
```
```
NameError: name 'Print' is not defined
```
Python distingue **majuscules et minuscules** : `print` ≠ `Print`.

**Mauvaise indentation**

```python
print("a")
    print("b")
```
```
IndentationError: unexpected indent
```

> 💡 **Lire une erreur** : regarde la **dernière ligne** (le type d'erreur et son explication),
> puis le numéro de ligne indiqué plus haut. L'erreur est ton amie : elle te dit où chercher.

## 5. À retenir

- Un programme est une suite d'instructions exécutées dans l'ordre.
- `python fichier.py` exécute un fichier ; `python` seul ouvre le mode interactif.
- `print()` affiche ; `sep` et `end` règlent la présentation.
- `#` introduit un commentaire.
- Python distingue majuscules et minuscules, et l'indentation compte.

## 6. Exercices

Fichier : [`exercices/ex01_premiers_pas.py`](../exercices/ex01_premiers_pas.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex01_premiers_pas.py -v
```

## 7. Quiz

1. Quelle commande exécute le fichier `ventes.py` ?
2. Que fait `print("A", "B", sep="-")` ?
3. Que signifie `NameError: name 'Print' is not defined` ?
4. À quoi sert `#` ?
5. Pourquoi l'indentation est-elle importante en Python ?

<details>
<summary>Réponses</summary>

1. `python ventes.py`
2. Il affiche `A-B`.
3. Python ne connaît pas le nom `Print` (il faut écrire `print`, en minuscules).
4. À écrire un commentaire ignoré par Python.
5. Elle définit quelles lignes appartiennent à un même bloc (par exemple le corps d'une fonction).

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu viens d'écrire et d'exécuter ton premier programme. Tous les développeurs du monde ont commencé exactement comme toi, par un simple « Mbote ».

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 1.2 — Variables et nombres](l02_variables_et_nombres.md).
<!-- /cadre:fin -->
