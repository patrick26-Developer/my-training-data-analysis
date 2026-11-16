"""Mini-projet du module 1 — La caisse du marché (solution de référence).

Lancement :  python parcours/p01_python_fondamentaux/projets/m1_caisse_du_marche.py
"""

PARITE_FCFA_EURO = 655.957
SEUIL_REMISE = 10_000
TAUX_REMISE = 5  # en pourcentage


def main() -> None:
    print("=" * 36)
    print("   BOUTIQUE MAMA NZONI — BRAZZAVILLE")
    print("=" * 36)

    client = input("Nom du client : ").strip().title()
    produit = input("Produit : ").strip().title()
    prix = float(input("Prix unitaire (FCFA) : ").replace(",", "."))
    quantite = int(input("Quantité : "))

    sous_total = prix * quantite
    remise = 0.0
    if sous_total > SEUIL_REMISE:  # les conditions sont vues au module 2
        remise = sous_total * TAUX_REMISE / 100
    total = sous_total - remise

    print()
    print(f"Client : {client}")
    print("-" * 36)
    print(f"{'Produit':<14}{'Qté':>5}{'Prix':>8}{'Total':>9}")
    print(f"{produit:<14}{quantite:>5}{prix:>8,.0f}{sous_total:>9,.0f}")
    print("-" * 36)
    print(f"{'Remise':<27}{-remise:>9,.0f}")
    print(f"{'TOTAL (FCFA)':<27}{total:>9,.0f}")
    print(f"{'TOTAL (EUR)':<27}{total / PARITE_FCFA_EURO:>9,.2f}")
    print("=" * 36)
    print("Merci et à bientôt !")


if __name__ == "__main__":
    main()
