"""HU-03: productos por pedir. Contrato en el README."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Producto:
    nombre: str
    stock: int
    stock_minimo: int


def productos_por_pedir(productos: list[Producto]) -> list[Producto]:
    for p in productos:
        if not isinstance(p.nombre, str) or not p.nombre.strip():
            raise ValueError("Producto con nombre vacío")
        if not isinstance(p.stock, int) or isinstance(p.stock, bool) or p.stock < 0:
            raise ValueError(f"Producto '{p.nombre}': stock inválido ({p.stock})")
        if (
            not isinstance(p.stock_minimo, int)
            or isinstance(p.stock_minimo, bool)
            or p.stock_minimo < 0
        ):
            raise ValueError(
                f"Producto '{p.nombre}': stock_minimo inválido ({p.stock_minimo})"
            )

    por_pedir = [p for p in productos if p.stock <= p.stock_minimo]
    return sorted(por_pedir, key=lambda p: (-(p.stock_minimo - p.stock), p.nombre))
