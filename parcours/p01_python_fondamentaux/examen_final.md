# Examen final — P01 Python Fondamentaux

⏱ Durée : 90 minutes · ✅ Seuil de réussite : 70 % · 📚 Sans aide extérieure (documentation officielle autorisée)

L'examen comporte **deux parties** : un QCM de 30 questions (30 points) et 6 problèmes de code (70 points).
Les réponses du QCM sont à la fin ; à ne consulter qu'après avoir répondu.

---

## Partie A — QCM (30 points, 1 point par question)

**1.** Que fait `print("A", "B", sep="-")` ?
a) `A B` b) `A-B` c) `AB` d) Une erreur

**2.** Quel est le type de `input("Âge : ")` ?
a) `int` b) `float` c) `str` d) cela dépend de la saisie

**3.** Que vaut `17 // 5` ?
a) 3.4 b) 3 c) 2 d) 4

**4.** Que vaut `17 % 5` ?
a) 3 b) 2 c) 12 d) 0

**5.** Que vaut `"Python"[1:4]` ?
a) `"Pyt"` b) `"yth"` c) `"ytho"` d) `"Pyth"`

**6.** Quelle expression est vraie ?
a) `bool("")` b) `bool(0)` c) `bool([0])` d) `bool(None)`

**7.** Combien de fois s'exécute `for i in range(2, 10, 3):` ?
a) 2 b) 3 c) 4 d) 8

**8.** Que contient `a` après `a = [1, 2]; b = a; b.append(3)` ?
a) `[1, 2]` b) `[1, 2, 3]` c) `[3]` d) une erreur

**9.** Comment créer un ensemble vide ?
a) `{}` b) `set()` c) `[]` d) `()`

**10.** Que renvoie `{"a": 1}.get("b", 0)` ?
a) `None` b) une erreur `KeyError` c) `0` d) `"b"`

**11.** Que fait `sorted(L)` ?
a) trie `L` en place et renvoie `None` b) renvoie une nouvelle liste triée c) renvoie un tuple d) trie `L` en place et la renvoie

**12.** Quel est le résultat de `[x * 2 for x in range(3)]` ?
a) `[0, 1, 2]` b) `[0, 2, 4]` c) `[2, 4, 6]` d) `(0, 2, 4)`

**13.** Une fonction sans instruction `return` renvoie :
a) `0` b) `""` c) `None` d) `False`

**14.** Quel est le piège de `def f(x, L=[])` ?
a) rien b) la liste par défaut est partagée entre les appels c) `L` est un tuple d) `f` ne peut être appelée qu'avec 2 arguments

**15.** Que fait `lambda x: x + 1` ?
a) une classe b) une fonction anonyme c) une boucle d) un module

**16.** Que vaut `factorielle(3)` avec `def factorielle(n): return 1 if n <= 1 else n * factorielle(n - 1)` ?
a) 3 b) 6 c) 9 d) une erreur de récursion

**17.** Quel mode d'ouverture ajoute à la fin d'un fichier sans l'effacer ?
a) `"r"` b) `"w"` c) `"a"` d) `"x"`

**18.** Pourquoi utiliser `with open(...) as f:` ?
a) c'est plus rapide b) fermeture automatique du fichier c) pour lire un binaire d) pour chiffrer

**19.** Que fait `except ValueError:` ?
a) attrape toutes les erreurs b) attrape seulement `ValueError` c) lève une erreur d) ignore le `try`

**20.** Quelle exception est levée par `int("abc")` ?
a) `TypeError` b) `ValueError` c) `KeyError` d) `NameError`

**21.** Quel module pour lire un fichier JSON ?
a) `csv` b) `json` c) `pathlib` d) `re`

**22.** `Path("a") / "b.txt"` produit :
a) un texte `"a/b.txt"` brut b) un objet `Path` c) une erreur d) un fichier créé

**23.** À quoi sert `python -m venv venv` ?
a) installer un paquet b) créer un environnement virtuel c) lancer un test d) mettre à jour pip

**24.** Que fait `if __name__ == "__main__":` ?
a) exécute le bloc seulement si le fichier est lancé directement b) importe le module c) définit `main` d) arrête le programme

**25.** Quelle commande lance les tests ?
a) `python -m pytest` b) `python -m test` c) `pytest.run()` d) `python -t`

**26.** `assert x == 3` échoue lorsque :
a) `x` vaut 3 b) `x` ne vaut pas 3 c) jamais d) toujours

**27.** Quelle est la convention pour une constante ?
a) `taux_tva` b) `TauxTva` c) `TAUX_TVA` d) `tauxTVA`

**28.** Quel outil formate automatiquement le code ?
a) `ruff format` b) `pytest` c) `pip` d) `venv`

**29.** Quelle est la complexité d'une recherche dichotomique ?
a) O(n) b) O(n²) c) O(log n) d) O(1)

**30.** Quel graphique pour comparer les ventes de 4 produits ?
a) un nuage de points b) un diagramme en barres c) un histogramme d) une courbe de tendance

---

## Partie B — Problèmes de code (70 points)

Fichier de réponse : [`exercices/ex41_examen_final.py`](exercices/ex41_examen_final.py) (une fonction par problème).

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex41_examen_final.py -v
```

Le corrigé (`solutions/sol41_examen_final.py`) est à consulter **après** l'examen.

**Problème 1 (10 pts) — `mention(note)`**
Retourne `"Très bien"` (≥ 16), `"Bien"` (≥ 14), `"Assez bien"` (≥ 12), `"Passable"` (≥ 10), sinon `"Ajourné"`.
Lève `ValueError` si la note n'est pas entre 0 et 20.

**Problème 2 (10 pts) — `mots_frequents(texte, n)`**
Retourne la liste des `n` mots les plus fréquents (en minuscules, sans ponctuation `.,;:!?`), sous forme de couples
`(mot, nombre)`, triés par fréquence décroissante puis ordre alphabétique.

**Problème 3 (10 pts) — `rendre_monnaie(montant, pieces)`**
Retourne le dictionnaire `{pièce: nombre}` de l'algorithme glouton. Lève `ValueError` si `montant < 0`.

**Problème 4 (15 pts) — `charger_notes(chemin)`**
Lit un CSV (`nom,note`), ignore les lignes invalides (note non numérique ou hors de 0–20),
retourne un dictionnaire `{nom: moyenne}` (plusieurs lignes par nom possibles).
Fichier absent : retourne `{}`.

**Problème 5 (15 pts) — `est_equilibre(texte)`**
Retourne `True` si les parenthèses, crochets et accolades du texte sont correctement équilibrés et imbriqués :
`"([]{})"` → `True`, `"([)]"` → `False`. Pense à une **pile** (liste).

**Problème 6 (10 pts) — Qualité**
Ton fichier doit passer `ruff check` et `ruff format --check`, chaque fonction doit avoir une docstring avec un
exemple, et tu dois fournir **au moins 6 tests `pytest`**.

---

## Barème et décision

| Résultat global | Décision |
|---|---|
| ≥ 85 / 100 | Réussi avec **mention Très bien** |
| 70 – 84 | Réussi |
| < 70 | À repasser après révision (délai de 7 jours) |

Le **certificat « Python Fondamentaux »** exige : examen ≥ 70 % **et** projet de synthèse ≥ 70/100.

---

## Corrigé du QCM

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | c | b | b | b | c | b | b | b | c |

| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|
| b | b | c | b | b | b | c | b | b | b |

| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|---|---|---|---|---|---|---|---|---|---|
| b | b | b | a | a | b | c | a | c | b |

Détails à connaître : (6) `[0]` est une liste non vide donc vraie ; (7) `range(2, 10, 3)` donne 2, 5, 8 : 3 tours ;
(14) l'argument par défaut modifiable est créé une seule fois.
