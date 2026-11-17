# Guide de style — écrire des leçons qui donnent envie d'apprendre

Une leçon réussie ne se contente pas d'expliquer : elle **donne envie de continuer**, **guide pas à pas**
et fait **ressentir le progrès**. Ce guide s'applique à tous les parcours.

## 1. Les 7 principes

1. **Parler à une personne.** « Tu » partout, phrases courtes, ton chaleureux. Jamais de « il convient de ».
2. **Commencer par l'envie, pas par la définition.** D'abord ce que la leçon permet de *faire* (un reçu, un
   graphique, un petit jeu), ensuite comment.
3. **Un seul pas à la fois.** Un concept, un exemple minimal, puis on complexifie. Si une phrase contient deux
   idées nouvelles, on la coupe.
4. **Le concret avant l'abstrait.** Marché de Poto-Poto, boutique de Mama Nzoni, transfert d'argent mobile,
   bus de Brazzaville : des situations que l'apprenant reconnaît.
5. **Montrer l'erreur avant de la corriger.** Se tromper est normal ; on le dit, on le montre, on le répare.
6. **Faire sentir la progression.** Étapes numérotées, petites victoires (« Bravo, tu viens de… »), aperçu de
   la suite (« Dans la prochaine leçon, tu pourras… »).
7. **Inviter à pratiquer.** Chaque leçon se termine par un défi réalisable en 10 à 20 minutes.

## 2. Structure d'une leçon

| Bloc | Rôle | Exemple |
|---|---|---|
| 🔥 **Accroche** | Donner envie, en une ou deux phrases | « À la fin, ton programme saura rendre la monnaie tout seul. » |
| 🎯 **Ce que tu sauras faire** | Objectifs concrets et vérifiables | « Calculer le total d'une facture » |
| 1. **Le problème** | Une situation réelle | « Mama Nzoni se trompe dans ses additions. » |
| 2. **L'idée en images** | Analogie ou schéma | « Une variable est une étiquette sur une boîte. » |
| 3. **Pas à pas** | Étapes courtes, code qui s'exécute | « Étape 1 : crée la variable. Étape 2 : … » |
| 4. ⚠️ **Pièges courants** | L'erreur réelle, son message, sa solution | « `NameError` : tu as oublié… » |
| 5. **À retenir** | 5 lignes maximum | |
| 6. **Exercices** | 3 à 8 petits défis avec tests automatiques | |
| 7. **Quiz** | 4-5 questions, réponses repliées | |
| 🎉 **Bravo** | Reconnaître l'effort, annoncer la suite | « Tu viens de franchir une étape clé. » |

## 3. Le vocabulaire qui donne envie (et celui à éviter)

| ✅ Préférer | ❌ Éviter |
|---|---|
| « Tu vas pouvoir… » | « L'apprenant doit être capable de… » |
| « Essayons ensemble » | « Considérons le cas où » |
| « Regarde ce qui se passe » | « Il est trivial de constater » |
| « C'est normal de se tromper ici » | « Évidemment » / « Il suffit de » |
| « Un peu comme… » (analogie) | Définition formelle en premier |

> Les mots « évidemment », « simplement », « il suffit de » découragent celles et ceux pour qui ce n'est
> justement pas évident. On les bannit.

## 4. Encourager sans mentir

- Féliciter des **actions** (« tu as écrit ta première fonction ») plutôt que des **talents** (« tu es doué »).
- Ne jamais promettre ce que le contenu ne peut pas garantir (emploi, salaire, diplôme d'État).
- Montrer l'effort attendu : durée estimée de chaque leçon, rythme conseillé.
- Aucun faux témoignage : les avis affichés sur les pages de vente doivent venir de vraies personnes.

## 5. Accessibilité et contexte local

- Textes courts, titres clairs, listes plutôt que longs paragraphes (lecture sur téléphone).
- Un terme technique = **une définition** à sa première apparition.
- Exemples en **FCFA**, noms et lieux locaux, mais sans folklore appuyé.
- Pas de dépendance à une connexion rapide : exemples exécutables hors ligne.
- Vérifier que chaque exemple de code fonctionne : `python outils/verifier_lecons.py`.

## 6. Check-list avant de publier une leçon

- [ ] L'accroche donne-t-elle envie en moins de 15 secondes ?
- [ ] Un débutant comprend-il chaque mot sans aide extérieure ?
- [ ] Chaque exemple est-il exécuté et vérifié (`verifier_lecons.py`) ?
- [ ] Y a-t-il au moins une erreur courante montrée et expliquée ?
- [ ] L'apprenant sait-il quoi faire ensuite (exercice, leçon suivante) ?
- [ ] Le ton est-il chaleureux, sans condescendance ni jargon inutile ?
