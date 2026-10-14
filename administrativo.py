from persona import Persona


class Administrativo(Persona):

    def __init__(self, nombre, identificacion, correo, numero_de_empleado, dependencia, cargo, jornada):
        super().__init__(nombre, identificacion, correo)
        self.numero_de_empleado = numero_de_empleado
        self.dependencia = dependencia
        self.cargo = cargo
        self.jornada = jornada

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Numero de Empleado: {self.numero_de_empleado}")
        print(f"Dependencia: {self.dependencia}")
        print(f"Cargo: {self.cargo}")
        print(f"Jornada: {self.jornada}")

    def realizar_actividad_principal(self):
        print(f"{self.nombre} trabaja como {self.cargo} en {self.dependencia}")
