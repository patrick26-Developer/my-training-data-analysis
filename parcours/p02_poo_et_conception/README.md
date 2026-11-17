# P02 — POO et conception

Prérequis : P01, notamment fonctions, exceptions, modules et tests.
Objectif : savoir choisir et concevoir des objets pour faire évoluer une boutique.
Les annotations de types avancées restent en P03.

## Progression

| Étape | Leçon | Application |
|---|---|---|
| 1 | [Classes et instances](lecons/l01_classes.md) | `Produit`, attributs, méthodes, `self` |
| 2 | [Composition et encapsulation](lecons/l02_composition.md) | `Stock`, invariants, propriétés |
| 3 | [Dataclasses](lecons/l03_dataclasses.md) | `Vente`, égalité, représentation, instantané |
| 4 | [Héritage et polymorphisme](lecons/l04_heritage.md) | politiques de remise interchangeables |
| 5 | [Patterns simples](lecons/l05_patterns.md) | stratégie, injection d'une dépendance |
| 6 | [Intégrer la boutique](lecons/l06_integrer_la_boutique.md) | console, JSON/CSV, migration et tests |

Les cinq premières leçons proposent chacune trois exercices avec squelettes,
corrigés commentés et tests communs. Le sixième module utilise le projet de synthèse
comme trois exercices d'intégration. L'[examen final](examen_final.md) comporte
20 QCM, quatre problèmes de code et deux questions de conception/documentation.

**Contenu prévu livré et validation technique effectuée.** La relecture humaine et
les essais avec de vrais débutants restent à faire ; cette mention ne vaut pas
validation pédagogique ni émission de certificat.

## Travail pratique

Étudier le [projet boutique](projets/boutique_objets/README.md), puis refaire la
transformation de P01 sans consulter le corrigé. Conserver les résultats métier :
normalisation des noms, cumul de stock, alertes, remise de 5 % au-dessus de 10 000 FCFA.
Les tests de comparaison avec P01 servent de filet de sécurité.

Depuis la racine du dépôt :

```powershell
python -m pytest parcours/p02_poo_et_conception/solutions parcours/p02_poo_et_conception/projets
python -m pytest parcours/p02_poo_et_conception/exercices/test_ex01_classes.py -v
```

Les exercices sont volontairement incomplets. Les tests valident le comportement ;
une relecture humaine doit aussi juger les responsabilités, les noms, la documentation
et la pertinence des classes. Aucune validation par de vrais débutants n'a encore eu lieu.

## Validation du parcours

- Pour chaque module : quiz et exercices ≥ 70 %. Les quiz sont corrigés avec les
  réponses fournies ; les tests vérifient les exercices. Une appréciation humaine
  reste nécessaire pour le travail de conception du module 6.
- Examen ≥ 70/100 : QCM 20 points, code 60 points, conception/documentation 20 points.
- Projet de synthèse ≥ 70/100 selon sa grille de relecture humaine.

Pour les exercices des cinq premières leçons, compter les tests réussis sur les tests
collectés ; 70 % est le seuil de travail, mais corriger tous les échecs est recommandé.
Pour le module 6, utiliser la grille du projet et son quiz (cinq réponses, 1 point chacune).
Les résultats auto-corrigés ne constituent pas une certification vérifiée.
