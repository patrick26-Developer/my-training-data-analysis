"""Mini-projet du module 4 — Gestionnaire de stock en console (solution de référence).

Le stock est une liste de dictionnaires {"nom", "prix", "quantite"}.
Lancement :  python parcours/p01_python_fondamentaux/projets/m4_gestionnaire_de_stock.py
"""

Stock = list[dict]


def chercher(stock: Stock, nom: str) -> dict | None:
    for produit in stock:
        if produit["nom"].lower() == nom.lower():
            return produit
    return None


def ajouter(stock: Stock, nom: str, prix: float, quantite: int) -> None:
    existant = chercher(stock, nom)
    if existant:
        existant["quantite"] += quantite
        existant["prix"] = prix
    else:
        stock.append({"nom": nom, "prix": prix, "quantite": quantite})


def vendre(stock: Stock, nom: str, quantite: int) -> str:
    produit = chercher(stock, nom)
    if produit is None:
        return "Produit inconnu."
    if produit["quantite"] < quantite:
        return f"Stock insuffisant ({produit['quantite']} disponible)."
    produit["quantite"] -= quantite
    return f"Vente : {quantite} x {produit['nom']} = {quantite * produit['prix']:,.0f} FCFA"


def valeur_totale(stock: Stock) -> float:
    return sum(p["prix"] * p["quantite"] for p in stock)


def lister(stock: Stock) -> str:
    if not stock:
        return "Stock vide."
    lignes = [f"{'Produit':<14}{'Prix':>8}{'Qté':>6}"]
    lignes += [f"{p['nom']:<14}{p['prix']:>8,.0f}{p['quantite']:>6}" for p in stock]
    return "\n".join(lignes)


def main() -> None:
    stock: Stock = []
    while True:
        print("\n1 Ajouter  2 Vendre  3 Lister  4 Valeur totale  5 Rechercher  q Quitter")
        choix = input("Choix : ").strip().lower()
        match choix:
            case "1":
                nom = input("Nom : ").strip().title()
                prix = float(input("Prix : "))
                quantite = int(input("Quantité : "))
                ajouter(stock, nom, prix, quantite)
            case "2":
                nom = input("Nom : ").strip()
                print(vendre(stock, nom, int(input("Quantité : "))))
            case "3":
                print(lister(stock))
            case "4":
                print(f"Valeur du stock : {valeur_totale(stock):,.0f} FCFA")
            case "5":
                produit = chercher(stock, input("Nom : ").strip())
                print(produit if produit else "Introuvable.")
            case "q":
                print("Au revoir !")
                break
            case _:
                print("Choix invalide.")


if __name__ == "__main__":
    main()
