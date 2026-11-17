"""Convertir objets et valeurs JSON ; aucune saisie utilisateur ici."""

import csv
import json
from dataclasses import asdict
from pathlib import Path
from tempfile import NamedTemporaryFile

from .modele import Caisse, Produit, Stock, Vente, cle


def sauvegarder(chemin, caisse):
    """Écrire un JSON versionné puis remplacer la sauvegarde précédente.

    Le fichier temporaire est placé dans le même dossier. Une erreur d'écriture
    laisse ainsi la sauvegarde précédente intacte. Ce mécanisme ne remplace pas
    une base de données pour des accès simultanés.
    """
    chemin = Path(chemin)
    donnees = {
        "version": 1,
        "stock": [
            {"nom": p.nom, "prix": p.prix, "quantite": p.quantite} for p in caisse.stock.produits
        ],
        "journal": [asdict(vente) for vente in caisse.journal],
    }
    # Sérialiser avant de toucher au disque ; refuser NaN et l'infini.
    contenu = json.dumps(donnees, ensure_ascii=False, indent=2, allow_nan=False)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    temporaire = None
    try:
        with NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=chemin.parent,
            prefix=".boutique-",
            suffix=".tmp",
            delete=False,
        ) as fichier:
            temporaire = Path(fichier.name)
            fichier.write(contenu)
        temporaire.replace(chemin)
    finally:
        if temporaire is not None:
            temporaire.unlink(missing_ok=True)


def charger(chemin):
    """Absence : caisse vide. Contenu invalide : ValueError, sans écraser le fichier.

    Accepte aussi le format P01 sans version (stock sous forme de dictionnaire).
    Les objets sont reconstruits et validés avant de retourner la caisse.
    Les erreurs d'accès au disque restent des OSError à traiter par l'interface.
    """
    try:
        contenu = Path(chemin).read_text(encoding="utf-8")
    except FileNotFoundError:
        return Caisse(Stock())
    try:
        donnees = json.loads(contenu)
        if not isinstance(donnees, dict):
            raise ValueError("Objet JSON attendu.")
        produits = donnees["stock"]
        if "version" not in donnees and isinstance(produits, dict):
            produits = list(produits.values())
        elif type(donnees.get("version")) is not int or donnees["version"] != 1:
            raise ValueError("Version de sauvegarde inconnue.")
        if not isinstance(produits, list) or not isinstance(donnees["journal"], list):
            raise ValueError("Listes de produits et de ventes attendues.")
        stock = Stock()
        deja_vus = set()
        for ligne in produits:
            produit = Produit(**ligne)
            if cle(produit.nom) in deja_vus:
                raise ValueError("Produit dupliqué dans la sauvegarde.")
            deja_vus.add(cle(produit.nom))
            stock.ajouter(produit)
        journal = [Vente(**ligne) for ligne in donnees["journal"]]
        return Caisse(stock, journal=journal)
    except (ValueError, TypeError, KeyError, AttributeError, OverflowError) as erreur:
        raise ValueError("Sauvegarde invalide : " + str(erreur)) from erreur


def exporter_journal_csv(chemin, caisse):
    """Exporter des valeurs simples, lisibles dans un tableur ; retourner le nombre de ventes."""
    chemin = Path(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    colonnes = ["date", "client", "produit", "quantite", "prix", "remise", "total"]
    with chemin.open("w", newline="", encoding="utf-8") as fichier:
        ecrivain = csv.DictWriter(fichier, fieldnames=colonnes)
        ecrivain.writeheader()
        ecrivain.writerows(asdict(vente) for vente in caisse.journal)
    return len(caisse.journal)
