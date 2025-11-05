from datetime import date, datetime
from domain.modelos import Usuario, Material
from domain.politicas import FijaPorDia, Escalonada, ConDescuento, ConTope
from services.multas import ServicioMultas
from adapters.repo_archivo import RepoArchivo
from adapters.formateador_texto import FormateadorTexto

repo = RepoArchivo()
formateador = FormateadorTexto()
servicio = ServicioMultas(repo, formateador)

def leer_fecha(texto):
    while True:
        try:
            fecha_str = input(texto + " (YYYY-MM-DD): ")
            return datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            print("Fecha inválida. Intenta de nuevo.")

def seleccionar_politica():
    print("\nSeleccione la política de multa:")
    print("1. Fija por día")
    print("2. Escalonada")
    print("3. Fija con tope máximo")
    opcion = input("Opción: ")

    if opcion == "1":
        tarifa = float(input("Tarifa fija por día: "))
        return FijaPorDia(tarifa)
    elif opcion == "2":
        n = int(input("Días al primer nivel: "))
        a = float(input("Tarifa A: "))
        b = float(input("Tarifa B: "))
        return Escalonada(n, a, b)
    elif opcion == "3":
        base = FijaPorDia(float(input("Tarifa base por día: ")))
        tope = float(input("Monto máximo (tope): "))
        return ConTope(base, tope)
    else:
        print("Opción inválida, se usará política fija ₡100 por día.")
        return FijaPorDia(100.0)

def registrar_prestamo():
    print("\n--- Registrar préstamo ---")
    nombre = input("Nombre del usuario: ")
    categoria = input("Categoría (estandar/estudiante/docente): ")
    titulo = input("Título del material: ")
    tipo = input("Tipo de material (libro/revista/audiovisual): ")
    fecha_venc = leer_fecha("Fecha de vencimiento")

    usuario = Usuario(nombre, categoria)
    material = Material(titulo, tipo)
    prestamo = servicio.registrar_prestamo(usuario, material, fecha_venc)

    print("Préstamo registrado exitosamente.")
    return prestamo

def devolver_material(prestamo):
    print("\n--- Devolver material ---")
    fecha_dev = leer_fecha("Fecha de devolución")

    politica = seleccionar_politica()

    # Descuento por categoría (decorador)
    if prestamo.usuario.categoria == "estudiante":
        politica = ConDescuento(politica, 20)
    elif prestamo.usuario.categoria == "docente":
        politica = ConDescuento(politica, 10)

    recibo = servicio.calcular_y_guardar(politica, prestamo, fecha_dev)
    texto = servicio.texto_recibo(recibo)
    print("\n" + texto)

def listar_recibos():
    print("\n--- Recibos guardados ---")
    recibos = servicio.listar_recibos()
    if not recibos:
        print("No hay recibos registrados todavía.")
    else:
        for linea in recibos:
            print(linea.strip())

def menu():
    prestamo_actual = None
    while True:
        print("\n=== Sistema de Multas de Biblioteca ===")
        print("1. Registrar préstamo")
        print("2. Devolver material y calcular multa")
        print("3. Listar recibos guardados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            prestamo_actual = registrar_prestamo()
        elif opcion == "2":
            if prestamo_actual is None:
                print("Primero debe registrar un préstamo.")
            else:
                devolver_material(prestamo_actual)
                prestamo_actual = None  # reiniciamos
        elif opcion == "3":
            listar_recibos()
        elif opcion == "4":
            print("👋 ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

