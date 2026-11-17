# Leçon 9.4 — Projet : le tableau de bord d'une boutique

⏱ 80 min · 🎯 Intermédiaire · 📦 Prérequis : modules 4, 6 et leçons 9.2–9.3

<!-- cadre:debut -->
> 🔥 **Pourquoi tu vas aimer cette leçon** — Tu vas bâtir un vrai tableau de bord pour une boutique : lire des ventes, calculer des indicateurs et les afficher en graphiques.
<!-- /cadre:debut -->

## 🎯 Ce que tu sauras faire

- Lire des ventes depuis un fichier **CSV**
- Calculer des **indicateurs** (totaux, moyennes, meilleur produit, évolution)
- Produire un **tableau de bord** : plusieurs graphiques dans une même image
- Enchaîner **lecture → calcul → affichage** proprement, avec des fonctions séparées

---

## 1. Le problème

Mama Nzoni a noté ses ventes dans un fichier. Elle veut savoir : quel produit rapporte le plus ? quels mois
sont les meilleurs ? la boutique progresse-t-elle ? Tu vas construire pour elle un **tableau de bord**.

## 2. Les données

Fichier `ventes.csv` (dans [`../projets/donnees/ventes.csv`](../projets/donnees/ventes.csv)) :

```
mois,produit,quantite,prix_unitaire
2026-01,Manioc,120,500
2026-01,Riz,60,800
2026-02,Manioc,150,500
...
```

## 3. Architecture : trois étapes, trois fonctions

```
   lire_ventes(chemin)  →  indicateurs(ventes)  →  tableau_de_bord(ventes)
        (CSV → liste)         (calculs)                   (graphiques)
```

Séparer ces trois rôles permet de **tester** les calculs sans dessiner, et de **réutiliser** chaque partie.

### 3.1 Lire

```python
import csv


def lire_ventes(chemin):
    ventes = []
    with open(chemin, newline="", encoding="utf-8") as f:
        for ligne in csv.DictReader(f):
            ventes.append(
                {
                    "mois": ligne["mois"],
                    "produit": ligne["produit"],
                    "quantite": int(ligne["quantite"]),
                    "prix": float(ligne["prix_unitaire"]),
                }
            )
    return ventes
```

### 3.2 Calculer

```python
def chiffre_affaires_par_mois(ventes):
    totaux = {}
    for v in ventes:
        totaux[v["mois"]] = totaux.get(v["mois"], 0) + v["quantite"] * v["prix"]
    return dict(sorted(totaux.items()))


def chiffre_affaires_par_produit(ventes):
    totaux = {}
    for v in ventes:
        totaux[v["produit"]] = totaux.get(v["produit"], 0) + v["quantite"] * v["prix"]
    return totaux


def meilleur_produit(ventes):
    par_produit = chiffre_affaires_par_produit(ventes)
    return max(par_produit, key=par_produit.get)
```

Évolution (en %) d'un mois sur l'autre :

```python
def evolution(par_mois):
    valeurs = list(par_mois.values())
    return [round((b - a) / a * 100, 1) for a, b in zip(valeurs, valeurs[1:])]
```

### 3.3 Dessiner : le tableau de bord

```python
import matplotlib.pyplot as plt


def tableau_de_bord(ventes):
    par_mois = chiffre_affaires_par_mois(ventes)
    par_produit = chiffre_affaires_par_produit(ventes)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

    ax1.plot(list(par_mois), list(par_mois.values()), marker="o")
    ax1.set_title("Chiffre d'affaires par mois")
    ax1.set_ylabel("FCFA")
    ax1.tick_params(axis="x", rotation=45)
    ax1.grid(True)

    ax2.bar(list(par_produit), list(par_produit.values()), color="orange")
    ax2.set_title("Chiffre d'affaires par produit")

    fig.suptitle("Boutique Mama Nzoni", fontsize=14)
    fig.tight_layout()
    return fig
```

### 3.4 Lancer

```python
if __name__ == "__main__":
    ventes = lire_ventes("ventes.csv")
    print("Meilleur produit :", meilleur_produit(ventes))
    fig = tableau_de_bord(ventes)
    fig.savefig("tableau_de_bord.png", dpi=150)
    plt.show()
```

## 4. Pour aller plus loin

- Ajouter une **prévision** : droite de tendance par moindres carrés (voir exercice 6).
- Un camembert des parts de chaque produit.
- Un paramètre en ligne de commande avec `argparse` pour choisir le fichier.
- Remplacer tout ce code par **pandas** (parcours P08) : tu verras la différence !

## 5. ⚠️ Pièges courants

- Oublier de convertir `quantite` et `prix` (le CSV ne donne que du texte).
- Trier les mois en tant que **textes** : le format `AAAA-MM` garantit que l'ordre alphabétique = chronologique.
- Mélanger calcul et dessin dans la même fonction : impossible à tester.
- Diviser par zéro dans `evolution` si un mois vaut 0.

## 6. À retenir

- Découpe en étapes : **lire**, **calculer**, **présenter**.
- Les calculs sont des fonctions pures, faciles à tester.
- Un tableau de bord = plusieurs graphiques cohérents avec un titre général.
- `fig.savefig` pour partager le résultat.

## 7. Exercices

Fichier : [`exercices/ex35_graphique_des_ventes.py`](../exercices/ex35_graphique_des_ventes.py)

```powershell
pytest parcours/p01_python_fondamentaux/exercices/test_ex35_graphique_des_ventes.py -v
```

Programme complet de référence : [`../projets/m9_tableau_de_bord.py`](../projets/m9_tableau_de_bord.py).

<!-- cadre:fin -->
---

## 🎉 Bravo !

Le module 9 est terminé : tu as construit un vrai tableau de bord. C'est exactement ce que font les analystes de données.

💬 *Bloqué(e) ? C'est normal et ça fait partie de l'apprentissage. Relis la section « Pièges courants », refais l'exemple en le tapant toi-même, puis demande de l'aide dans la communauté.*

**Prochaine étape :** [Leçon 10.1 — Déboguer : traquer et corriger les bugs](l36_deboguer.md).
<!-- /cadre:fin -->
