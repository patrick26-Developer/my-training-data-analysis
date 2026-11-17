# Leçon 10.1 — Déboguer : traquer et corriger les bugs

⏱ 60 min · 🎯 Intermédiaire · 📦 Prérequis : modules 1 à 6

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Les bugs ne sont pas des ennemis : ce sont des énigmes. Tu vas apprendre la méthode des détectives du code.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Appliquer une **méthode** pour trouver un bug (au lieu de deviner)
- Utiliser `print`, `breakpoint()` / `pdb` et le débogueur de ton éditeur
- Reconnaître les **bugs classiques** d'un débutant
- Installer des **journaux** (`logging`) au lieu de `print` partout

---

## 1. Le problème

Un programme qui ne fonctionne pas du premier coup, c'est **normal** : même les experts passent plus de temps à
corriger qu'à écrire. La différence entre un débutant et un expert, c'est la **méthode**.

> *« Le débogage, c'est être le détective d'un crime dont tu es aussi le coupable. »*

## 2. La méthode en 6 étapes

1. **Reproduire** : trouve une entrée qui fait échouer le programme à chaque fois.
2. **Lire** le message d'erreur (dernière ligne du traceback, puis le numéro de ligne).
3. **Isoler** : réduis le problème au plus petit exemple possible.
4. **Formuler une hypothèse** : « je pense que `total` vaut 0 ici, parce que… »
5. **Vérifier** (afficher, déboguer, tester) — jamais « essayer au hasard ».
6. **Corriger** puis **retester**, et ajouter un test pour que le bug ne revienne pas.

## 3. Pas à pas

### 3.1 Lire un traceback (rappel)

```
Traceback (most recent call last):
  File "boutique.py", line 18, in <module>
    afficher_total(panier)
  File "boutique.py", line 11, in afficher_total
    total += article["prix"] * article["qte"]
KeyError: 'qte'
```

→ Le dictionnaire `article` n'a pas la clé `"qte"` (peut-être `"quantite"`). Tout est dit : type, message, ligne.

### 3.2 Le débogage par `print`

```python
def moyenne(notes):
    total = 0
    for n in notes:
        total += n
        print(f"DEBUG n={n!r} total={total!r}")  # !r montre aussi les guillemets/types
    return total / len(notes)
```

Astuce : `print(f"{variable = }")` affiche le **nom et la valeur** (Python 3.8+).
Pense à **retirer** les `print` de debug à la fin.

### 3.3 Le débogueur : `breakpoint()`

```python
def calcul(a, b):
    resultat = a * b
    breakpoint()  # le programme s'arrête ici et ouvre pdb
    return resultat + 1
```

Commandes de `pdb` :

| Commande | Effet |
|---|---|
| `p variable` | affiche la valeur |
| `n` (next) | exécute la ligne suivante |
| `s` (step) | entre dans la fonction appelée |
| `c` (continue) | continue jusqu'au prochain point d'arrêt |
| `l` (list) | montre le code autour |
| `w` (where) | affiche la pile d'appels |
| `q` (quit) | quitte |

Dans **VS Code** : clique à gauche d'un numéro de ligne pour poser un **point d'arrêt**, puis lance « Déboguer ». Tu
vois les variables, avances pas à pas, évalues des expressions — plus confortable que `pdb`.

### 3.4 `assert` pour vérifier ses hypothèses

```python
assert len(notes) > 0, "la liste de notes ne doit pas être vide"
```

Si l'hypothèse est fausse, le programme s'arrête **là où le problème est né**, et non dix lignes plus loin.

### 3.5 `logging` : des journaux professionnels

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logging.debug("détail technique")  # masqué avec level=INFO
logging.info("Vente enregistrée : %s", 1500)
logging.warning("Stock bas : %d", 3)
logging.error("Paiement refusé")
```

Niveaux : `DEBUG < INFO < WARNING < ERROR < CRITICAL`. Contrairement à `print`, on peut changer le niveau
sans toucher au code, écrire dans un fichier (`filename="app.log"`), et filtrer.

### 3.6 Les bugs classiques

| Symptôme | Cause fréquente |
|---|---|
| Résultat décalé de 1 | *off-by-one* : `range(n)` vs `range(1, n + 1)` |
| `None` inattendu | oubli de `return`, ou `liste = liste.sort()` |
| Comportement bizarre d'une liste | alias (`b = a`) au lieu d'une copie |
| Boucle infinie | la condition ne change jamais |
| `TypeError: str + int` | oubli de conversion (`int(input())`) |
| Valeur par défaut qui « se souvient » | argument par défaut modifiable (`liste=[]`) |
| Test toujours faux | `=` au lieu de `==`, ou comparaison de types différents |
| Résultat flottant bizarre | erreurs d'arrondi (`0.1 + 0.2`) |
| `UnboundLocalError` | variable modifiée dans une fonction sans `global`/retour |
| Texte mal formaté | oubli de `\n`, `strip()`, encodage |

### 3.7 La technique du « canard en plastique »

Explique ton code **à voix haute**, ligne par ligne, à un objet (un canard en plastique !) ou à un collègue. Très
souvent, tu trouves le bug **avant** la fin de ta phrase.

### 3.8 Quand tu es bloqué

1. Prends une pause de 10 minutes.
2. Réduis le problème à un exemple de 5 lignes.
3. Copie le **message d'erreur exact** dans un moteur de recherche.
4. Demande de l'aide en donnant : le code minimal, l'erreur complète, ce que tu as essayé.

## 4. ⚠️ Pièges courants

- **Modifier plusieurs choses à la fois** : tu ne sais plus ce qui a corrigé (ou cassé).
- **Corriger le symptôme, pas la cause** (ajouter un `if` pour masquer une erreur).
- **Laisser des `print` de debug** dans le code final.
- **Ne pas relire le message d'erreur** : il contient presque toujours la solution.
- **Avaler les erreurs** avec `except: pass`.

## 5. À retenir

- Méthode : reproduire, lire, isoler, hypothèse, vérifier, corriger, retester.
- `print(f"{x = }")`, `breakpoint()`, points d'arrêt dans l'éditeur.
- `assert` pour vérifier ses hypothèses ; `logging` plutôt que `print` en production.
- Un bug corrigé mérite un test.

## 6. Exercices : répare les bugs !

Fichier : [`exercices/ex36_deboguer.py`](../exercices/ex36_deboguer.py)

Ici, les fonctions existent déjà… et **contiennent chacune un bug**. À toi de le trouver et de le corriger.

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex36_deboguer.py -v
```

## 7. Quiz

1. Quelle est la première étape du débogage ?
2. À quoi sert `breakpoint()` ?
3. Pourquoi préférer `logging` à `print` pour une application ?
4. Que fait `print(f"{x = }")` ?

<details>
<summary>Réponses</summary>

1. Reproduire le bug de façon fiable.
2. Il arrête le programme et ouvre le débogueur `pdb` à cet endroit.
3. On peut régler le niveau de détail, écrire dans un fichier et filtrer sans modifier le code.
4. Il affiche `x = valeur` (nom et valeur de la variable).

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu sais traquer un bug avec méthode. C'est la compétence qui fait gagner le plus de temps dans toute une carrière.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 10.2 — Tes premiers tests](l37_premiers_tests.md).
<!-- /cadre:fin -->
