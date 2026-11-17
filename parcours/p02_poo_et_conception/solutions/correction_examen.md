# Correction de l’examen P02

## QCM

1. **a** — un modèle pour construire des objets.
2. **b** — l’instance courante.
3. **c** — dans __init__.
4. **a** — par les deux.
5. **b** — None.
6. **c** — un usage interne par convention.
7. **a** — la lecture.
8. **b** — de la composition.
9. **c** — une règle que l’objet doit préserver.
10. **a** — avant de modifier la quantité.
11. **b** — __init__ et __eq__.
12. **c** — non.
13. **a** — la réaffectation ordinaire des champs.
14. **b** — des copies des valeurs utiles.
15. **c** — respecter le contrat public du parent.
16. **a** — le même appel sur plusieurs objets compatibles.
17. **b** — la fournir depuis l’extérieur.
18. **c** — une fonction.
19. **a** — la convertir avec asdict.
20. **b** — être signalée sans être écrasée.

## Partie C : repères pour la correction humaine

1. Le produit gère ses règles propres ; le stock rassemble et recherche des produits.
   Un stock n'est pas une variété de produit et n'a ni un prix unitaire ni une quantité
   propres au même sens. La composition exprime cette relation et évite un faux contrat
   d'héritage. Une fonction de normalisation d'un nom ou de calcul sans état est un
   exemple approprié. Accepter toute justification cohérente, même formulée autrement.
2. `vendre` reçoit client, nom de produit, quantité entière positive et date facultative.
   Elle retourne une Vente immuable, diminue la quantité et ajoute une vente au journal.
   KeyError : produit absent. ValueError : quantité, stock, remise ou données invalides.
   Une stratégie peut aussi lever sa propre exception. Tester par exemple une rupture et
   une stratégie qui échoue : vérifier dans les deux cas quantité inchangée et journal
   inchangé. Accepter d'autres tests démontrant ces garanties.

Attribuer les points selon le barème de l'énoncé ; ne pas exiger ces phrases exactes.
Une bonne note de code ne suffit pas pour attribuer les points de documentation.
