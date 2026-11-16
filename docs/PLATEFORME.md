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
| 1 | Parcours P01 complet |
| 2 | Site v1 : lecture + exécution Pyodide de P01 |
| 3 | P02 et P03, comptes, certificats, paiement |
| 4+ | Un parcours à la fois (P04 → P12) |
