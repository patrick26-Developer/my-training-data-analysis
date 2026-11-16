"""Solutions 2.3 — match / case."""


def action_menu(choix: str) -> str:
    match choix:
        case "1":
            return "ajouter"
        case "2":
            return "supprimer"
        case "3":
            return "afficher"
        case "q" | "Q":
            return "quitter"
        case _:
            return "inconnu"


def type_de_jour(jour: str) -> str:
    match jour:
        case "lundi" | "mardi" | "mercredi" | "jeudi" | "vendredi":
            return "semaine"
        case "samedi" | "dimanche":
            return "week-end"
        case _:
            return "inconnu"


def jours_du_mois(mois: int) -> int:
    match mois:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 28
        case _:
            return 0


def operateur(indicatif: str) -> str:
    match indicatif:
        case "04":
            return "MTN"
        case "05" | "06":
            return "Airtel"
        case _:
            return "Inconnu"


def calculer(a: float, operation: str, b: float) -> float | None:
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/" if b != 0:
            return a / b
        case _:
            return None


def statut_commande(quantite: int) -> str:
    match quantite:
        case 0:
            return "vide"
        case q if q < 0:
            return "invalide"
        case q if q < 10:
            return "normale"
        case _:
            return "grosse"
