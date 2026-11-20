"""Exercices 3.2 — Complète les TODO sans modifier les signatures."""

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator


class Article:
    def __init__(self, nom: str, prix: int) -> None:
        self.nom = nom
        self.prix = prix

    @property
    def prix(self) -> int:
        # TODO : retourne le prix interne.
        raise NotImplementedError

    @prix.setter
    def prix(self, valeur: int) -> None:
        # TODO : refuse les prix négatifs, puis mémorise la valeur.
        raise NotImplementedError


class Paiement(ABC):
    @abstractmethod
    def payer(self, montant: int) -> str:
        """Retourne une confirmation de paiement."""
        raise NotImplementedError


class PaiementSimulation(Paiement):
    def payer(self, montant: int) -> str:
        # TODO : refuse un montant négatif avec ValueError.
        # Sinon, retourne « Simulation : <montant> FCFA ».
        raise NotImplementedError


class Catalogue:
    def __init__(self, articles: Iterable[Article]) -> None:
        # TODO : copie les articles dans une liste interne.
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, indice: int) -> Article:
        raise NotImplementedError

    def __iter__(self) -> Iterator[Article]:
        raise NotImplementedError
