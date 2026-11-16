"""Mini-projet du module 2 — Bulletin de notes et tarif de transport (solution de référence).

Énoncé :
  1. Demande le nom d'un élève et ses notes de maths, français et informatique (sur 20).
  2. Calcule la moyenne, affiche la mention (voir leçon 2.2) et « Admis » / « Ajourné ».
  3. Demande ensuite l'âge de l'élève et affiche le prix de son ticket de bus :
     moins de 12 ans : 100 FCFA ; de 12 à 64 ans : 200 FCFA ; 65 ans et plus : gratuit.

Lancement :  python parcours/p01_python_fondamentaux/projets/m2_bulletin_et_tarif.py
"""


def mention(moyenne: float) -> str:
    if moyenne >= 16:
        return "Très bien"
    if moyenne >= 14:
        return "Bien"
    if moyenne >= 12:
        return "Assez bien"
    if moyenne >= 10:
        return "Passable"
    return "Ajourné"


def prix_ticket(age: int) -> int:
    if age < 12:
        return 100
    if age < 65:
        return 200
    return 0


def main() -> None:
    nom = input("Nom de l'élève : ").strip().title()
    maths = float(input("Note de maths : "))
    francais = float(input("Note de français : "))
    info = float(input("Note d'informatique : "))
    age = int(input("Âge : "))

    moyenne = (maths + francais + info) / 3
    decision = "Admis" if moyenne >= 10 else "Ajourné"

    print()
    print(f"Bulletin de {nom}")
    print(f"Moyenne : {moyenne:.2f}/20 — {mention(moyenne)} ({decision})")
    prix = prix_ticket(age)
    print("Ticket de bus : " + ("gratuit" if prix == 0 else f"{prix} FCFA"))


if __name__ == "__main__":
    main()
