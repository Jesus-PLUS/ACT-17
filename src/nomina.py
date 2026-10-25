"""
Cálculo de nómina semanal

Reglas de negocio:
- Solo se capturan horas trabajadas: de 0 a 64 por semana
- Hasta 40 h = pago normal $200 por hora
- 40 a 56 h = 40 h normales + excedente al doble ($400/h)
- 56 a 64 h = 40 h normales + 16 h dobles + excedente al triple ($600/h)
- Cualquier otro valor = "Número no válido"
"""

TARIFA_NORMAL = 200
LIMITE_NORMAL = 40
LIMITE_DOBLE = 56

HORAS_MAXIMAS = 64
MENSAJE_INVALIDO = "Número no válido"


class HorasInvalidasError(ValueError):
    def __init__(self):
        super().__init__(MENSAJE_INVALIDO)


def calcular_nomina(horas):

    if horas < 0 or horas > HORAS_MAXIMAS:
        raise HorasInvalidasError()

    normales = min(horas, LIMITE_NORMAL)
    dobles = max(min(horas, LIMITE_DOBLE) - LIMITE_NORMAL, 0)
    triples = max(horas - LIMITE_DOBLE, 0)
    return (normales * TARIFA_NORMAL
            + dobles * TARIFA_NORMAL * 2
            + triples * TARIFA_NORMAL * 3)