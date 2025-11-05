from typing import Protocol
from domain.modelos import ReciboMulta

class FormateadorRecibo(Protocol):
    """Define cómo se convierte un recibo a texto."""
    def a_texto(self, recibo: ReciboMulta) -> str:
        ...
