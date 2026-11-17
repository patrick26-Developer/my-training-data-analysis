"""Mise en forme des reçus et des tableaux."""

PARITE_FCFA_EURO = 655.957
LARGEUR = 40


def formater_recu(vente: dict) -> str:
    """Retourne le reçu d'une vente sous forme de texte aligné."""
    sous_total = vente["prix"] * vente["quantite"]
    lignes = [
        "=" * LARGEUR,
        "BOUTIQUE MAMA NZONI — BRAZZAVILLE".center(LARGEUR),
        "=" * LARGEUR,
        f"Date   : {vente['date']}",
        f"Client : {vente['client']}",
        "-" * LARGEUR,
        f"{'Produit':<16}{'Qté':>5}{'Prix':>9}{'Total':>10}",
        f"{vente['produit']:<16}{vente['quantite']:>5}{vente['prix']:>9,.0f}{sous_total:>10,.0f}",
        "-" * LARGEUR,
        f"{'Remise':<30}{-vente['remise']:>10,.0f}",
        f"{'TOTAL (FCFA)':<30}{vente['total']:>10,.0f}",
        f"{'TOTAL (EUR)':<30}{vente['total'] / PARITE_FCFA_EURO:>10,.2f}",
        "=" * LARGEUR,
    ]
    return "\n".join(lignes)


def formater_stock(stock: dict) -> str:
    """Retourne le stock sous forme de tableau trié par nom."""
    if not stock:
        return "Stock vide."
    lignes = [f"{'Produit':<18}{'Prix':>9}{'Qté':>6}"]
    for produit in sorted(stock.values(), key=lambda p: p["nom"]):
        lignes.append(f"{produit['nom']:<18}{produit['prix']:>9,.0f}{produit['quantite']:>6}")
    return "\n".join(lignes)
