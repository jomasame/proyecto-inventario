import pytest

from inventario.reposicion import Producto, productos_por_pedir


# --- Casos normales -------------------------------------------------------

def test_devuelve_solo_los_productos_bajo_el_minimo():
    arroz = Producto("Arroz", 2, 10)
    sal = Producto("Sal", 20, 5)

    assert productos_por_pedir([arroz, sal]) == [arroz]


def test_ordena_por_mayor_faltante_primero():
    pan = Producto("Pan", 0, 3)        # faltante 3
    aceite = Producto("Aceite", 4, 10)  # faltante 6

    assert productos_por_pedir([pan, aceite]) == [aceite, pan]


def test_en_empate_de_faltante_ordena_por_nombre():
    zanahoria = Producto("Zanahoria", 1, 5)
    ajo = Producto("Ajo", 1, 5)

    assert productos_por_pedir([zanahoria, ajo]) == [ajo, zanahoria]


# --- Casos límite ---------------------------------------------------------

def test_lista_vacia_devuelve_lista_vacia():
    assert productos_por_pedir([]) == []


def test_stock_igual_al_minimo_si_se_pide():
    leche = Producto("Leche", 5, 5)

    assert productos_por_pedir([leche]) == [leche]


def test_stock_cero_con_minimo_cero_se_pide():
    agotado = Producto("Vela", 0, 0)

    assert productos_por_pedir([agotado]) == [agotado]


def test_si_ninguno_esta_bajo_el_minimo_devuelve_lista_vacia():
    assert productos_por_pedir([Producto("Sal", 20, 5)]) == []


def test_no_modifica_la_lista_de_entrada():
    entrada = [Producto("Sal", 20, 5), Producto("Arroz", 2, 10)]
    copia = list(entrada)

    productos_por_pedir(entrada)

    assert entrada == copia


# --- Casos de error -------------------------------------------------------

def test_stock_negativo_lanza_value_error_con_el_nombre():
    with pytest.raises(ValueError, match="Café"):
        productos_por_pedir([Producto("Café", -1, 5)])


def test_stock_que_no_es_entero_lanza_value_error():
    with pytest.raises(ValueError, match="Té"):
        productos_por_pedir([Producto("Té", 2.5, 5)])


def test_stock_booleano_lanza_value_error():
    with pytest.raises(ValueError, match="Azúcar"):
        productos_por_pedir([Producto("Azúcar", True, 5)])


def test_nombre_vacio_lanza_value_error():
    with pytest.raises(ValueError):
        productos_por_pedir([Producto("   ", 1, 5)])


def test_un_producto_invalido_rechaza_toda_la_operacion():
    with pytest.raises(ValueError):
        productos_por_pedir([Producto("Sal", 1, 5), Producto("Roto", -3, 5)])
