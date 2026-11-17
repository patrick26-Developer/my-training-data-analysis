# Tarifs et publics — Mayele Python Académie

> ⚠️ **Tous les montants de ce document sont des propositions de départ.** C'est toi qui décides des prix.
> Ils se règlent dans un seul fichier, [`catalogue/tarifs.toml`](../catalogue/tarifs.toml), puis
> `python outils/generer_catalogue.py` régénère [`catalogue/catalogue.json`](../catalogue/catalogue.json),
> que ta plateforme peut lire directement.

## 1. Comment les prix sont calculés

```
prix d'un parcours  =  prix de base  ×  coefficient du public        (arrondi à 500 FCFA)
prix par place (licence collective)  =  prix de base × coefficient × (1 − remise du palier)
prix d'un pack  =  somme des prix des parcours × (1 − remise du pack)
```

## 2. Les publics (accès individuel)

| Public | Coefficient | Justificatif à demander |
|---|---|---|
| Particulier | ×1,0 | aucun |
| Élève (collège, lycée) | ×0,4 | carte ou attestation de scolarité |
| Étudiant | ×0,6 | carte d'étudiant ou certificat d'inscription |
| Enseignant | ×0,6 | attestation de l'établissement |
| Formateur indépendant | ×0,8 | déclaration d'activité |
| Demandeur d'emploi / reconversion | ×0,5 | attestation ou déclaration sur l'honneur |

**Exemple avec un prix de base de 12 000 FCFA (P01)** : particulier 12 000 · élève 5 000 · étudiant 7 000 ·
enseignant 7 000 · formateur 9 500 · demandeur d'emploi 6 000.

## 3. Les licences collectives

| Licence | Pour qui | Minimum | Coefficient | Remises selon le nombre de places |
|---|---|---|---|---|
| Entreprise / équipe | sociétés, ONG, administrations | 3 | ×1,5 | 10 places : −10 % · 25 : −20 % · 50 : −30 % |
| École / université / centre | classes, promotions | 20 | ×0,35 | 50 places : −10 % · 100 : −20 % |

Une licence entreprise inclut en général : facture, tableau de suivi des collaborateurs et attestations. Ces
fonctions sont **à construire** dans ta plateforme : ne les promets que lorsqu'elles existent.

## 4. Les packs

| Pack | Parcours | Remise |
|---|---|---|
| Licence 1 : bases solides | P01 + P02 | −15 % |
| Licence complète | P01 + P02 + P03 | −20 % |

## 5. L'aperçu gratuit : donner envie avant d'acheter

Chaque parcours rend quelques leçons **lisibles gratuitement** (voir `apercu_gratuit` dans `tarifs.toml`).
Pour P01 : tout le module 1 (4 leçons). C'est ta meilleure publicité : on apprend vraiment quelque chose avant
de payer, et on a envie de continuer.

## 6. Bonnes pratiques commerciales

- **Vérifier les justificatifs** des tarifs réduits (et refaire la vérification chaque année).
- **Un tarif réduit est personnel** : un compte élève ne sert pas à plusieurs personnes.
- **Pas de revente du contenu** : écris-le dans les conditions d'utilisation (CGU) ; la licence formateur donne
  le droit de **se former**, pas de reproduire les cours. Si tu veux autoriser l'usage en classe, vends une
  licence établissement.
- **Moyens de paiement** : proposer mobile money (MTN MoMo, Airtel Money) et carte ; les frais des opérateurs sont
  à intégrer dans tes calculs.
- **Remboursement** : décide d'une politique claire (par exemple 7 jours si moins de 20 % du contenu consulté)
  et affiche-la ; ne promets une garantie que si tu peux la tenir.
- **Cadre légal** : renseigne-toi sur la TVA, l'immatriculation de ton activité et la protection des données
  personnelles au Congo avant l'ouverture des ventes.
- **Avis** : n'affiche que de vrais avis d'apprenants ; ne fabrique jamais de témoignages.
- **Certificats** : ils attestent d'une formation de l'académie. Ne les présente pas comme des diplômes d'État.

## 7. Idées de promotions

| Idée | Effet |
|---|---|
| Code de lancement (−20 % pendant 2 semaines) | premiers apprenants |
| Parrainage (−10 % pour le parrain et le filleul) | bouche-à-oreille |
| Prix de rentrée scolaire / universitaire | élèves et étudiants |
| Licence gratuite pour un club de code d'un lycée (limitée) | visibilité et réputation |
| Tarif solidaire (bourse) pour un nombre de places par trimestre | impact social, communication |

## 8. Ce qui reste à décider (par toi)

1. Les **prix de base** réels de chaque parcours.
2. **Accès à vie** ou **12 mois** ? (`duree_acces_mois`)
3. L'**aperçu gratuit** : quelles leçons ?
4. La **politique de remboursement** et les **CGU**.
5. Les **moyens de paiement** et leurs frais.
6. Les **justificatifs** exigés pour chaque tarif réduit.
