# Transformer la boutique de P01

## Consigne

1. Remplacer les dictionnaires produits par `Produit`, avec prix positif et quantité entière.
2. Faire posséder les produits par `Stock`. Prévoir ajout, recherche, valeur et alertes.
3. Enregistrer chaque vente dans une dataclass immuable contenant des valeurs copiées.
4. Extraire la règle de remise dans un objet remplaçable.
5. Donner cet objet à `Caisse` à sa construction : c'est l'injection de dépendance.

Comparer les résultats à P01 sur des entrées valides. Préserver la limite exacte de
10 000 FCFA : aucune remise à cette valeur, 5 % au-dessus. Une vente refusée ne doit
modifier ni quantité ni journal. Deux stocks doivent rester indépendants.

Le [corrigé](modele.py) et les [tests](test_modele.py) montrent le noyau métier.
La console (`main.py`), le stockage JSON et l'export CSV (`stockage.py`) sont fournis,
ainsi que les statistiques par produit et par client. Le chargeur accepte une sauvegarde
P01 valide et écrit ensuite le format P02 versionné. Ne jamais travailler sur l'unique
copie d'un fichier métier : copier les données avant de tester une migration.
Les quantités fractionnaires sont désormais rejetées ; P01 les convertissait en entiers.
Les recherches inconnues lèvent ici `KeyError`, les ruptures `ValueError` : adapter les
gestionnaires d'erreurs de la console si on la porte.

## Relecture humaine (100 points)

| Critère | Points |
|---|---|
| Comportements métier et cas limites | 40 |
| Répartition des responsabilités, composition pertinente | 25 |
| Tests utiles, dont ventes refusées et indépendance des stocks | 20 |
| Documentation des contrats et justification des choix | 15 |

Expliquer par écrit pourquoi `Stock` contient des produits et pourquoi il n'hérite
pas de `Produit`. Montrer aussi une règle qui resterait plus simple sous forme de
fonction. Le résultat des tests ne suffit pas à attribuer les points de conception.

## Lancer l'application

Depuis la racine du dépôt, avec l'environnement activé :

```powershell
python -m parcours.p02_poo_et_conception.projets.boutique_objets.main
# Pour tester sur une copie de données P01 :
python -m parcours.p02_poo_et_conception.projets.boutique_objets.main --fichier chemin/vers/copie/boutique.json
```

Le menu propose ajout, vente, consultation, alertes, statistiques et export CSV.
Choisir `q` sauvegarde. Une interruption ne sauvegarde pas les changements en cours.
Un fichier corrompu arrête le chargement sans l'écraser ; corriger le fichier ou utiliser
une copie saine. Les erreurs d'accès sont signalées. Cette version est locale et
mono-utilisateur, avec les nombres flottants de P01 et les mêmes seuils de remise.

## Trois livrables à produire avant de lire le corrigé

1. **Métier :** écrire Produit, Stock, Vente, les politiques et Caisse ; utiliser
   `test_modele.py` pour vérifier les comportements et la comparaison à P01.
2. **Stockage :** coder sauvegarder, charger et exporter_journal_csv en respectant
   les contrats de `stockage.py` ; appliquer les tests disque de `test_integration.py`.
3. **Console :** coder le menu documenté ci-dessus ; vérifier ajout, vente, refus,
   export et rechargement avec les tests console du même fichier.

Travailler dans une copie du dossier en conservant ses noms de modules. Les fichiers
fournis sont un corrigé complet, pas des squelettes à trous. La migration depuis P01,
les données corrompues, les valeurs non finies et les échecs de sauvegarde sont testés.
