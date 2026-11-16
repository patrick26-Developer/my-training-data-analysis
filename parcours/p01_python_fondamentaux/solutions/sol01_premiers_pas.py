"""Solutions 1.1 — Ton premier programme."""


def message_bienvenue() -> str:
    return "Bienvenue à Mayele Python Académie !"


def salutation(prenom: str) -> str:
    # On colle trois morceaux de texte avec +.
    return "Mbote, " + prenom + " !"
    # Version plus moderne (leçon 1.3) : return f"Mbote, {prenom} !"


def afficher_produit() -> None:
    # sep remplace l'espace par " : " entre les deux premiers éléments,
    # mais s'applique à tous : on construit donc la ligne en deux temps.
    print("Manioc", "500", sep=" : ", end=" ")
    print("FCFA")


def afficher_adresse() -> None:
    print("Boutique Mama Nzoni")
    print("Brazzaville")


def carte_de_visite(nom: str, ville: str) -> str:
    return nom + "\n" + ville
