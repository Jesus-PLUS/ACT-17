"""
Un caso por cada regla, tomado en su valor límite (donde suelen estar los errores):
(hrs)
1. Pago normal  [0, 40]
2. Pago doble   (40, 56]
3. Pago triple  (56, 64]
4. Fuera de rango Ej: -1 y 65
5. Valor no numérico Ej: "abc"
Más dos pruebas del programa completo: captura válida (50 h) y mensaje "Número no válido"
"""
import pytest
from src.nomina import calcular_nomina, HorasInvalidasError, main

# parametrización
# Ejecuta la misma prueba una vez por cada par de horas y pago esperado.
@pytest.mark.parametrize("horas, esperado", [
    (0, 0), # para 0 horas
    (40, 8000), # para 40 hrs y pago normal
    (56, 14400), # para hrs dobles
    (64, 19200), # hrs triples
])
def test_pago_normal(horas, esperado):
    assert calcular_nomina(horas) == esperado

# Ejecuta la prueba con horas menores y mayores que el rango permitido.
@pytest.mark.parametrize("horas", [-1, 65, "abc"])
def test_fuera_de_rango(horas):
    """Verifica que las horas fuera de rango generen HorasInvalidasError."""
    with pytest.raises(HorasInvalidasError, match="Número no válido"):
        calcular_nomina(horas)


# comprueba cómo responde el programa si el usuario ingresa un valor no numérico
def test_programa_mensaje_invalido():
    mensajes = []
    assert main(entrada=lambda _: "abc", salida=mensajes.append) == 1
    assert mensajes == ["Número no válido"]

# verifica que procese correctamente una entrada válida y muestre el pago esperado
def test_programa_muestra_pago():
    mensajes = []
    # simula que el usuario ingresa "50" horas
    # comprueba que main devuelva 0 (que no hay errores)
    assert main(entrada=lambda _: "50", salida=mensajes.append) == 0
    assert mensajes[-1] == "Pago semanal: $12,000.00"