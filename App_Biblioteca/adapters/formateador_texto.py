from domain.modelos import ReciboMulta

class FormateadorTexto:
    """Convierte un recibo de multa en un formato de texto legible."""

    def a_texto(self, recibo: ReciboMulta) -> str:
        usuario = recibo.prestamo.usuario
        material = recibo.prestamo.material
        return (
            f"📚 Recibo de multa\n"
            f"Usuario: {usuario.nombre} ({usuario.categoria})\n"
            f"Material: {material.titulo} ({material.tipo})\n"
            f"Fecha devolución: {recibo.fecha_devolucion}\n"
            f"Monto a pagar: ₡{recibo.monto:.2f}\n"
            f"{'-'*30}\n"
        )
