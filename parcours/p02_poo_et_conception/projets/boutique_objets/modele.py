"""Objets métier de la boutique, sans interface ni accès aux fichiers."""

from dataclasses import dataclass
from datetime import date
from math import isclose, isfinite


def cle(nom):
    return " ".join(nom.split()).lower()


class Produit:
    """Un produit protège son prix et sa quantité contre les valeurs invalides."""

    def __init__(self, nom, prix, quantite):
        self._nom = " ".join(nom.split()).title()
        if not self._nom:
            raise ValueError("Le nom est obligatoire.")
        self.prix = prix
        if type(quantite) is not int or quantite < 0:
            raise ValueError("La quantité doit être un entier positif ou nul.")
        self._quantite = quantite

    @property
    def nom(self):
        return self._nom

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, valeur):
        if type(valeur) not in (int, float) or not isfinite(valeur) or valeur <= 0:
            raise ValueError("Le prix doit être strictement positif.")
        self._prix = float(valeur)

    @property
    def quantite(self):
        return self._quantite

    def ajouter(self, quantite):
        if type(quantite) is not int or quantite <= 0:
            raise ValueError("La quantité doit être un entier strictement positif.")
        self._quantite += quantite

    def retirer(self, quantite):
        if type(quantite) is not int or quantite <= 0:
            raise ValueError("La quantité doit être un entier strictement positif.")
        if quantite > self.quantite:
            raise ValueError("Stock insuffisant.")
        self._quantite -= quantite

    def valeur(self):
        return self.prix * self.quantite


class Stock:
    """Compose des produits ; chaque instance possède son propre dictionnaire."""

    def __init__(self):
        self._produits = {}

    def ajouter(self, produit):
        identifiant = cle(produit.nom)
        if identifiant in self._produits:
            existant = self._produits[identifiant]
            if produit.quantite:
                existant.ajouter(produit.quantite)
            existant.prix = produit.prix
        else:
            # Une copie évite que l'appelant modifie ensuite notre stock par son objet.
            self._produits[identifiant] = Produit(produit.nom, produit.prix, produit.quantite)

    def trouver(self, nom):
        # L'objet retourné reste modifiable via ses méthodes publiques : contrat explicite.
        return self._produits[cle(nom)]

    @property
    def produits(self):
        """Vue figée de la collection ; les produits gardent leurs méthodes publiques."""
        return tuple(self._produits.values())

    def valeur(self):
        return sum(produit.valeur() for produit in self._produits.values())

    def alertes(self, seuil=5):
        return sorted(p.nom for p in self._produits.values() if p.quantite <= seuil)


@dataclass(frozen=True)
class Vente:
    """Instantané de valeurs : changer le produit ne réécrit pas une vente passée."""

    date: str
    client: str
    produit: str
    quantite: int
    prix: float
    remise: float
    total: float

    def __post_init__(self):
        """Valider aussi les ventes reconstruites depuis un fichier externe."""
        date.fromisoformat(self.date)
        if not isinstance(self.client, str) or not self.client.strip():
            raise ValueError("Client obligatoire.")
        if not isinstance(self.produit, str) or not self.produit.strip():
            raise ValueError("Produit obligatoire.")
        if type(self.quantite) is not int or self.quantite <= 0:
            raise ValueError("Quantité entière positive requise.")
        for montant in (self.prix, self.remise, self.total):
            if type(montant) not in (int, float) or not isfinite(montant):
                raise ValueError("Montant fini requis.")
        sous_total = self.prix * self.quantite
        if self.prix <= 0 or not 0 <= self.remise <= sous_total:
            raise ValueError("Prix ou remise invalide.")
        if self.total < 0 or not isclose(self.total, sous_total - self.remise, abs_tol=1e-9):
            raise ValueError("Total incohérent.")


class SansRemise:
    """Contrat : calculer un montant entre zéro et le sous-total, sans effet de bord."""

    def calculer(self, sous_total):
        return 0.0


class RemiseSeuil(SansRemise):
    """Spécialise le calcul en conservant le même contrat public."""

    def calculer(self, sous_total):
        if sous_total > 10_000:
            return sous_total * 5 / 100
        return 0.0


class Caisse:
    """Reçoit une stratégie de remise ; ne dépend pas de sa classe concrète."""

    def __init__(self, stock, politique=None, journal=()):
        self.stock = stock
        self.politique = RemiseSeuil() if politique is None else politique
        self._journal = list(journal)
        if any(not isinstance(vente, Vente) for vente in self._journal):
            raise ValueError("Le journal doit contenir des Vente.")

    @property
    def journal(self):
        return tuple(self._journal)

    def vendre(self, client, nom, quantite, jour=None):
        produit = self.stock.trouver(nom)
        if type(quantite) is not int or quantite <= 0:
            raise ValueError("La quantité doit être un entier strictement positif.")
        if quantite > produit.quantite:
            raise ValueError("Stock insuffisant.")
        sous_total = produit.prix * quantite
        remise = self.politique.calculer(sous_total)
        if (
            type(remise) not in (int, float)
            or not isfinite(remise)
            or not 0 <= remise <= sous_total
        ):
            raise ValueError("Remise invalide.")
        vente = Vente(
            (jour or date.today()).isoformat(),
            " ".join(client.split()).title() or "Client",
            produit.nom,
            quantite,
            produit.prix,
            remise,
            sous_total - remise,
        )
        # Construire et vérifier avant de modifier le stock limite les échecs partiels.
        produit.retirer(quantite)
        self._journal.append(vente)
        return vente

    def chiffre_affaires(self):
        return sum(vente.total for vente in self._journal)

    def total_par_produit(self):
        totaux = {}
        for vente in self._journal:
            totaux[vente.produit] = totaux.get(vente.produit, 0) + vente.total
        return dict(sorted(totaux.items(), key=lambda ligne: ligne[1], reverse=True))

    def meilleur_client(self):
        depenses = {}
        for vente in self._journal:
            depenses[vente.client] = depenses.get(vente.client, 0) + vente.total
        return max(depenses, key=depenses.get) if depenses else None
