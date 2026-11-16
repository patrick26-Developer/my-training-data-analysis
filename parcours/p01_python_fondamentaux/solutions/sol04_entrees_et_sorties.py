"""Solutions 1.4 — Entrées et sorties."""


def demander_prenom() -> str:
    prenom = input("Prénom : ")
    return prenom.strip().title()


def _lire_decimal(question: str) -> float:
    """Lit un nombre décimal, en acceptant la virgule ou le point."""
    return float(input(question).replace(",", "."))


def additionner_saisies() -> float:
    premier = _lire_decimal("Premier nombre : ")
    second = _lire_decimal("Second nombre : ")
    return premier + second


def total_saisi() -> float:
    prix = _lire_decimal("Prix unitaire : ")
    quantite = int(input("Quantité : "))
    return prix * quantite


def saluer_utilisateur() -> None:
    nom = input("Nom : ").strip().title()
    print(f"Mbote, {nom} !")


def recu(client: str, quantite: int, total: float) -> str:
    lignes = [
        f"Client   : {client}",
        f"Quantité : {quantite}",
        f"Total    : {total:,.0f} FCFA",
    ]
    return "\n".join(lignes)
