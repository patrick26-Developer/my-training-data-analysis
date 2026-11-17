# Examen final — P02 POO et conception

⏱ Durée : 120 minutes · Total : 100 points · Réussite : au moins 70/100

Documentation Python autorisée. Ne pas consulter les corrigés ni le projet de référence.
Les entrées numériques des problèmes sont des entiers finis ; sauf indication contraire,
les prix, sous-totaux et distances sont positifs ou nuls. Le solde initial peut être
négatif dans les cas de refus. Les noms sont des textes valides. Aucun contrôle
supplémentaire de type n'est demandé pour cet examen.

## Partie A — QCM (20 points)

Une seule réponse par question, 1 point par bonne réponse, 0 sinon.

**1. Une classe est…**

a) un modèle pour construire des objets · b) une instance déjà construite · c) un fichier JSON

**2. self désigne…**

a) la classe parente · b) l’instance courante · c) toutes les instances

**3. Où initialiser une liste indépendante par objet ?**

a) dans une variable globale · b) dans le corps de la classe · c) dans __init__

**4. Deux variables désignent le même objet. Une mutation est visible…**

a) par les deux · b) par aucune · c) uniquement par la première

**5. Une méthode sans return explicite retourne…**

a) 0 · b) None · c) self

**6. Le préfixe _ indique…**

a) un chiffrement · b) une interdiction absolue d’accès · c) un usage interne par convention

**7. Une propriété sans setter permet…**

a) la lecture · b) toutes les mutations · c) uniquement la suppression

**8. Stock contient des Produit : c’est…**

a) de la récursivité · b) de la composition · c) de l’héritage obligatoire

**9. Un invariant est…**

a) une copie JSON · b) un type Python · c) une règle que l’objet doit préserver

**10. Pour refuser un retrait, on valide…**

a) avant de modifier la quantité · b) après la sauvegarde · c) après avoir vidé le stock

**11. dataclass génère notamment…**

a) un serveur · b) __init__ et __eq__ · c) un fichier CSV

**12. Les annotations des champs valident automatiquement les valeurs…**

a) toujours · b) seulement les prix · c) non

**13. frozen=True empêche…**

a) la réaffectation ordinaire des champs · b) toute mutation d’une liste interne · c) la lecture

**14. Une vente historique doit conserver…**

a) le produit mutable seul · b) des copies des valeurs utiles · c) le stock complet partagé

**15. Une classe enfant doit…**

a) toujours appeler super() · b) changer toutes les signatures · c) respecter le contrat public du parent

**16. Le polymorphisme permet…**

a) le même appel sur plusieurs objets compatibles · b) uniquement des nombres · c) d’éviter tous les tests

**17. Injecter une dépendance signifie…**

a) la rendre globale · b) la fournir depuis l’extérieur · c) la lire obligatoirement en JSON

**18. Une stratégie simple sans état peut être…**

a) seulement un parent abstrait · b) seulement une base de données · c) une fonction

**19. Pour encoder une dataclass en JSON, on peut…**

a) la convertir avec asdict · b) appeler input dessus · c) utiliser son adresse mémoire

**20. Une sauvegarde corrompue devrait ici…**

a) être remplacée silencieusement · b) être signalée sans être écrasée · c) être ignorée et payée

## Partie B — Code (60 points)

Compléter [ex07_examen_final.py](exercices/ex07_examen_final.py).
Lancer `python -m pytest parcours/p02_poo_et_conception/exercices/test_ex07_examen_final.py -v`.
Chacun des 20 tests nommés vaut 3 points. Un test réussi vaut 3, un échec ou une erreur 0.
Les erreurs de collecte ne donnent pas de points à la partie code avant correction.
Les tests sont publics : la compréhension et les choix sont aussi évalués en partie C.

### Problème 1 — Portefeuille (15 points)

`Portefeuille(solde)` refuse un solde négatif par ValueError. La propriété `solde`
est lisible sans setter. `debiter(montant)` diminue le solde et ne retourne rien.
Refuser par ValueError un montant inférieur ou égal à zéro ou supérieur au solde,
sans modifier celui-ci. Deux portefeuilles doivent être indépendants.

### Problème 2 — Ligne de ticket (15 points)

Créer une dataclass gelée `LigneTicket(produit: str, prix: int, quantite: int)`.
La méthode `total()` retourne prix * quantite. Conserver l'égalité et la représentation
générées. Pas de validation des champs demandée dans ce problème.

### Problème 3 — Livraison (15 points)

`Livraison.frais(distance)` retourne 0. `LivraisonMoto` en hérite et redéfinit
`frais(distance)` pour retourner 500 + 100 * distance, en FCFA. La méthode accepte
la même distance dans les deux classes.

### Problème 4 — Commande (15 points)

`Commande(livraison)` reçoit un objet fournissant `frais(distance)`.
`total(sous_total, distance)` appelle cette méthode une seule fois avec la distance
reçue et ajoute le résultat au sous-total. Des frais négatifs provoquent ValueError.
Ne pas exiger une classe concrète : une autre stratégie compatible doit fonctionner.

## Partie C — Conception et documentation (20 points, correction humaine)

1. **10 points.** Justifier en 150 à 250 mots pourquoi la boutique compose des
   produits dans un stock. Comparer avec un héritage Stock(Produit). Donner un cas
   où une fonction est plus simple qu'une classe. Répartition : responsabilités 4,
   comparaison argumentée 4, exemple de fonction 2.
2. **10 points.** Documenter le contrat de `Caisse.vendre` du projet : paramètres,
   résultat, erreurs, effets sur stock et journal. Expliquer deux tests d'échec à
   réaliser. Répartition : entrées/résultat 3, erreurs/effets 3, deux tests pertinents 4.

La note finale est A + B + C ; la partie C ne peut pas être attribuée par pytest.
Le projet de synthèse est évalué séparément sur 100 points.
Pour valider P02 : six modules suivis (quiz et exercices ≥ 70 % par module),
examen ≥ 70/100 et projet ≥ 70/100 après relecture humaine. Les règles de validation
sont documentées ; aucun certificat n'est automatiquement émis par ce dépôt.

## Corrigés

Après l'épreuve : [QCM et grille humaine](solutions/correction_examen.md),
[code commenté](solutions/sol07_examen_final.py).
