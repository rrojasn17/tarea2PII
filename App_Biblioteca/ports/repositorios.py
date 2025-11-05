from typing import Protocol
from domain.modelos import ReciboMulta

class RepositorioRecibos(Protocol):
    """Define lo que debe poder hacer cualquier repositorio de recibos."""

    def guardar(self, recibo: ReciboMulta) -> None:
        ...

    def listar(self) -> list[ReciboMulta]:
        ...
