# Importamos la excepción personalizada
from excepciones import ErrorCliente

class Cliente:
    def __init__(self, nombre, email):
        # Atributos privados (doble guion bajo)
        self.__nombre = nombre
        self.__email = email

        # Validamos los datos al crear el cliente
        self.validar()

    def validar(self):
        # Si el nombre está vacío → error
        if not self.__nombre:
            raise ErrorCliente("El nombre no puede estar vacío")

        # Si el email no tiene @ → error
        if "@" not in self.__email:
            raise ErrorCliente("Email inválido")

    # Método para obtener el nombre (encapsulación)
    def get_nombre(self):
        return self.__nombre

    # Método para obtener el email
    def get_email(self):
        return self.__email
