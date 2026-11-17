# Leçon 9.2 — Courbes et histogrammes avec `matplotlib`

⏱ 70 min · 🎯 Intermédiaire · 📦 Prérequis : modules 4 et 7

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Courbes, barres, histogrammes : transforme des colonnes de chiffres en graphiques qui racontent une histoire.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Installer et importer `matplotlib`
- Tracer une **courbe**, des **barres**, un **histogramme**, un **nuage de points**, un **camembert**
- Ajouter titre, étiquettes, légende, grille
- Enregistrer un graphique dans un fichier image

---

## 1. Le problème

Un tableau de 12 mois de ventes ne « parle » pas. Un **graphique** montre en une seconde la tendance, le meilleur
mois, les creux. `matplotlib` est la bibliothèque de référence de Python pour dessiner des graphiques ; c'est aussi
la base de `seaborn`, `pandas` et de beaucoup d'outils de data science.

## 2. Installation

```powershell
python -m pip install matplotlib
```

```python
import matplotlib.pyplot as plt  # alias conventionnel : plt
```

## 3. Pas à pas

### 3.1 Première courbe

```python
mois = [1, 2, 3, 4, 5, 6]
ventes = [120, 150, 130, 180, 210, 190]

plt.plot(mois, ventes)
plt.show()  # ouvre une fenêtre
```

### 3.2 Habiller le graphique

```python
plt.plot(mois, ventes, marker="o", color="green", label="Boutique A")
plt.title("Ventes du semestre")
plt.xlabel("Mois")
plt.ylabel("Ventes (milliers de FCFA)")
plt.grid(True)
plt.legend()
plt.savefig("ventes.png", dpi=150)  # enregistre une image
plt.show()
```

### 3.3 L'interface « objet » (à privilégier)

```python
fig, ax = plt.subplots(figsize=(8, 4))  # une figure et un jeu d'axes
ax.plot(mois, ventes, marker="o")
ax.set_title("Ventes du semestre")
ax.set_xlabel("Mois")
ax.set_ylabel("Ventes")
fig.savefig("ventes.png")
```

`fig` est la **feuille**, `ax` le **repère** (axes) où l'on dessine. Cette forme est plus claire dès qu'on a
plusieurs graphiques, et c'est elle qu'utilisent les exercices.

### 3.4 Diagramme en barres

```python
produits = ["Manioc", "Riz", "Sel", "Huile"]
quantites = [40, 25, 60, 15]

fig, ax = plt.subplots()
ax.bar(produits, quantites, color="orange")
ax.set_title("Stock par produit")
ax.set_ylabel("Quantité")
```

Barres horizontales : `ax.barh(...)`.

### 3.5 Histogramme : la distribution des valeurs

```python
notes = [8, 9, 10, 10, 11, 12, 12, 12, 13, 14, 15, 15, 16, 18]
fig, ax = plt.subplots()
ax.hist(notes, bins=5, edgecolor="black")
ax.set_title("Répartition des notes")
```

Un histogramme **regroupe** les valeurs en intervalles (« classes ») et compte combien tombent dans chacun.

### 3.6 Nuage de points

```python
heures = [1, 2, 3, 4, 5, 6]
notes = [8, 11, 12, 14, 16, 17]
fig, ax = plt.subplots()
ax.scatter(heures, notes)
ax.set_xlabel("Heures de révision")
ax.set_ylabel("Note")
```

### 3.7 Camembert

```python
fig, ax = plt.subplots()
ax.pie([50, 30, 20], labels=["Manioc", "Riz", "Autres"], autopct="%1.0f%%")
```

### 3.8 Plusieurs graphiques dans une figure

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  # 1 ligne, 2 colonnes
ax1.plot(mois, ventes)
ax1.set_title("Courbe")
ax2.bar(mois, ventes)
ax2.set_title("Barres")
fig.tight_layout()
```

### 3.9 Choisir le bon graphique

| Je veux montrer… | Graphique |
|---|---|
| une évolution dans le temps | courbe (`plot`) |
| comparer des catégories | barres (`bar`) |
| la répartition d'une variable | histogramme (`hist`) |
| la relation entre deux variables | nuage de points (`scatter`) |
| des parts d'un tout (peu de catégories) | camembert (`pie`) |

### 3.10 Bonnes pratiques

- Un **titre** et des **étiquettes d'axes** (avec l'unité) toujours.
- Pas plus de 5-6 couleurs ; choisis des couleurs lisibles.
- Barres : l'axe vertical commence à **0** (sinon l'image trompe).
- Évite les camemberts à beaucoup de parts : préfère des barres.

## 4. ⚠️ Pièges courants

- **Oublier `plt.show()`** dans un script : rien ne s'affiche.
- **Listes de tailles différentes** : `ValueError: x and y must have same first dimension`.
- **Plusieurs graphiques qui se superposent** : crée une nouvelle figure avec `plt.subplots()` ou ferme-la
  avec `plt.close(fig)`.
- **Serveur sans écran** : utilise `matplotlib.use("Agg")` et enregistre avec `savefig`.
- **Accents mal affichés** : en général OK avec les polices récentes ; sinon change de police.

## 5. À retenir

- `fig, ax = plt.subplots()` puis `ax.plot / bar / hist / scatter / pie`.
- `ax.set_title`, `set_xlabel`, `set_ylabel`, `legend`, `grid`.
- `fig.savefig("fichier.png")` pour enregistrer ; `plt.show()` pour afficher.
- Choisis le type de graphique selon le message à faire passer.

## 6. Exercices

Fichier : [`exercices/ex33_matplotlib.py`](../exercices/ex33_matplotlib.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex33_matplotlib.py -v
```

## 7. Quiz

1. Que représentent `fig` et `ax` ?
2. Quel graphique pour comparer le stock de 4 produits ?
3. À quoi sert `bins` dans `hist` ?
4. Pourquoi l'axe d'un diagramme en barres doit-il commencer à 0 ?

<details>
<summary>Réponses</summary>

1. `fig` est la figure entière (la feuille), `ax` le repère dans lequel on dessine.
2. Un diagramme en barres.
3. Au nombre d'intervalles (classes) dans lesquels regrouper les valeurs.
4. Sinon les différences paraissent plus grandes qu'elles ne le sont.

</details>

<!-- cadre:fin -->
---

## 🎉 Bravo !

Tu sais maintenant dessiner les principaux graphiques de la data. Chaque chiffre peut désormais devenir une image.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 9.3 — Représenter une fonction mathématique](l34_fonctions_mathematiques.md).
<!-- /cadre:fin -->
