"""Génère la version web de Python Fondamentaux à partir du contenu du dépôt."""

from html import escape
from pathlib import Path
from shutil import copyfile
from string import Template

import mistune

SITE = Path(__file__).resolve().parent
ROOT = SITE.parent
COURSE = ROOT / "parcours" / "p01_python_fondamentaux"
OUTPUT = ROOT / "dist"
MODULES = (
    ("Premiers pas", 4),
    ("Prendre des décisions", 7),
    ("Répéter", 10),
    ("Les collections", 15),
    ("Les fonctions", 19),
    ("Erreurs et fichiers", 23),
    ("Modules et environnement", 27),
    ("Maths et algorithmique", 31),
    ("Premiers graphiques", 35),
    ("Écrire du bon code", 39),
    ("Évaluation finale", 41),
)


class LessonRenderer(mistune.HTMLRenderer):
    def link(self, text: str, url: str, title: str | None = None) -> str:
        path = Path(url.removeprefix("../"))
        if (COURSE / "lecons" / path.name).is_file() and path.suffix == ".md":
            url = f"/lecons/{path.stem}.html"
        elif path == Path("examen_final.md"):
            url = "/lecons/examen_final.html"
        elif path.parts and path.parts[0] in {"exercices", "projets", "solutions"}:
            source = (COURSE / path).resolve()
            if source.is_relative_to(COURSE):
                relative = source.relative_to(COURSE)
                if source.is_file():
                    target = OUTPUT / "fichiers" / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    copyfile(source, target)
                    url = f"/fichiers/{relative.as_posix()}"
                elif source.is_dir():
                    url = (
                        "https://github.com/patrick26-Developer/my-training-data-analysis"
                        f"/tree/main/parcours/{COURSE.name}/{relative.as_posix()}"
                    )
        return super().link(text, url, title)

    def block_code(self, code: str, info: str | None = None) -> str:
        block = super().block_code(code, info)
        if info == "python":
            return (
                f'<div class="example">{block}<button type="button">Essayer le code</button></div>'
            )
        return block


def main() -> None:
    sources = [*sorted((COURSE / "lecons").glob("l*.md")), COURSE / "examen_final.md"]
    lessons = [(source.stem, source.read_text(encoding="utf-8-sig")) for source in sources]
    titles = [
        next(line[2:].strip() for line in body.splitlines() if line.startswith("# "))
        for _, body in lessons
    ]
    if len(lessons) != MODULES[-1][1]:
        raise ValueError("Le nombre de pages ne correspond pas au plan de P01.")

    template = Template((SITE / "page.html").read_text(encoding="utf-8"))
    markdown = mistune.create_markdown(renderer=LessonRenderer(escape=True), plugins=["table"])
    (OUTPUT / "lecons").mkdir(parents=True, exist_ok=True)
    for asset in ("style.css", "atelier.js", "python-worker.js"):
        copyfile(SITE / asset, OUTPUT / asset)

    def lesson_link(index: int, label: str | None = None, *, current: bool = False) -> str:
        slug = lessons[index][0]
        active = ' aria-current="page"' if current else ""
        return f'<a href="/lecons/{slug}.html"{active}>{escape(label or titles[index])}</a>'

    def modules(current: int | None = None) -> str:
        groups = []
        start = 0
        for name, end in MODULES:
            opened = " open" if current is not None and start <= current < end else ""
            items = "".join(
                f"<li>{lesson_link(i, current=i == current)}</li>" for i in range(start, end)
            )
            groups.append(f"<details{opened}><summary>{name}</summary><ul>{items}</ul></details>")
            start = end
        return "".join(groups)

    def write(
        path: Path, title: str, content: str, index: int | None = None, navigation: str = ""
    ) -> None:
        path.write_text(
            template.substitute(
                title=escape(title),
                modules=modules(index),
                content=content,
                navigation=navigation,
                layout="landing" if index is None else "lesson",
            ),
            encoding="utf-8",
        )

    intro = (
        '<section class="hero"><p class="eyebrow">Mayele Python Académie</p>'
        "<h1>Apprends Python<br>en pratiquant.</h1>"
        "<p>Un parcours en français pour apprendre à programmer à partir de zéro. "
        "Lis les leçons et essaie les exemples directement dans ton navigateur.</p>"
        f'<div class="actions">{lesson_link(0, "Commencer le parcours")}</div></section>'
        '<section class="curriculum"><h2>Python Fondamentaux</h2>'
        "<p>11 modules, du premier programme au projet de synthèse.</p>"
        f"{modules()}</section>"
    )
    write(OUTPUT / "index.html", "Apprendre Python", intro)
    for index, (slug, body) in enumerate(lessons):
        previous = lesson_link(index - 1, "Leçon précédente") if index > 0 else ""
        following = lesson_link(index + 1, "Leçon suivante") if index + 1 < len(lessons) else ""
        write(
            OUTPUT / "lecons" / f"{slug}.html",
            titles[index],
            f"<article>{markdown(body)}</article>",
            index,
            f'<nav class="pagination" aria-label="Navigation entre les leçons">{previous}{following}</nav>',
        )


if __name__ == "__main__":
    main()
