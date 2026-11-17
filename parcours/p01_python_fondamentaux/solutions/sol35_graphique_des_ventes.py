"""Solutions 9.4 — Tableau de bord d'une boutique."""

import csv
from os import PathLike

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

Vente = dict


def lire_ventes(chemin: str | PathLike[str]) -> list[Vente]:
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


def chiffre_affaires_par_mois(ventes: list[Vente]) -> dict[str, float]:
    totaux: dict[str, float] = {}
    for v in ventes:
        totaux[v["mois"]] = totaux.get(v["mois"], 0) + v["quantite"] * v["prix"]
    return dict(sorted(totaux.items()))


def chiffre_affaires_par_produit(ventes: list[Vente]) -> dict[str, float]:
    totaux: dict[str, float] = {}
    for v in ventes:
        totaux[v["produit"]] = totaux.get(v["produit"], 0) + v["quantite"] * v["prix"]
    return totaux


def meilleur_produit(ventes: list[Vente]) -> str:
    par_produit = chiffre_affaires_par_produit(ventes)
    return max(par_produit, key=lambda produit: par_produit[produit])


def evolution(par_mois: dict[str, float]) -> list[float]:
    valeurs = list(par_mois.values())
    resultat = []
    for ancien, nouveau in zip(valeurs, valeurs[1:], strict=False):
        if ancien != 0:
            resultat.append(round((nouveau - ancien) / ancien * 100, 1))
    return resultat


def droite_de_tendance(valeurs: list[float]) -> tuple[float, float]:
    n = len(valeurs)
    xs = range(n)
    somme_x = sum(xs)
    somme_y = sum(valeurs)
    somme_xy = sum(x * y for x, y in zip(xs, valeurs, strict=True))
    somme_x2 = sum(x * x for x in xs)
    a = (n * somme_xy - somme_x * somme_y) / (n * somme_x2 - somme_x**2)
    b = (somme_y - a * somme_x) / n
    return round(a, 4) + 0.0, round(b, 4) + 0.0


def prevision(valeurs: list[float], mois_suivants: int = 1) -> float:
    a, b = droite_de_tendance(valeurs)
    x = len(valeurs) + mois_suivants - 1
    return round(a * x + b, 2)


def tableau_de_bord(ventes: list[Vente]) -> Figure:
    par_mois = chiffre_affaires_par_mois(ventes)
    par_produit = chiffre_affaires_par_produit(ventes)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
    ax1.plot(list(par_mois), list(par_mois.values()), marker="o")
    ax1.set_title("Chiffre d'affaires par mois")
    ax2.bar(list(par_produit), list(par_produit.values()))
    ax2.set_title("Chiffre d'affaires par produit")
    fig.suptitle("Boutique Mama Nzoni")
    return fig
