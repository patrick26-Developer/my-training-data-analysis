"""Mini-projet du module 5 — La caisse en fonctions (solution de référence).

Reprend la caisse du marché en la découpant en petites fonctions, et tient un journal des ventes.
Lancement :  python parcours/p01_python_fondamentaux/projets/m5_caisse_en_fonctions.py
"""

PARITE_FCFA_EURO = 655.957
SEUIL_REMISE = 10_000
TAUX_REMISE = 5


def calculer_remise(sous_total: float) -> float:
    """Retourne le montant de la remise (5 % au-dessus de 10 000 FCFA)."""
    if sous_total > SEUIL_REMISE:
        return sous_total * TAUX_REMISE / 100
    return 0.0


def calculer_vente(produit: str, prix: float, quantite: int) -> dict:
    """Retourne le détail d'une vente sous forme de dictionnaire."""
    sous_total = prix * quantite
    remise = calculer_remise(sous_total)
    return {
        "produit": produit,
        "prix": prix,
        "quantite": quantite,
        "remise": remise,
        "total": sous_total - remise,
    }


def formater_recu(client: str, vente: dict) -> str:
    """Retourne le reçu sous forme de texte aligné."""
    lignes = [
        "=" * 36,
        f"Client : {client}",
        "-" * 36,
        f"{'Produit':<14}{'Qté':>5}{'Prix':>8}{'Total':>9}",
        f"{vente['produit']:<14}{vente['quantite']:>5}{vente['prix']:>8,.0f}"
        f"{vente['prix'] * vente['quantite']:>9,.0f}",
        f"{'Remise':<27}{-vente['remise']:>9,.0f}",
        f"{'TOTAL (FCFA)':<27}{vente['total']:>9,.0f}",
        f"{'TOTAL (EUR)':<27}{vente['total'] / PARITE_FCFA_EURO:>9,.2f}",
        "=" * 36,
    ]
    return "\n".join(lignes)


def total_du_journal(journal: list[dict]) -> float:
    return sum(v["total"] for v in journal)


def lire_vente() -> tuple[str, dict]:
    client = input("Client : ").strip().title()
    produit = input("Produit : ").strip().title()
    prix = float(input("Prix unitaire : ").replace(",", "."))
    quantite = int(input("Quantité : "))
    return client, calculer_vente(produit, prix, quantite)


def main() -> None:
    journal: list[dict] = []
    while True:
        client, vente = lire_vente()
        journal.append(vente)
        print(formater_recu(client, vente))
        if input("Autre vente ? (o/n) ").strip().lower() != "o":
            break
    print(f"\n{len(journal)} vente(s) — total du jour : {total_du_journal(journal):,.0f} FCFA")


if __name__ == "__main__":
    main()
