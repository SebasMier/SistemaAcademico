from persona import Persona


class Administrativo(Persona):

    def __init__(self, nombre, identificacion, correo, numero_de_empleado, dependencia, cargo, jornada):
        super().__init__(nombre, identificacion, correo)
        self.numero_de_empleado = numero_de_empleado
        self.dependencia = dependencia
        self.cargo = cargo
        self.jornada = jornada
