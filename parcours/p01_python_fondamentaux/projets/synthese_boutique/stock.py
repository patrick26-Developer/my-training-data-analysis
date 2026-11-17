"""Gestion du stock : produits, ajout, retrait, alertes.

Un produit est un dictionnaire {"nom": str, "prix": float, "quantite": int}.
Le stock est un dictionnaire {nom_en_minuscules: produit}.
"""

Produit = dict
Stock = dict[str, Produit]


class StockError(Exception):
    """Erreur générale de gestion du stock."""


class ProduitInconnuError(StockError):
    """Le produit demandé n'existe pas."""


class StockInsuffisantError(StockError):
    """La quantité demandée dépasse le stock disponible."""


def cle(nom: str) -> str:
    """Retourne la clé normalisée d'un nom de produit (minuscules, sans espaces superflus)."""
    return " ".join(nom.split()).lower()


def creer_produit(nom: str, prix: float, quantite: int) -> Produit:
    """Crée un produit après validation des données.

    Raises:
        ValueError: si le nom est vide, le prix <= 0 ou la quantité < 0.
    """
    nom = " ".join(nom.split()).title()
    if not nom:
        raise ValueError("Le nom est obligatoire.")
    if prix <= 0:
        raise ValueError("Le prix doit être strictement positif.")
    if quantite < 0:
        raise ValueError("La quantité ne peut pas être négative.")
    return {"nom": nom, "prix": float(prix), "quantite": int(quantite)}


def ajouter_produit(stock: Stock, produit: Produit) -> None:
    """Ajoute un produit ; s'il existe déjà, cumule la quantité et met à jour le prix."""
    existant = stock.get(cle(produit["nom"]))
    if existant:
        existant["quantite"] += produit["quantite"]
        existant["prix"] = produit["prix"]
    else:
        stock[cle(produit["nom"])] = produit


def trouver(stock: Stock, nom: str) -> Produit:
    """Retourne le produit ou lève ProduitInconnuError."""
    try:
        return stock[cle(nom)]
    except KeyError:
        raise ProduitInconnuError(f"Produit inconnu : {nom!r}") from None


def retirer_du_stock(stock: Stock, nom: str, quantite: int) -> Produit:
    """Retire `quantite` unités du produit et retourne le produit.

    Raises:
        ValueError: quantité <= 0.
        ProduitInconnuError: produit absent.
        StockInsuffisantError: stock insuffisant.
    """
    if quantite <= 0:
        raise ValueError("La quantité doit être strictement positive.")
    produit = trouver(stock, nom)
    if produit["quantite"] < quantite:
        raise StockInsuffisantError(
            f"Stock insuffisant pour {produit['nom']} : {produit['quantite']} disponible(s)."
        )
    produit["quantite"] -= quantite
    return produit


def valeur_du_stock(stock: Stock) -> float:
    """Retourne la valeur totale du stock (prix x quantité)."""
    return sum(p["prix"] * p["quantite"] for p in stock.values())


def produits_en_alerte(stock: Stock, seuil: int = 5) -> list[str]:
    """Retourne les noms (triés) des produits dont la quantité est <= seuil."""
    return sorted(p["nom"] for p in stock.values() if p["quantite"] <= seuil)
