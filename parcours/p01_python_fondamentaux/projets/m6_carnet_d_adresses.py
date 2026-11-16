"""Mini-projet du module 6 — Carnet d'adresses persistant (solution de référence).

Les contacts sont enregistrés dans carnet.json à côté de ce script.
Lancement :  python parcours/p01_python_fondamentaux/projets/m6_carnet_d_adresses.py
"""

import json
from pathlib import Path

FICHIER = Path(__file__).resolve().parent / "carnet.json"


def charger(chemin: Path = FICHIER) -> list[dict]:
    try:
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠ Fichier corrompu : on repart d'un carnet vide.")
        return []


def sauvegarder(contacts: list[dict], chemin: Path = FICHIER) -> None:
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def ajouter(contacts: list[dict], nom: str, telephone: str) -> None:
    nom = nom.strip().title()
    if not nom or not telephone.strip():
        raise ValueError("Le nom et le téléphone sont obligatoires.")
    contacts.append({"nom": nom, "telephone": telephone.strip()})


def rechercher(contacts: list[dict], motif: str) -> list[dict]:
    return [c for c in contacts if motif.lower() in c["nom"].lower()]


def supprimer(contacts: list[dict], nom: str) -> bool:
    for contact in contacts:
        if contact["nom"].lower() == nom.strip().lower():
            contacts.remove(contact)
            return True
    return False


def main() -> None:
    contacts = charger()
    while True:
        print("\n1 Ajouter  2 Lister  3 Rechercher  4 Supprimer  q Quitter")
        choix = input("Choix : ").strip().lower()
        match choix:
            case "1":
                try:
                    ajouter(contacts, input("Nom : "), input("Téléphone : "))
                    sauvegarder(contacts)
                    print("Contact ajouté.")
                except ValueError as erreur:
                    print("Erreur :", erreur)
            case "2":
                for c in sorted(contacts, key=lambda c: c["nom"]):
                    print(f"{c['nom']:<20}{c['telephone']}")
            case "3":
                for c in rechercher(contacts, input("Recherche : ")):
                    print(f"{c['nom']:<20}{c['telephone']}")
            case "4":
                if supprimer(contacts, input("Nom exact : ")):
                    sauvegarder(contacts)
                    print("Supprimé.")
                else:
                    print("Introuvable.")
            case "q":
                break
            case _:
                print("Choix invalide.")


if __name__ == "__main__":
    main()
