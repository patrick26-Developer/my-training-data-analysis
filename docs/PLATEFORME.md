# Plateforme web — architecture et feuille de route

## Contraintes du contexte

- Connexion chère ou instable → site **léger**, **mobile-first**, **mode hors-ligne** (PWA).
- Beaucoup d'apprenants sans PC puissant → **Python dans le navigateur** (Pyodide), rien à installer.
- Paiement local → **mobile money** (MTN MoMo, Airtel Money) via un agrégateur de paiement.
- Langue : français d'abord.

## Stack cible

| Couche | Choix |
|---|---|
| Backend | Django (auth, admin, ORM) |
| Interface | Templates + HTMX (léger, peu de JS) |
| Base de données | PostgreSQL (SQLite en dev) |
| Cache / files | Redis, Celery |
| Exécution du code | Pyodide côté navigateur ; runner isolé côté serveur pour la correction |
| Contenu | Markdown versionné dans Git, importé par le site |
| Déploiement | Docker + Docker Compose, hébergé sur Render |
| CI | GitHub Actions (ruff, mypy, pytest) |

## Fonctionnalités

1. Comptes, progression, tableau de bord
2. Lecture des leçons + éditeur de code exécutable
3. Correction automatique des exercices (tests pytest)
4. Quiz
5. Certificats PDF avec numéro et QR code, page de vérification publique
6. Paiement par mobile money, parcours 1 gratuit
7. Communauté (forum ou Discord)

## Feuille de route

| Phase | Livrable |
|---|---|
| 0 | Restructuration, dépendances, modèle de leçon ✅ |
| 1 | Parcours P01 complet ✅ (validation technique ; relecture pédagogique à faire) |
| 2 | P02 : POO et conception, puis P03 une fois P02 terminé |
| 3 | Site v1 : lecture + exécution Pyodide de P01, puis comptes, certificats et paiement |
| 4+ | Un parcours à la fois (P04 → P12) |

## État réel et validation

P02 dispose de six modules, exercices, corrigés, boutique console avec stockage et examen final.
La validation technique du contenu est effectuée ; P03 reste le prochain parcours à compléter.
Les contenus demandent encore une relecture humaine et des essais avec des débutants.
Les tests automatiques ne jugent pas seuls la conception ni la documentation.
Les comptes, paiements et certificats vérifiables décrits ici sont des fonctionnalités prévues.
