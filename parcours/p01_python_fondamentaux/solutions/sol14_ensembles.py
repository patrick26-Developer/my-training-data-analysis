"""Solutions 4.4 — Les ensembles."""


def nb_differents(elements: list) -> int:
    return len(set(elements))


def communs(boutique_a: list[str], boutique_b: list[str]) -> list[str]:
    return sorted(set(boutique_a) & set(boutique_b))


def seulement_chez_a(boutique_a: list[str], boutique_b: list[str]) -> list[str]:
    return sorted(set(boutique_a) - set(boutique_b))


def mot_valide(mot: str, lettres_permises: str) -> bool:
    return set(mot) <= set(lettres_permises)


def est_pangramme(phrase: str) -> bool:
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(phrase.lower())


def doublons(elements: list) -> list:
    vus = set()
    repetes = set()
    for e in elements:
        if e in vus:
            repetes.add(e)
        vus.add(e)
    return sorted(repetes)


def anagrammes(a: str, b: str) -> bool:
    lettres_a = sorted(a.lower().replace(" ", ""))
    lettres_b = sorted(b.lower().replace(" ", ""))
    return lettres_a == lettres_b
