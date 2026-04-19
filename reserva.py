# Importamos errores y logger
from excepciones import ErrorReserva
from logger import registrar_log

class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente      # Objeto cliente
        self.servicio = servicio    # Objeto servicio
        self.estado = "Pendiente"   # Estado inicial

    def confirmar(self):
        try:
            # Intentamos calcular el costo
            costo = self.servicio.calcular_costo()

            # Si todo sale bien → confirmamos
            self.estado = "Confirmada"
            return costo

        except Exception as e:
            # Guardamos el error en logs
            registrar_log(f"Error al confirmar reserva: {e}")

            # Lanzamos un nuevo error encadenado
            raise ErrorReserva("No se pudo confirmar la reserva") from e

    def cancelar(self):
        # Cambiamos el estado
        self.estado = "Cancelada"
