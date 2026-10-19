from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre, identificacion, correo):
        self.nombre = nombre
        self.identificacion = identificacion
        self.cambiar_correo(correo)

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Identificacion: {self.identificacion}")
        print(f"Correo: {self._correo}")

    def cambiar_correo(self, nuevo_correo):
        if nuevo_correo == "":
            raise ValueError("El correo no puede estar vacio.")
        else:
            self._correo = nuevo_correo

    @abstractmethod
    def realizar_actividad_principal(self):
        pass
