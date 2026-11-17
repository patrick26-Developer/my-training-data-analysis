"""Persistance : sauvegarde et chargement JSON, export CSV."""

import csv
import json
from os import PathLike
from pathlib import Path

Chemin = str | PathLike[str]


def sauvegarder(chemin: Chemin, stock: dict, journal: list[dict]) -> None:
    """Enregistre le stock et le journal dans un fichier JSON lisible."""
    Path(chemin).parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump({"stock": stock, "journal": journal}, f, ensure_ascii=False, indent=2)


def charger(chemin: Chemin) -> tuple[dict, list[dict]]:
    """Recharge (stock, journal). Fichier absent ou invalide : données vides."""
    try:
        with open(chemin, encoding="utf-8") as f:
            donnees = json.load(f)
        return donnees["stock"], donnees["journal"]
    except (FileNotFoundError, json.JSONDecodeError, KeyError, TypeError):
        return {}, []


def exporter_journal_csv(chemin: Chemin, journal: list[dict]) -> int:
    """Exporte le journal des ventes en CSV ; retourne le nombre de lignes écrites."""
    colonnes = ["date", "client", "produit", "quantite", "prix", "remise", "total"]
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        ecrivain = csv.DictWriter(f, fieldnames=colonnes)
        ecrivain.writeheader()
        ecrivain.writerows(journal)
    return len(journal)
