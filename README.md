# Proyecto final: Inventario de tienda

Sistema pequeño de control de inventario para una tienda de barrio.

## Funcionalidad de la semana 5

### Historia de usuario

**HU-03 (Must). Ver los productos por pedir**

> Como encargado de la tienda, quiero ver qué productos están en o por debajo de su
> stock mínimo, para saber qué debo pedir al proveedor antes de quedarme sin existencias.

**Criterio de aceptación**

- *Dado* un inventario con productos, *cuando* pido la lista de productos por pedir,
  *entonces* veo solo los productos cuyo `stock` es **menor o igual** a su `stock_minimo`.
- Los productos aparecen del más urgente (mayor faltante) al menos urgente.
- *Escenario de error:* si algún producto tiene datos inválidos (stock negativo,
  stock que no es entero, nombre vacío), el sistema rechaza la operación con un
  `ValueError` y un mensaje que dice cuál producto falló, en vez de devolver una lista parcial.

### Contrato de la función

```python
# src/inventario/reposicion.py
@dataclass(frozen=True)
class Producto:
    nombre: str
    stock: int          # existencias actuales, >= 0
    stock_minimo: int   # umbral de reposición, >= 0

def productos_por_pedir(productos: list[Producto]) -> list[Producto]: ...
```

| Aspecto | Definición |
|---|---|
| **Recibe** | Una lista (puede estar vacía) de `Producto`. |
| **Devuelve** | Una lista **nueva** con los productos donde `stock <= stock_minimo`. No modifica la lista de entrada. |
| **Orden** | Por faltante (`stock_minimo - stock`) de mayor a menor; en empate, por `nombre` alfabéticamente. |
| **Supuestos** | Los nombres no se repiten; las cantidades están en la misma unidad de venta. |
| **Errores** | `ValueError` si `nombre` está vacío o es solo espacios, si `stock` o `stock_minimo` no son enteros (un `bool` tampoco vale) o si son negativos. |

**Casos límite**

- Lista vacía → `[]`.
- `stock == stock_minimo` → **sí** se pide (el umbral es inclusivo).
- `stock == 0` → se pide siempre, y va primero si tiene el mayor faltante.
- `stock_minimo == 0` y `stock == 0` → se pide (0 <= 0).
- Ningún producto bajo el mínimo → `[]`.

**Ejemplos**

| Entrada | Salida |
|---|---|
| `[]` | `[]` |
| `[Producto("Arroz", 2, 10), Producto("Sal", 20, 5)]` | `[Producto("Arroz", 2, 10)]` |
| `[Producto("Leche", 5, 5)]` (stock igual al mínimo) | `[Producto("Leche", 5, 5)]` |
| `[Producto("Pan", 0, 3), Producto("Aceite", 4, 10)]` | `[Producto("Aceite", 4, 10), Producto("Pan", 0, 3)]` (faltantes 6 y 3: el mayor faltante va primero) |
| `[Producto("Café", -1, 5)]` | `ValueError: Producto 'Café': stock inválido (-1)` |

### Cómo ejecutar las pruebas

```bash
pip install pytest
pytest
```

Un solo comando (`pytest`) ejecuta todas las pruebas; `pytest.ini` ya configura la ruta del código.

## Estructura

```
src/inventario/reposicion.py   # funcionalidad
tests/test_reposicion.py       # pruebas
bitacora_ia.md                 # bitácora de uso de IA
```
