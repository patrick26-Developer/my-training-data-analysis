"""Corrigé 3.2 — Propriétés, contrat abstrait et composition."""

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator


class Article:
    def __init__(self, nom: str, prix: int) -> None:
        self.nom = nom
        self.prix = prix  # La création utilise aussi la validation.

    @property
    def prix(self) -> int:
        return self._prix

    @prix.setter
    def prix(self, valeur: int) -> None:
        if valeur < 0:
            raise ValueError("Le prix doit être positif ou nul")
        self._prix = valeur


class Paiement(ABC):
    @abstractmethod
    def payer(self, montant: int) -> str:
        """Retourne une confirmation de paiement."""
        raise NotImplementedError


class PaiementSimulation(Paiement):
    def payer(self, montant: int) -> str:
        if montant < 0:
            raise ValueError("Montant négatif")
        return f"Simulation : {montant} FCFA"


class Catalogue:
    def __init__(self, articles: Iterable[Article]) -> None:
        self._articles = list(articles)  # Copie du conteneur, pas des articles.

    def __len__(self) -> int:
        return len(self._articles)

    def __getitem__(self, indice: int) -> Article:
        return self._articles[indice]

    def __iter__(self) -> Iterator[Article]:
        return iter(self._articles)
