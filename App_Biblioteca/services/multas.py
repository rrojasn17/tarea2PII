from datetime import date
from domain.modelos import Prestamo, ReciboMulta

class ServicioMultas:
    def __init__(self, repositorio, formateador):
        """
        El servicio necesita dos dependencias:
        - repositorio: para guardar y listar recibos.
        - formateador: para convertir recibos a texto.
        """
        self.repositorio = repositorio
        self.formateador = formateador

    def registrar_prestamo(self, usuario, material, fecha_vencimiento: date) -> Prestamo:
        """
        Crea y devuelve un objeto Prestamo.
        """
        return Prestamo(usuario, material, fecha_vencimiento)

    def calcular_y_guardar(self, politica, prestamo: Prestamo, fecha_devolucion: date) -> ReciboMulta:
        """
        Calcula la multa usando la política dada, crea un recibo y lo guarda.
        """
        dias_atraso = (fecha_devolucion - prestamo.fecha_vencimiento).days
        dias_atraso = max(0, dias_atraso)  # evita negativos

        monto = politica.calcular(dias_atraso, prestamo.material.tipo)

        recibo = ReciboMulta(prestamo, monto, fecha_devolucion)
        self.repositorio.guardar(recibo)
        return recibo

    def texto_recibo(self, recibo: ReciboMulta) -> str:
        """
        Devuelve el texto del recibo usando el formateador configurado.
        """
        return self.formateador.a_texto(recibo)

    def listar_recibos(self):
        """
        Retorna la lista de recibos guardados.
        """
        return self.repositorio.listar()

