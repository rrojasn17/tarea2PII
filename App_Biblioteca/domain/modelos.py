from dataclasses import dataclass
from datetime import date

@dataclass # Crea metodo automaticamente el constructor (__init__) y el metodo (__repr__)
class Usuario:
    nombre: str
    categoria: str  # "estandar", "estudiante", "docente"

@dataclass
class Material:
    titulo: str
    tipo: str  # "libro", "revista", "audiovisual"

@dataclass
class Prestamo:
    usuario: Usuario # Viene de la clase Usuario
    material: Material # Viene de la clase Material
    fecha_vencimiento: date

@dataclass
class ReciboMulta:
    prestamo: Prestamo # Viene de la clase Prestado
    monto: float
    fecha_devolucion: date



