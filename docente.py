from persona import Persona


class Docente(Persona):

    def __init__(self, nombre, identificacion, correo, numero_de_empleado, facultad, tipo_de_contratacion, horas_semanales):
        super().__init__(nombre, identificacion, correo)
        self.numero_de_empleado = numero_de_empleado
        self.facultad = facultad
        self.tipo_de_contratacion = tipo_de_contratacion
        self.horas_semanales = horas_semanales
