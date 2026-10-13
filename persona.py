class Persona:
    def __init__(self, nombre, identificacion, correo):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo = correo

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Identificacion: {self.identificacion}")
        print(f"Correo: {self.correo}")
