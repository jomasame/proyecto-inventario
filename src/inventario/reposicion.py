"""HU-03: productos por pedir. Contrato en el README."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Producto:
    nombre: str
    stock: int
    stock_minimo: int


def _es_cantidad_valida(valor: object) -> bool:
    """Entero >= 0. Se excluye bool porque en Python True es un int."""
    return isinstance(valor, int) and not isinstance(valor, bool) and valor >= 0


def _validar(producto: Producto) -> None:
    if not isinstance(producto.nombre, str) or not producto.nombre.strip():
        raise ValueError("Producto con nombre vacío")
    for campo in ("stock", "stock_minimo"):
        valor = getattr(producto, campo)
        if not _es_cantidad_valida(valor):
            raise ValueError(f"Producto '{producto.nombre}': {campo} inválido ({valor})")


def _faltante(producto: Producto) -> int:
    return producto.stock_minimo - producto.stock


def _orden_de_urgencia(producto: Producto) -> tuple[int, str]:
    """Mayor faltante primero; en empate, alfabético por nombre."""
    return (-_faltante(producto), producto.nombre)


def productos_por_pedir(productos: list[Producto]) -> list[Producto]:
    for producto in productos:
        _validar(producto)

    por_pedir = [p for p in productos if _faltante(p) >= 0]
    return sorted(por_pedir, key=_orden_de_urgencia)
