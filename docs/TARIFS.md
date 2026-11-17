# Tarifs et lancement — Mayele Python Académie

> **Stratégie : le volume avant la marge.** Des prix bas, **identiques pour tout le monde, dans le monde entier**,
> pour toucher le plus grand nombre d'apprenants. Les prix s'ajustent selon **l'effectif réel des utilisateurs**,
> pas selon un chiffre figé.
>
> ⚠️ Les montants ci-dessous sont des **valeurs de départ**. Tout se règle dans
> [`catalogue/tarifs.toml`](../catalogue/tarifs.toml) ; ensuite `python outils/generer_catalogue.py` régénère
> [`catalogue/catalogue.json`](../catalogue/catalogue.json), que ta plateforme lit.

## 1. Le plan en deux temps

| Phase | Durée | Ce que les utilisateurs peuvent faire |
|---|---|---|
| **1. Lancement gratuit** | 1 à 2 mois (réglable : 1 mois et 15 jours, 2 mois pile…) | tout lire, tout parcourir, **télécharger les documents** |
| **2. Premium** | à partir de la fin de la phase gratuite | les cours deviennent **achetables**, de **1 000 à 5 000 FCFA** par cours |

Le passage au premium est calculé automatiquement à partir de la **date d'ouverture** (`date_ouverture` dans
`tarifs.toml`) et de la durée choisie (`gratuit_mois`, `gratuit_jours`).

**Exemple** : ouverture le 1ᵉʳ décembre 2026, deux mois gratuits → premium dès le **1ᵉʳ février 2027**, annonce
aux utilisateurs le **17 janvier 2027** (15 jours avant).

### Bonnes pratiques de communication

- **Dire dès le premier jour** que la gratuité est temporaire et indiquer la date de fin : pas de mauvaise surprise.
- **Rappeler** la date 15 jours avant, puis 3 jours avant (e-mail, notification, bandeau sur le site).
- Annoncer clairement **ce qui reste gratuit** après la phase de lancement (par exemple le module 1 de chaque parcours).
- **Remercier** les premiers utilisateurs : badge « pionnier », ou petite réduction sur le premier achat.
- Pendant la phase gratuite, inviter les gens à **donner leur avis** : cela t'aidera à fixer les bons prix.

## 2. Le même prix pour tous, en trois monnaies

Un seul prix par cours, **valable pour tous les utilisateurs du monde**, affiché dans trois monnaies équivalentes :

| FCFA | Euro | Dollar |
|---|---|---|
| 1 000 | 1,5 € | 1,5 $ |
| 2 000 | 3,0 € | 3,5 $ |
| 3 000 | 4,5 € | 5,0 $ |
| 4 000 | 6,0 € | 6,5 $ |
| 5 000 | 7,5 € | 8,5 $ |

- Le franc CFA est lié à l'euro par une **parité fixe** (1 € = 655,957 FCFA) : le prix en euro est stable.
- Le **dollar varie** : `usd_pour_1_eur` dans `tarifs.toml` est une valeur **indicative à mettre à jour** régulièrement.
- Les montants en euro et en dollar sont arrondis à 0,50 pour obtenir des prix « propres ».

> ❓ J'ai compris « le même prix » comme **le même prix équivalent** dans les trois monnaies. Si tu voulais dire
> autre chose (par exemple des chiffres identiques, ou des prix ronds fixés à la main dans chaque monnaie), dis-le :
> c'est un simple changement de paramètre.

## 3. Les prix de départ proposés

| Parcours | Prix de base |
|---|---|
| P01 Python Fondamentaux | 2 000 FCFA (3 € · 3,5 $) |
| P02 POO et conception | 3 000 FCFA (4,5 € · 5 $) |
| P03 Python Avancé | 4 000 FCFA (6 € · 6,5 $) |
| Pack Licence 1 (P01 + P02) | 4 000 FCFA |
| Pack Licence complète (P01 + P02 + P03) | jusqu'à 7 000 FCFA (le plafond de 5 000 s'applique **par cours**) |

Les parcours plus avancés (data, IA, backend, cybersécurité) pourront se situer plus haut dans la fourchette,
jusqu'à 5 000 FCFA, mais jamais au-delà.

**Règle de sécurité du générateur** : tout prix hors de la fourchette [1 000 ; 5 000] est **refusé** (erreur),
et tout prix calculé est ramené dans la fourchette.

## 4. Tarifs réduits : facultatifs

Ta stratégie est un **prix unique pour tous**. Le fichier de tarifs contient pourtant des coefficients
(élève, étudiant, enseignant, formateur, demandeur d'emploi) et des licences collectives (équipes, écoles),
désactivés par défaut (`differencier_par_public = false`). Tu peux les activer plus tard si l'effectif des
utilisateurs le justifie, sans rien réécrire. Les prix restent toujours dans la fourchette 1 000 – 5 000 FCFA.

## 5. Piloter le prix grâce à l'effectif

Puisque ta stratégie repose sur **le nombre d'utilisateurs**, suis ces indicateurs dès la phase gratuite :

| Indicateur | Comment le lire |
|---|---|
| **Inscrits** | combien de personnes découvrent la plateforme |
| **Actifs** (ont terminé au moins une leçon) | l'intérêt réel du contenu |
| **Taux de complétion** du module 1 | la qualité de l'accueil |
| **Taux de conversion** (inscrits → acheteurs) | la bonne adéquation prix / valeur |
| **Revenu par utilisateur** | à comparer aux frais de paiement |

Le revenu estimé se calcule simplement :

```
revenu  =  nombre d'utilisateurs  ×  taux de conversion  ×  prix moyen payé
```

**Exemple (illustratif, à remplacer par tes vrais chiffres)** : 10 000 inscrits × 8 % d'acheteurs × 2 000 FCFA
= 1 600 000 FCFA. Si le taux de conversion monte quand le prix baisse, un prix plus bas peut rapporter davantage.
C'est exactement ce que tu observeras avec tes vrais utilisateurs : teste, mesure, ajuste.

## 6. Points d'attention

- **Frais de paiement** : sur de petits montants, les frais fixes par transaction (mobile money, cartes) peuvent
  représenter une part importante du prix. Renseigne-toi sur les frais exacts de chaque moyen de paiement et
  envisage un **pack** ou un **solde prépayé** pour limiter leur poids.
- **Pouvoir d'achat différent selon les pays** : un prix unique mondial est simple et lisible ; si l'effectif
  montre des blocages dans certains pays, tu pourras ajuster plus tard.
- **Remboursement et CGU** : définis une politique claire et affiche-la avant l'ouverture des ventes.
- **Contenus déjà téléchargés** pendant la gratuité : précise dans les CGU l'usage autorisé (usage personnel, pas de
  revente ni de republication).
- **Cadre légal** (immatriculation de l'activité, fiscalité, protection des données personnelles) : à vérifier
  localement avant de vendre.
- **Avis et témoignages** : n'affiche que de vrais avis d'apprenants.
- **Certificats** : ils attestent d'une formation de l'académie ; ne les présente pas comme des diplômes d'État.

## 7. Ce qui reste à décider (par toi)

1. La **date d'ouverture** de la plateforme et la **durée exacte** de la gratuité (2 mois ? 1,5 mois ?).
2. Les **prix de base** définitifs de chaque parcours.
3. Ce qui reste **gratuit** après le lancement (aperçu).
4. Le **taux du dollar** à utiliser pour l'affichage.
5. La **politique de remboursement** et les **CGU**.
6. Les **moyens de paiement** acceptés et leurs frais.
