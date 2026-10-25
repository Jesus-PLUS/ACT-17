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
    """Error que indica que las horas ingresadas no son válidas."""

    def __init__(self):
        """Inicializa el error con el mensaje estándar de entrada inválida."""
        super().__init__(MENSAJE_INVALIDO)


def calcular_nomina(horas):
    """Calcula el pago semanal según las horas normales, dobles y triples."""
    if isinstance(horas, bool) or not isinstance(horas, (int, float)):
        raise HorasInvalidasError()

    if horas < 0 or horas > HORAS_MAXIMAS:
        raise HorasInvalidasError()

    normales = min(horas, LIMITE_NORMAL)
    dobles = max(min(horas, LIMITE_DOBLE) - LIMITE_NORMAL, 0)
    triples = max(horas - LIMITE_DOBLE, 0)
    return (normales * TARIFA_NORMAL
            + dobles * TARIFA_NORMAL * 2
            + triples * TARIFA_NORMAL * 3)

# coordina la entrada del usuario, el cálculo de nómina y la presentación del resultado
def main(entrada=input, salida=print):
    """Lee las horas, muestra el pago o informa si la entrada no es válida."""

    # solicita las horas, las convierte a número decimal y llama a calcular_nomina
    try:
        horas = float(entrada("Horas trabajadas (0-64): "))
        pago = calcular_nomina(horas)
    # si algún paso genera un ValueError, muestra el mensaje de entrada inválida y devuelve 1
    except ValueError:
        salida(MENSAJE_INVALIDO)
        return 1
    # si termina bien, muestra el pago
    salida(f"Pago semanal: ${pago:,.2f}") # separador de miles y dos decimales
    return 0