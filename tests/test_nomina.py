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
from src.nomina import calcular_nomina

# parametrización
# Ejecuta la misma prueba una vez por cada par de horas y pago esperado.
@pytest.mark.parametrize("horas, esperado", [
    (0, 0), # para 0 horas
    (40, 8000), # para 40 hrs y pago normal
])
def test_pago_normal(horas, esperado):
    assert calcular_nomina(horas) == esperado