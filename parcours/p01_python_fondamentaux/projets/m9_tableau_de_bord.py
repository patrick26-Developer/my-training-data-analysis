"""Mini-projet du module 9 — Tableau de bord d'une boutique (solution de référence).

Lancement :  python parcours/p01_python_fondamentaux/projets/m9_tableau_de_bord.py
Produit l'image tableau_de_bord.png à côté de ce script.
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

DOSSIER = Path(__file__).resolve().parent


def lire_ventes(chemin: Path) -> list[dict]:
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


def chiffre_affaires_par_mois(ventes: list[dict]) -> dict[str, float]:
    totaux: dict[str, float] = {}
    for v in ventes:
        totaux[v["mois"]] = totaux.get(v["mois"], 0) + v["quantite"] * v["prix"]
    return dict(sorted(totaux.items()))


def chiffre_affaires_par_produit(ventes: list[dict]) -> dict[str, float]:
    totaux: dict[str, float] = {}
    for v in ventes:
        totaux[v["produit"]] = totaux.get(v["produit"], 0) + v["quantite"] * v["prix"]
    return totaux


def meilleur_produit(ventes: list[dict]) -> str:
    par_produit = chiffre_affaires_par_produit(ventes)
    return max(par_produit, key=lambda produit: par_produit[produit])


def evolution(par_mois: dict[str, float]) -> list[float]:
    valeurs = list(par_mois.values())
    return [round((b - a) / a * 100, 1) for a, b in zip(valeurs, valeurs[1:], strict=False) if a]


def tableau_de_bord(ventes: list[dict]) -> Figure:
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


def main() -> None:
    ventes = lire_ventes(DOSSIER / "donnees" / "ventes.csv")
    print("Meilleur produit :", meilleur_produit(ventes))
    print("Évolution mensuelle (%) :", evolution(chiffre_affaires_par_mois(ventes)))
    fig = tableau_de_bord(ventes)
    sortie = DOSSIER / "tableau_de_bord.png"
    fig.savefig(sortie, dpi=150)
    print("Image enregistrée :", sortie)
    plt.show()


if __name__ == "__main__":
    main()
