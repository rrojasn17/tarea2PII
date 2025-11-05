from abc import ABC, abstractmethod

class PoliticaMulta(ABC):
    """Clase abstracta que define la estructura común para cualquier política de multa."""

    @property
    @abstractmethod
    def nombre(self) -> str:
        """Nombre legible de la política."""
        pass

    @abstractmethod
    def calcular(self, dias_atraso: int, tipo_material: str) -> float:
        """Devuelve el monto de la multa según los días de atraso y tipo de material."""
        pass

#--------------------------------------------------------------------------------------------

class FijaPorDia(PoliticaMulta):
    def __init__(self, tarifa_fija: float):
        self._tarifa_fija = tarifa_fija

    @property
    def nombre(self):
        return "Fija por día"

    def calcular(self, dias_atraso: int, tipo_material: str) -> float:
        if dias_atraso <= 0:
            return 0.0
        return dias_atraso * self._tarifa_fija

#--------------------------------------------------------------------------------------------

class Escalonada(PoliticaMulta):
    def __init__(self, n: int, tarifa_a: float, tarifa_b: float):
        self._n = n
        self._tarifa_a = tarifa_a
        self._tarifa_b = tarifa_b

    @property
    def nombre(self):
        return "Escalonada"

    def calcular(self, dias_atraso: int, tipo_material: str) -> float:
        if dias_atraso <= 0:
            return 0.0
        if dias_atraso <= self._n:
            return dias_atraso * self._tarifa_a
        else:
            return self._n * self._tarifa_a + (dias_atraso - self._n) * self._tarifa_b

#--------------------------------------------------------------------------------------------

class ConDescuento(PoliticaMulta):
    def __init__(self, base: PoliticaMulta, porcentaje: float):
        self._base = base
        self._porcentaje = porcentaje

    @property
    def nombre(self):
        return f"{self._base.nombre} + Descuento {self._porcentaje}%"

    def calcular(self, dias_atraso: int, tipo_material: str) -> float:
        base_monto = self._base.calcular(dias_atraso, tipo_material)
        descuento = base_monto * (self._porcentaje / 100)
        return base_monto - descuento

#--------------------------------------------------------------------------------------------

class ConTope(PoliticaMulta):
    def __init__(self, base: PoliticaMulta, tope: float):
        self._base = base
        self._tope = tope

    @property
    def nombre(self):
        return f"{self._base.nombre} con Tope {self._tope}"

    def calcular(self, dias_atraso: int, tipo_material: str) -> float:
        monto = self._base.calcular(dias_atraso, tipo_material)
        return min(monto, self._tope)

#--------------------------------------------------------------------------------------------

fija = FijaPorDia(100)
escalonada = Escalonada(3, 50, 100)
descuento = ConDescuento(fija, 20)
tope = ConTope(escalonada, 500)

print(fija.calcular(5, "libro"))         # 500
print(escalonada.calcular(5, "libro"))  # 350
print(descuento.calcular(5, "libro"))   # 400
print(tope.calcular(10, "libro"))       # 500 (tope aplicado)