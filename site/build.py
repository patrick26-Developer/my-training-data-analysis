"""Génère le catalogue de l'académie et les leçons des parcours disponibles."""

from html import escape
from pathlib import Path
from re import MULTILINE, findall
from shutil import copyfile
from string import Template
from urllib.parse import urlsplit

import mistune

SITE = Path(__file__).resolve().parent
ROOT = SITE.parent
COURSE = ROOT / "parcours" / "p01_python_fondamentaux"
OUTPUT = ROOT / "dist"
REPOSITORY = "https://github.com/patrick26-Developer/my-training-data-analysis"
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
    def __init__(self, course: Path, prefix: str, pages: dict[Path, str]) -> None:
        super().__init__(escape=True)
        self.course = course
        self.prefix = prefix
        self.pages = pages
        self.sections: list[tuple[str, str]] = []

    def heading(self, text: str, level: int, **attrs: str) -> str:
        if level == 2:
            anchor = f"section-{len(self.sections) + 1}"
            self.sections.append((anchor, text))
            return super().heading(text, level, id=anchor)
        return super().heading(text, level, **attrs)

    def link(self, text: str, url: str, title: str | None = None) -> str:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path:
            return super().link(text, url, title)
        source = (self.source.parent / parts.path).resolve()
        if source in self.pages:
            url = self.pages[source] + (f"#{parts.fragment}" if parts.fragment else "")
        elif source.is_relative_to(self.course) and source.exists():
            relative = source.relative_to(self.course).as_posix()
            folder = f"parcours/{self.course.name}/{relative}"
            if source.is_file() and source.suffix != ".md":
                target = OUTPUT / f"fichiers/{self.prefix}{relative}"
                target.parent.mkdir(parents=True, exist_ok=True)
                copyfile(source, target)
                url = f"/fichiers/{self.prefix}{relative}"
            else:
                kind = "tree" if source.is_dir() else "blob"
                url = f"{REPOSITORY}/{kind}/main/{folder}"
                if parts.fragment:
                    url += f"#{parts.fragment}"
        return super().link(text, url, title)

    def block_code(self, code: str, info: str | None = None) -> str:
        block = super().block_code(code, info)
        if info == "python":
            return (
                f'<div class="example">{block}<button type="button">Essayer le code</button></div>'
            )
        return block


def course_cards(first_lessons: dict[str, str]) -> str:
    syllabus = (ROOT / "docs" / "CURSUS.md").read_text(encoding="utf-8-sig")
    courses = findall(r"^\| (P\d{2}) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|", syllabus, MULTILINE)
    if not courses:
        raise ValueError("Le tableau des parcours est absent du cursus.")
    cards = []
    for code, title, cycle, level in courses:
        status, label, link = "planned", "Planifié", ""
        if code in first_lessons:
            status, label = (
                ("in-progress", "En cours") if code == "P03" else ("online", "Disponible en ligne")
            )
            action = "Lire les leçons disponibles" if code == "P03" else "Commencer le parcours"
            link = f'<a href="{first_lessons[code]}">{action} <span aria-hidden="true">↗</span></a>'
        cards.append(
            f'<article class="course-card" data-status="{status}">'
            f'<div class="card-top"><span class="course-code">{code}</span><span class="course-status">{label}</span></div>'
            f"<h3>{escape(title.strip())}</h3><p>{escape(cycle.strip())} · {escape(level.strip())}</p>"
            f"{link}</article>"
        )
    return "".join(cards)


def render_course(
    course: Path, code: str, course_title: str, module_plan: tuple[tuple[str, int], ...]
) -> tuple[str, str]:
    prefix = "" if code == "P01" else f"{code.lower()}/"
    route = f"/lecons/{prefix}"

    sources = sorted((course / "lecons").glob("*.md"))
    exam = course / "examen_final.md"
    if exam.is_file():
        sources.append(exam)
    lessons = [(source.stem, source.read_text(encoding="utf-8-sig")) for source in sources]
    titles = [
        next(line[2:].strip() for line in body.splitlines() if line.startswith("# "))
        for _, body in lessons
    ]
    if len(lessons) != module_plan[-1][1]:
        raise ValueError(f"Le nombre de pages ne correspond pas au plan de {code}.")
    pages = {source.resolve(): f"{route}{source.stem}.html" for source in sources}
    target = OUTPUT / f"lecons/{prefix}"
    target.mkdir(parents=True, exist_ok=True)
    template = Template((SITE / "page.html").read_text(encoding="utf-8"))

    def lesson_link(index: int, label: str | None = None, *, current: bool = False) -> str:
        slug = lessons[index][0]
        active = ' aria-current="page"' if current else ""
        return f'<a href="{route}{slug}.html"{active}>{escape(label or titles[index])}</a>'

    def modules(current: int | None = None) -> str:
        groups = []
        start = 0
        for name, end in module_plan:
            opened = " open" if current is not None and start <= current < end else ""
            items = "".join(
                f"<li>{lesson_link(i, current=i == current)}</li>" for i in range(start, end)
            )
            groups.append(f"<details{opened}><summary>{name}</summary><ul>{items}</ul></details>")
            start = end
        return "".join(groups)

    def write(
        path: Path,
        title: str,
        content: str,
        index: int | None = None,
        navigation: str = "",
        outline: str = "",
    ) -> None:
        path.write_text(
            template.substitute(
                title=escape(title),
                modules=modules(index),
                content=content,
                navigation=navigation,
                outline=outline,
                layout="landing" if index is None else "lesson",
            ),
            encoding="utf-8",
        )

    for index, (slug, body) in enumerate(lessons):
        renderer = LessonRenderer(course, prefix, pages)
        renderer.source = sources[index]
        markdown = mistune.create_markdown(renderer=renderer, plugins=["table"])
        article = markdown(body)
        outline = "".join(
            f'<li><a href="#{anchor}">{label}</a></li>' for anchor, label in renderer.sections
        )
        if outline:
            outline = (
                '<nav class="outline" aria-label="Dans cette leçon">'
                f"<details open><summary>Dans cette leçon</summary><ul>{outline}</ul></details></nav>"
            )
        previous = lesson_link(index - 1, "Leçon précédente") if index > 0 else ""
        following = lesson_link(index + 1, "Leçon suivante") if index + 1 < len(lessons) else ""
        write(
            target / f"{slug}.html",
            titles[index],
            f'<p class="breadcrumb"><a href="/#parcours">{escape(course_title)}</a>'
            f' <span aria-hidden="true">/</span> {escape(next(name for name, end in module_plan if index < end))}</p>'
            f"<article>{article}</article>",
            index,
            f'<nav class="pagination" aria-label="Navigation entre les leçons">{previous}{following}</nav>',
            outline,
        )

    return pages[sources[0].resolve()], modules()


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for asset in ("style.css", "atelier.js", "catalogue.js", "python-worker.js"):
        copyfile(SITE / asset, OUTPUT / asset)
    p01, modules = render_course(COURSE, "P01", "Python Fondamentaux", MODULES)
    p02, _ = render_course(
        ROOT / "parcours/p02_poo_et_conception",
        "P02",
        "POO et conception",
        (("Objets et conception", 5), ("Projet et examen", 7)),
    )
    p03_course = ROOT / "parcours/p03_python_avance"
    p03, _ = render_course(
        p03_course,
        "P03",
        "Python avancé",
        (("Leçons disponibles", len(list((p03_course / "lecons").glob("*.md")))),),
    )
    home = Template((SITE / "home.html").read_text(encoding="utf-8"))
    template = Template((SITE / "page.html").read_text(encoding="utf-8"))
    content = home.substitute(
        first_lesson=p01,
        cards=course_cards({"P01": p01, "P02": p02, "P03": p03}),
        modules=modules,
    )
    (OUTPUT / "index.html").write_text(
        template.substitute(
            title="Apprendre Python",
            modules="",
            content=content,
            navigation="",
            outline="",
            layout="landing",
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
