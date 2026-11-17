"""Ventes : enregistrement, remises, journal, statistiques."""

from datetime import date

from .stock import Stock, retirer_du_stock

SEUIL_REMISE = 10_000  # FCFA
TAUX_REMISE = 5  # pourcentage


def calculer_remise(sous_total: float) -> float:
    """Retourne la remise : 5 % au-dessus de 10 000 FCFA, sinon 0.

    >>> calculer_remise(20000)
    1000.0
    >>> calculer_remise(10000)
    0.0
    """
    if sous_total > SEUIL_REMISE:
        return sous_total * TAUX_REMISE / 100
    return 0.0


def enregistrer_vente(
    stock: Stock,
    journal: list[dict],
    client: str,
    nom_produit: str,
    quantite: int,
    jour: date | None = None,
) -> dict:
    """Enregistre une vente : met à jour le stock et ajoute une ligne au journal.

    Returns:
        La vente (dictionnaire) ajoutée au journal.

    Raises:
        ProduitInconnuError, StockInsuffisantError, ValueError (voir `retirer_du_stock`).
    """
    produit = retirer_du_stock(stock, nom_produit, quantite)
    sous_total = produit["prix"] * quantite
    remise = calculer_remise(sous_total)
    vente = {
        "date": (jour or date.today()).isoformat(),
        "client": " ".join(client.split()).title() or "Client",
        "produit": produit["nom"],
        "quantite": quantite,
        "prix": produit["prix"],
        "remise": remise,
        "total": sous_total - remise,
    }
    journal.append(vente)
    return vente


def chiffre_d_affaires(journal: list[dict]) -> float:
    """Retourne la somme des totaux du journal."""
    return sum(v["total"] for v in journal)


def total_par_produit(journal: list[dict]) -> dict[str, float]:
    """Retourne {produit: chiffre d'affaires}, trié par chiffre décroissant."""
    totaux: dict[str, float] = {}
    for v in journal:
        totaux[v["produit"]] = totaux.get(v["produit"], 0) + v["total"]
    return dict(sorted(totaux.items(), key=lambda item: item[1], reverse=True))


def meilleur_client(journal: list[dict]) -> str | None:
    """Retourne le client qui a le plus dépensé, ou None si le journal est vide."""
    depenses: dict[str, float] = {}
    for v in journal:
        depenses[v["client"]] = depenses.get(v["client"], 0) + v["total"]
    if not depenses:
        return None
    return max(depenses, key=lambda c: depenses[c])
