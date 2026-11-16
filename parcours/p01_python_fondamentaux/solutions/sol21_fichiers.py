"""Solutions 6.2 — Lire et écrire des fichiers."""

from os import PathLike

Chemin = str | PathLike[str]


def ecrire_lignes(chemin: Chemin, lignes: list[str]) -> None:
    with open(chemin, "w", encoding="utf-8") as f:
        for ligne in lignes:
            f.write(ligne + "\n")


def lire_lignes(chemin: Chemin) -> list[str]:
    try:
        with open(chemin, encoding="utf-8") as f:
            return [ligne.strip() for ligne in f if ligne.strip()]
    except FileNotFoundError:
        return []


def ajouter_ligne(chemin: Chemin, ligne: str) -> None:
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")


def compter_lignes(chemin: Chemin) -> int:
    compteur = 0
    try:
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                if ligne.strip():
                    compteur += 1
    except FileNotFoundError:
        return 0
    return compteur


def compter_mots(chemin: Chemin) -> int:
    total = 0
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:
            total += len(ligne.split())
    return total


def valeur_du_stock(chemin: Chemin) -> int:
    total = 0
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:
            if not ligne.strip():
                continue
            _produit, prix, quantite = ligne.strip().split(";")
            total += int(prix) * int(quantite)
    return total


def copier_en_majuscules(source: Chemin, destination: Chemin) -> None:
    with open(source, encoding="utf-8") as entree:
        contenu = entree.read()
    with open(destination, "w", encoding="utf-8") as sortie:
        sortie.write(contenu.upper())


def derniere_ligne(chemin: Chemin) -> str | None:
    derniere = None
    try:
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                if ligne.strip():
                    derniere = ligne.strip()
    except FileNotFoundError:
        return None
    return derniere
