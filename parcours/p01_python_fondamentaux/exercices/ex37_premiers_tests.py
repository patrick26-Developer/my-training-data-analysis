"""Exercices 10.2 — Écris les tests !

Chaque fonction `tests_pour_xxx(fonction)` reçoit une implémentation de `xxx` à vérifier.
  - Si l'implémentation est CORRECTE : tes tests ne doivent rien lever.
  - Si elle est BOGUÉE : au moins un de tes `assert` doit échouer (AssertionError).
Couvre : cas normaux, cas limites, cas d'erreur. Lance les tests avec :
    pytest parcours/p01_python_fondamentaux/exercices/test_ex37_premiers_tests.py -v
"""


# Exercice 1 — est_pair(n) : True si n est pair.
def tests_pour_est_pair(est_pair):
    # Exemple fourni :
    assert est_pair(2) is True
    # TODO : ajoute d'autres cas (0, impair, négatif…)


# Exercice 2 — maximum(liste) : plus grand élément d'une liste non vide.
def tests_pour_maximum(maximum):
    raise NotImplementedError


# Exercice 3 — prix_ttc(prix_ht, taux=18) : prix TTC (utilise pytest.approx pour les flottants).
def tests_pour_prix_ttc(prix_ttc):
    raise NotImplementedError


# Exercice 4 — mention(note) : "Très bien" >= 16, "Bien" >= 14, "Assez bien" >= 12,
# "Passable" >= 10, sinon "Ajourné". Pense aux valeurs LIMITES (10, 12, 14, 16, 9.99).
def tests_pour_mention(mention):
    raise NotImplementedError


# Exercice 5 — retirer(solde, montant) : retourne solde - montant ;
# lève ValueError si montant <= 0 ou si montant > solde. Teste aussi les erreurs.
def tests_pour_retirer(retirer):
    raise NotImplementedError


# Exercice 6 — sans_doublons(liste) : liste sans doublons, ordre de première apparition conservé,
# l'original n'est PAS modifié.
def tests_pour_sans_doublons(sans_doublons):
    raise NotImplementedError


# Exercice 7 — est_bissextile(annee) : règle complète (divisible par 4, sauf siècles, sauf 400).
def tests_pour_est_bissextile(est_bissextile):
    raise NotImplementedError


# Exercice 8 — TDD : écris D'ABORD le test puis le code.
# Écris la fonction `fizzbuzz(n)` : retourne "FizzBuzz" si n est multiple de 3 ET 5, "Fizz" si
# multiple de 3, "Buzz" si multiple de 5, sinon le nombre sous forme de texte.
def fizzbuzz(n):
    raise NotImplementedError
