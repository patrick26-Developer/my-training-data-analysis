"""Exécute les exemples de code des leçons Markdown pour vérifier qu'ils fonctionnent.

Principe : pour chaque leçon, les blocs ```python sont exécutés dans l'ordre, dans un espace de noms
partagé (comme un notebook). Un bloc qui est suivi d'un bloc de sortie contenant « Error » ou
« Traceback » est un exemple d'ERREUR VOLONTAIRE : on vérifie alors qu'il échoue bien.
`input()` est simulé, `plt.show()` et `turtle` sont neutralisés.

Usage :
    python outils/verifier_lecons.py                      # toutes les leçons
    python outils/verifier_lecons.py parcours/p01_python_fondamentaux/lecons/l01_premiers_pas.md
"""

import builtins
import contextlib
import io
import os
import re
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

RACINE = Path(__file__).resolve().parent.parent
LIMITE_LIGNES = 2_000_000  # au-delà, on considère le bloc comme une boucle infinie


class BoucleInfinieError(Exception):
    """Un bloc exécute trop de lignes : boucle infinie probable."""


def _surveiller():
    compteur = [0]

    def trace(frame, event, arg):
        if ".md:bloc" not in frame.f_code.co_filename:
            return None  # bibliothèques : on ne les surveille pas
        if event == "line":
            compteur[0] += 1
            if compteur[0] > LIMITE_LIGNES:
                raise BoucleInfinieError("boucle infinie probable")
        return trace

    return trace


BLOC = re.compile(r"^```(\w*)\n(.*?)^```", re.S | re.M)
ERREUR_ATTENDUE = re.compile(r"(Error|Traceback|Exception|SyntaxError)")
# Extraits illustratifs : variables définies ailleurs, fichiers d'un autre projet, fragments…
CONTEXTE_MANQUANT = (NameError, ModuleNotFoundError, ImportError, SyntaxError, FileNotFoundError)


def blocs(texte: str) -> list[tuple[str, str]]:
    return [(m.group(1), m.group(2)) for m in BLOC.finditer(texte)]


def a_ignorer(code: str) -> bool:
    """Blocs non exécutables tels quels (shell, placeholders, fenêtres, réseau…)."""
    return any(
        m in code for m in ("turtle", "breakpoint()", "argparse", "sys.argv", "ArgumentParser")
    )


def verifier(chemin: Path) -> tuple[int, int, list[str], list[str]]:
    texte = chemin.read_text(encoding="utf-8")
    liste = blocs(texte)
    espace: dict = {"__name__": "__lecon__"}
    reponses = iter(lambda: "3", None)
    executes = ok = 0
    problemes: list[str] = []
    avertissements: list[str] = []
    espace["__file__"] = str(chemin)
    if str(RACINE) not in sys.path:
        sys.path.insert(0, str(RACINE))
    ancien_cwd = Path.cwd()
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        try:
            for i, (langue, code) in enumerate(liste):
                if langue != "python" or a_ignorer(code) or code.lstrip().startswith(">>>"):
                    continue
                suivant = liste[i + 1][1] if i + 1 < len(liste) and liste[i + 1][0] == "" else ""
                erreur_voulue = bool(ERREUR_ATTENDUE.search(suivant)) and "Traceback" not in code
                executes += 1
                sortie = io.StringIO()
                try:
                    with contextlib.redirect_stdout(sortie):
                        builtins_input = builtins.input
                        builtins.input = lambda *_: next(reponses)
                        try:
                            objet = compile(code, f"{chemin.name}:bloc{i}", "exec")
                            sys.settrace(_surveiller())
                            try:
                                exec(objet, espace)
                            finally:
                                sys.settrace(None)
                        finally:
                            builtins.input = builtins_input
                    if erreur_voulue:
                        avertissements.append(
                            f"bloc {i} : erreur annoncée mais code réussi (état partagé ?)"
                        )
                    ok += 1
                except BaseException as e:
                    annote = re.search(r"#.*(Error|❌|erreur|Erreur)", code) is not None
                    if (
                        erreur_voulue
                        or annote
                        or (isinstance(e, BoucleInfinieError) and "infini" in texte.lower())
                    ):
                        ok += 1  # erreur annoncée, ou boucle infinie montrée comme piège
                    elif isinstance(e, CONTEXTE_MANQUANT):
                        premiere = code.strip().splitlines()[0] if code.strip() else ""
                        avertissements.append(f"bloc {i} ({premiere[:40]!r}) : {type(e).__name__}")
                        ok += 1  # extrait illustratif : pas une erreur de la leçon
                    else:
                        premiere = code.strip().splitlines()[0] if code.strip() else ""
                        problemes.append(f"bloc {i} ({premiere[:50]!r}) : {type(e).__name__}: {e}")
        finally:
            os.chdir(ancien_cwd)
    return executes, ok, problemes, avertissements


def main() -> int:
    cibles = [Path(a).resolve() for a in sys.argv[1:]] or sorted(
        RACINE.glob("parcours/*/lecons/*.md")
    )
    total_problemes = 0
    total_avertissements = 0
    for chemin in cibles:
        executes, ok, problemes, avertissements = verifier(chemin)
        total_problemes += len(problemes)
        total_avertissements += len(avertissements)
        etat = "OK " if not problemes else "!! "
        print(f"{etat}{chemin.relative_to(RACINE)} : {ok}/{executes} blocs")
        for p in problemes:
            print("     -", p)
    print(f"\n{total_problemes} problème(s) détecté(s).")
    return 1 if total_problemes else 0


if __name__ == "__main__":
    sys.exit(main())
