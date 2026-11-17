"""Console : lancer avec python -m parcours.p02_poo_et_conception.projets.boutique_objets.main."""

import argparse
from pathlib import Path

from .modele import Produit
from .stockage import charger, exporter_journal_csv, sauvegarder


def lire_nombre(question, type_=float):
    while True:
        try:
            return type_(input(question).replace(",", "."))
        except ValueError:
            print("Merci de saisir un nombre valide.")


def menu(chemin):
    """Retourner 0 après sauvegarde ; 1 si le chargement est impossible."""
    chemin = Path(chemin)
    try:
        caisse = charger(chemin)
    except (ValueError, OSError, UnicodeError) as erreur:
        print(f"Chargement impossible : {erreur}")
        return 1
    while True:
        print("\n=== BOUTIQUE OBJETS ===")
        print(
            "1 Ajouter  2 Vendre  3 Stock  4 Alertes  5 Statistiques  6 Export CSV  q Sauver et quitter"
        )
        try:
            choix = input("Choix : ").strip().lower()
            match choix:
                case "1":
                    nom = input("Nom : ")
                    prix = lire_nombre("Prix : ")
                    quantite = lire_nombre("Quantité : ", int)
                    caisse.stock.ajouter(Produit(nom, prix, quantite))
                    print("Produit enregistré.")
                case "2":
                    client = input("Client : ")
                    nom = input("Produit : ")
                    quantite = lire_nombre("Quantité : ", int)
                    vente = caisse.vendre(client, nom, quantite)
                    print(f"{vente.client} : {vente.quantite} x {vente.produit}")
                    print(f"Remise : {vente.remise:.2f} FCFA ; total : {vente.total:.2f} FCFA")
                case "3":
                    for produit in caisse.stock.produits:
                        print(
                            f"{produit.nom} : {produit.prix:.2f} FCFA ; quantité {produit.quantite}"
                        )
                    print(f"Valeur du stock : {caisse.stock.valeur():.2f} FCFA")
                case "4":
                    print("Stock bas : " + ", ".join(caisse.stock.alertes()))
                case "5":
                    print(f"Chiffre d'affaires : {caisse.chiffre_affaires():.2f} FCFA")
                    print("Meilleur client :", caisse.meilleur_client())
                    for nom, total in caisse.total_par_produit().items():
                        print(f"{nom} : {total:.2f} FCFA")
                case "6":
                    nombre = exporter_journal_csv(chemin.with_suffix(".csv"), caisse)
                    print(f"{nombre} vente(s) exportée(s).")
                case "q":
                    sauvegarder(chemin, caisse)
                    print("Données sauvegardées. Au revoir !")
                    return 0
                case _:
                    print("Choix inconnu.")
        except KeyError:
            print("Produit inconnu.")
        except (ValueError, OSError) as erreur:
            print(f"Opération refusée : {erreur}")
        except (EOFError, KeyboardInterrupt):
            print("\nSession interrompue ; changements non sauvegardés.")
            return 1


def main():
    analyseur = argparse.ArgumentParser(description="Boutique objet P02")
    analyseur.add_argument(
        "--fichier", type=Path, default=Path(__file__).with_name("boutique.json")
    )
    options = analyseur.parse_args()
    return menu(options.fichier)


if __name__ == "__main__":
    raise SystemExit(main())
