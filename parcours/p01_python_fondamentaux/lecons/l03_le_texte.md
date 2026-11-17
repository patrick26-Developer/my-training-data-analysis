# Leçon 1.3 — Le texte (chaînes de caractères)

⏱ 60 min · 🎯 Débutant · 📦 Prérequis : leçon 1.2

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Les noms mal écrits, les majuscules au hasard, les espaces en trop : tu vas apprendre à nettoyer n'importe quel texte en une ligne.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Créer et assembler du texte, y compris avec les **f-strings**
- Accéder à une lettre ou à un morceau de texte (indices et tranches)
- Utiliser les méthodes courantes : `upper`, `strip`, `replace`, `split`, `find`…
- Nettoyer un texte saisi par un utilisateur

---

## 1. Le problème

Un client écrit son nom dans un formulaire : `"  mAmA   nzoni "`. Tu veux l'afficher proprement :
`"Mama Nzoni"`. Les textes saisis par des humains sont toujours désordonnés : majuscules au hasard,
espaces en trop. Python a des outils pour les nettoyer.

## 2. L'idée en images

Un texte est un **collier de perles** : chaque caractère (lettre, chiffre, espace, symbole) est une perle
numérotée **à partir de 0**.

```
 M  b  o  t  e
 0  1  2  3  4        indices positifs
-5 -4 -3 -2 -1        indices négatifs (depuis la fin)
```

## 3. Pas à pas

### 3.1 Créer du texte

```python
a = "Mbote"
b = "Brazzaville"
c = "L'école"  # guillemets doubles pour pouvoir écrire une apostrophe
d = """Ligne 1
Ligne 2"""  # trois guillemets : texte sur plusieurs lignes
```

Caractères spéciaux : `\n` (retour à la ligne), `\t` (tabulation), `\\` (un vrai antislash).

### 3.2 Assembler : `+`, `*` et les f-strings

```python
print("Mbote" + " " + "Grâce")  # Mbote Grâce
print("-" * 20)  # --------------------
```

Le plus lisible est la **f-string** : un `f` devant les guillemets, et des `{...}` qui contiennent des variables
ou des calculs.

```python
nom = "Grâce"
age = 25
print(f"{nom} a {age} ans")  # Grâce a 25 ans
print(f"Dans 5 ans : {age + 5} ans")  # Dans 5 ans : 30 ans
```

Formater un nombre : `{valeur:format}`.

```python
prix = 2500.5
print(f"{prix:.2f}")  # 2500.50   (2 décimales)
print(f"{1234567:,}")  # 1,234,567 (séparateur de milliers)
print(f"{0.153:.1%}")  # 15.3%     (pourcentage)
print(f"{'Manioc':>10}")  #     Manioc  (aligné à droite sur 10 caractères)
```

### 3.3 Longueur et indices

```python
mot = "Mbote"
print(len(mot))  # 5
print(mot[0])  # M
print(mot[4])  # e
print(mot[-1])  # e   (dernier caractère)
```

### 3.4 Les tranches (*slices*)

`texte[début:fin]` prend de `début` **inclus** à `fin` **exclu**.

```python
mot = "Brazzaville"
print(mot[0:3])  # Bra
print(mot[:3])  # Bra       (début omis = 0)
print(mot[3:])  # zzaville  (fin omise = jusqu'au bout)
print(mot[-4:])  # ville
print(mot[::-1])  # ellivazzarB   (pas de -1 : à l'envers)
```

### 3.5 Les textes sont **immuables**

On ne peut pas modifier une lettre en place :

```python
mot = "Mbote"
mot[0] = "m"
```
```
TypeError: 'str' object does not support item assignment
```

Les méthodes **renvoient un nouveau texte** ; il faut le ranger dans une variable.

### 3.6 Les méthodes les plus utiles

```python
t = "  mAmA nzoni  "
print(t.strip())  # "mAmA nzoni"      enlève les espaces aux bords
print(t.lower())  # "  mama nzoni  "
print(t.upper())  # "  MAMA NZONI  "
print(t.strip().title())  # "Mama Nzoni"      majuscule à chaque mot
print(t.replace("n", "N"))  # "  mAmA NzoNi  "
```

Chercher :

```python
phrase = "Le manioc coûte 500 FCFA"
print("manioc" in phrase)  # True
print(phrase.find("coûte"))  # 10   (position, ou -1 si absent)
print(phrase.startswith("Le"))  # True
print(phrase.endswith("FCFA"))  # True
print(phrase.count("o"))  # 3
```

Découper et recoller :

```python
ligne = "Manioc;500;12"
morceaux = ligne.split(";")  # ['Manioc', '500', '12']  (une liste, vue au module 4)
print(morceaux[0])  # Manioc
print(" - ".join(morceaux))  # Manioc - 500 - 12
```

Vérifier le contenu :

```python
"2500".isdigit()  # True
"25a".isdigit()  # False
"abc".isalpha()  # True
```

### 3.7 Convertir texte ↔ nombre

```python
int("2500") + 1  # 2501
str(2500) + " FCFA"  # "2500 FCFA"
float("3.5")  # 3.5
```

## 4. ⚠️ Pièges courants

**Indice hors limites**

```python
"Mbote"[10]
```
```
IndexError: string index out of range
```

**Oublier de ranger le résultat**

```python
nom = "grâce"
nom.upper()
print(nom)  # grâce  → inchangé !
nom = nom.upper()  # ✅
```

**Convertir un texte invalide**

```python
int("abc")
```
```
ValueError: invalid literal for int() with base 10: 'abc'
```
(Le module 6 t'apprend à gérer ces erreurs proprement.)

**Oublier le `f`**

```python
print("Total : {total}")  # affiche littéralement {total}
```

## 5. À retenir

- Indices à partir de **0** ; `-1` = dernier ; tranche `[a:b]` exclut `b`.
- f-string : `f"{variable:.2f}"` — le moyen moderne d'assembler du texte.
- Les textes sont **immuables** : les méthodes renvoient un nouveau texte.
- `strip`, `lower`, `upper`, `title`, `replace`, `split`, `join`, `find`, `startswith`, `endswith`.
- `int()`, `float()`, `str()` convertissent.

## 6. Exercices

Fichier : [`exercices/ex03_le_texte.py`](../exercices/ex03_le_texte.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex03_le_texte.py -v
```

## 7. Quiz

1. Que vaut `"Python"[1:4]` ?
2. Que vaut `"Python"[-2:]` ?
3. Pourquoi `"abc".upper()` seul sur une ligne ne change-t-il rien ?
4. Que renvoie `"a,b,c".split(",")` ?
5. Écris une f-string qui affiche `12.50 FCFA` à partir de `x = 12.5`.

<details>
<summary>Réponses</summary>

1. `"yth"`
2. `"on"`
3. La méthode renvoie un nouveau texte qui n'est rangé nulle part ; il faut écrire `texte = texte.upper()`.
4. `['a', 'b', 'c']`
5. `f"{x:.2f} FCFA"`

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu manipules le texte comme un pro : découper, nettoyer, formater. Tu peux déjà traiter des données réelles.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 1.4 — Entrées et sorties : dialoguer avec l'utilisateur](l04_entrees_et_sorties.md).
<!-- /cadre:fin -->
