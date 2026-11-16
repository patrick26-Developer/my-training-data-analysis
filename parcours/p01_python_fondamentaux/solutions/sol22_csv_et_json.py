"""Solutions 6.3 — CSV et JSON."""

import csv
import json
from os import PathLike
from typing import Any

Chemin = str | PathLike[str]


def ecrire_stock_csv(chemin: Chemin, produits: list[dict]) -> None:
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        ecrivain = csv.DictWriter(f, fieldnames=["nom", "prix", "quantite"])
        ecrivain.writeheader()
        ecrivain.writerows(produits)


def lire_stock_csv(chemin: Chemin) -> list[dict]:
    produits = []
    with open(chemin, newline="", encoding="utf-8") as f:
        for ligne in csv.DictReader(f):
            produits.append(
                {
                    "nom": ligne["nom"],
                    "prix": int(ligne["prix"]),
                    "quantite": int(ligne["quantite"]),
                }
            )
    return produits


def valeur_totale_csv(chemin: Chemin) -> int:
    return sum(p["prix"] * p["quantite"] for p in lire_stock_csv(chemin))


def sauvegarder_json(chemin: Chemin, donnees: Any) -> None:
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)


def charger_json(chemin: Chemin, defaut: Any = None) -> Any:
    try:
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return defaut


def compter_par_ville(chemin: Chemin) -> dict[str, int]:
    compteur: dict[str, int] = {}
    with open(chemin, newline="", encoding="utf-8") as f:
        for ligne in csv.DictReader(f):
            ville = ligne["ville"]
            compteur[ville] = compteur.get(ville, 0) + 1
    return compteur


def csv_vers_json(chemin_csv: Chemin, chemin_json: Chemin) -> None:
    with open(chemin_csv, newline="", encoding="utf-8") as f:
        lignes = [dict(ligne) for ligne in csv.DictReader(f)]
    sauvegarder_json(chemin_json, lignes)


def ajouter_produit_json(chemin: Chemin, produit: dict) -> int:
    produits = charger_json(chemin, defaut=[])
    produits.append(produit)
    sauvegarder_json(chemin, produits)
    return len(produits)
