import os
from domain.modelos import ReciboMulta

class RepoArchivo:
    """Guarda los recibos de multa en un archivo de texto simple."""

    def __init__(self, nombre_archivo: str = "recibos.txt"):
        self.nombre_archivo = nombre_archivo

    def guardar(self, recibo: ReciboMulta) -> None:
        """Guarda el recibo como texto (una línea por recibo)."""
        with open(self.nombre_archivo, "a", encoding="utf-8") as f:
            texto = f"{recibo.prestamo.usuario.nombre},{recibo.monto},{recibo.fecha_devolucion}\n"
            f.write(texto)

    def listar(self) -> list[str]:
        """Lee todas las líneas del archivo (simple versión)."""
        if not os.path.exists(self.nombre_archivo):
            return []
        with open(self.nombre_archivo, "r", encoding="utf-8") as f:
            return f.readlines()
