# Importamos herramientas para clases abstractas
from abc import ABC, abstractmethod
from excepciones import ErrorServicio

# Clase abstracta (no se puede usar directamente)
class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del servicio

    # Método que OBLIGA a las clases hijas a implementarlo
    @abstractmethod
    def calcular_costo(self):
        pass

    # Otro método obligatorio
    @abstractmethod
    def descripcion(self):
        pass
