from datetime import datetime, date

def leer_entero(mensaje, minimo=None, maximo=None):
    """
    Pide al usuario un número entero y valida que sea correcto.
    Permite definir un rango opcional (minimo, maximo).
    """
    while True:
        try:
            valor = int(input(mensaje))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"⚠️  El valor debe estar entre {minimo} y {maximo}. Intenta de nuevo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Debes escribir un número entero.")


def leer_float(mensaje, minimo=None, maximo=None):
    """
    Pide un número decimal (float) y valida que sea correcto.
    """
    while True:
        try:
            valor = float(input(mensaje))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"El valor debe estar entre {minimo} y {maximo}. Intenta de nuevo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Debes escribir un número decimal.")


def leer_fecha(mensaje):
    """
    Pide una fecha en formato YYYY-MM-DD y la convierte a objeto date.
    """
    while True:
        fecha_str = input(mensaje)
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            return fecha
        except ValueError:
            print("Formato inválido. Usa el formato YYYY-MM-DD (por ejemplo, 2025-10-27).")


def leer_opcion(mensaje, opciones):
    """
    Pide una opción del menú y valida que esté dentro del rango.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor not in opciones:
                print(f"Opción inválida. Escoge una de: {opciones}")
                continue
            return valor
        except ValueError:
            print("Debes ingresar un número válido.")
