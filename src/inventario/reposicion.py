"""HU-03: productos por pedir. Contrato en el README (esqueleto: sin implementar)."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Producto:
    nombre: str
    stock: int
    stock_minimo: int


def productos_por_pedir(productos: list[Producto]) -> list[Producto]:
    raise NotImplementedError("HU-03 pendiente de implementar")
