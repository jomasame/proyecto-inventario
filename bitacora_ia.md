# Bitácora de uso de IA

Proyecto: Inventario de tienda
Estudiante: José Sanabria
Funcionalidad: HU-03 Ver los productos por pedir
Asistente usado: Claude (Claude Code), modo chat/agente

## Entradas

### Entrada 1

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** «Dada la HU-03 y este contrato, propón casos de prueba normales, límite y de error antes de escribir el código.» El asistente propuso 13 casos, entre ellos stock igual al mínimo, lista vacía, stock `True` (booleano) y que la función no modifique la lista de entrada.
- **Decisión:** Aceptada
- **Por qué:** Cubren los casos normales, los límites y el escenario de error del criterio de aceptación; el caso del booleano no se me había ocurrido y es un borde real de Python.
- **Verificación:** Leí cada prueba contra el contrato del README y confirmé que las 13 fallaban en rojo (`NotImplementedError`) antes de implementar.
- **Commit relacionado:** 12c0449 «Pruebas de productos por pedir (en rojo)»

### Entrada 2

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** «Implementa `productos_por_pedir` para que pasen estas pruebas y cumpla el contrato.» El primer borrador validaba con `isinstance(p.stock, int)`.
- **Decisión:** Aceptada con cambios
- **Por qué:** La lógica de filtrado y de orden estaba bien, pero `isinstance(True, int)` es `True`, así que un booleano pasaba como stock válido y el contrato dice que no.
- **Verificación:** `pytest` dio 12 pasadas y 1 fallo (`test_stock_booleano_lanza_value_error`). Agregué `not isinstance(valor, bool)` sin tocar la prueba y quedaron las 13 en verde.
- **Commit relacionado:** a2ee3b5 «Implementa productos por pedir (pruebas en verde)»

### Entrada 3

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** El asistente planteó, como alternativa, ignorar en silencio los productos con datos inválidos y devolver solo los válidos.
- **Decisión:** Rechazada
- **Por qué:** El criterio de aceptación pide rechazar la operación con un error que diga qué producto falló; una lista parcial podría ocultar un producto que sí hay que pedir.
- **Verificación:** Mantuve la validación que lanza `ValueError`; la prueba `test_un_producto_invalido_rechaza_toda_la_operacion` pasa.
- **Commit relacionado:** a2ee3b5 «Implementa productos por pedir (pruebas en verde)»

### Entrada 4

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** «Con las pruebas en verde, refactoriza: hay validación repetida para `stock` y `stock_minimo` y una fórmula de orden poco legible.» Propuso `_es_cantidad_valida`, `_validar`, `_faltante` y `_orden_de_urgencia`.
- **Decisión:** Aceptada
- **Por qué:** Elimina el bloque `if` duplicado y da nombre a la regla de orden, sin cambiar el comportamiento.
- **Verificación:** Ejecuté `pytest` tras el refactor (13 pasan) y `git diff --stat -- tests` no muestra cambios en las pruebas.
- **Commit relacionado:** 2c7b690 «Refactor: elimina validacion duplicada y nombra la regla de orden»

### Entrada 5

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** El asistente redactó la tabla de ejemplos del README. En el ejemplo de orden, la salida no coincidía con la regla de desempate que yo había definido.
- **Decisión:** Aceptada con cambios
- **Por qué:** Un ejemplo incorrecto en el contrato confunde a quien lo lea y contradice el código.
- **Verificación:** Ejecuté los ejemplos del README en Python y comparé con lo escrito; cambié el ejemplo (Pan 0/3 y Aceite 4/10 → Aceite primero) para que mostrara el orden por faltante.
- **Commit relacionado:** 12c0449 «Pruebas de productos por pedir (en rojo)»

## Resumen

| Decisión | Cantidad |
|---|---|
| Aceptadas | 2 |
| Aceptadas con cambios | 2 |
| Rechazadas | 1 |

## Errores que atraparon las pruebas

El primer borrador del asistente validaba el stock con `isinstance(p.stock, int)`. La prueba `test_stock_booleano_lanza_value_error` falló porque `True` es un `int` en Python y no se lanzaba `ValueError`. Corregí el código excluyendo `bool` en la validación; la prueba no se modificó.

## Reflexión final (5 a 8 líneas)

El asistente me ayudó más proponiendo casos límite que yo no había pensado, como el booleano y que la función no modifique la lista de entrada. Escribir el contrato y las pruebas primero me permitió juzgar su código con un criterio propio en vez de confiar en él. Las pruebas atraparon que `True` pasaba como stock válido, algo que a simple vista el código parecía manejar bien. También aprendí a revisar los ejemplos del README, porque el asistente cometió un error ahí que solo vi al ejecutarlos. Rechacé ignorar en silencio los datos inválidos porque el criterio pide un error claro. En la próxima funcionalidad escribiría también una prueba del formato exacto del mensaje de error y pediría el refactor en un commit aparte desde el principio.
