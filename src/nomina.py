"""
Cálculo de nómina semanal

Reglas de negocio:
- Solo se capturan horas trabajadas: de 0 a 64 por semana
- Hasta 40 h = pago normal $200 por hora
- 40 a 56 h = 40 h normales + excedente al doble ($400/h)
- 56 a 64 h = 40 h normales + 16 h dobles + excedente al triple ($600/h)
- Cualquier otro valor = "Número no válido"
"""
