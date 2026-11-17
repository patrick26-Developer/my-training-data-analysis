"""Programme principal : menu en console.

Lancement depuis la racine du dépôt :
    python -m parcours.p01_python_fondamentaux.projets.synthese_boutique.main
"""

from pathlib import Path

from . import affichage, stockage, ventes
from . import stock as gestion_stock

FICHIER = Path(__file__).resolve().parent / "boutique.json"


def lire_nombre(question: str, type_=float):
    """Redemande tant que la saisie n'est pas un nombre valide."""
    while True:
        try:
            return type_(input(question).replace(",", "."))
        except ValueError:
            print("Merci de saisir un nombre valide.")


def menu() -> None:
    stock, journal = stockage.charger(FICHIER)
    while True:
        print("\n=== BOUTIQUE ===")
        print("1 Ajouter un produit   2 Vendre   3 Voir le stock   4 Alertes")
        print("5 Chiffre d'affaires   6 Exporter CSV   q Quitter")
        choix = input("Choix : ").strip().lower()
        try:
            match choix:
                case "1":
                    nom = input("Nom : ")
                    prix = lire_nombre("Prix : ")
                    quantite = lire_nombre("Quantité : ", int)
                    gestion_stock.ajouter_produit(
                        stock, gestion_stock.creer_produit(nom, prix, quantite)
                    )
                    print("Produit enregistré.")
                case "2":
                    client = input("Client : ")
                    produit = input("Produit : ")
                    quantite = lire_nombre("Quantité : ", int)
                    vente = ventes.enregistrer_vente(stock, journal, client, produit, quantite)
                    print(affichage.formater_recu(vente))
                case "3":
                    print(affichage.formater_stock(stock))
                case "4":
                    alertes = gestion_stock.produits_en_alerte(stock)
                    print("Stock bas : " + ", ".join(alertes) if alertes else "Aucune alerte.")
                case "5":
                    print(f"Chiffre d'affaires : {ventes.chiffre_d_affaires(journal):,.0f} FCFA")
                    print("Meilleur client :", ventes.meilleur_client(journal))
                case "6":
                    nombre = stockage.exporter_journal_csv(FICHIER.with_name("ventes.csv"), journal)
                    print(f"{nombre} vente(s) exportée(s).")
                case "q":
                    stockage.sauvegarder(FICHIER, stock, journal)
                    print("Données sauvegardées. Au revoir !")
                    break
                case _:
                    print("Choix invalide.")
        except (ValueError, gestion_stock.StockError) as erreur:
            print("⚠", erreur)


if __name__ == "__main__":
    menu()
