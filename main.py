# Importamos todas las clases
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from logger import registrar_log

# Listas para guardar datos en memoria
clientes = []
reservas = []

def ejecutar():
    try:
        # -------------------------
        # 1. Crear cliente válido
        # -------------------------
        c1 = Cliente("Juan", "juan@email.com")
        clientes.append(c1)

        # -------------------------
        # 2. Cliente inválido
        # -------------------------
        try:
            c2 = Cliente("", "correo_malo")
        except Exception as e:
            registrar_log(e)  # Guardamos error

        # -------------------------
        # 3. Crear servicios
        # -------------------------
        s1 = ReservaSala(2)
        s2 = AlquilerEquipo(3)
        s3 = Asesoria(1)

        # -------------------------
        # 4. Reserva válida
        # -------------------------
        r1 = Reserva(c1, s1)
        print("Costo:", r1.confirmar())
        reservas.append(r1)

        # -------------------------
        # 5. Reserva inválida
        # -------------------------
        try:
            s_malo = ReservaSala(-1)  # Error
            r2 = Reserva(c1, s_malo)
            r2.confirmar()
        except Exception as e:
            registrar_log(e)

        # -------------------------
        # 6-10. Más reservas
        # -------------------------
        for i in range(5):
            try:
                r = Reserva(c1, s2)
                r.confirmar()
                reservas.append(r)
            except Exception as e:
                registrar_log(e)

    except Exception as e:
        # Error general del sistema
        registrar_log(f"Error general: {e}")

    finally:
        # Esto SIEMPRE se ejecuta
        print("El sistema sigue funcionando correctamente")

# Ejecutar programa
if __name__ == "__main__":
    ejecutar()
