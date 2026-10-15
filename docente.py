from persona import Persona


class Docente(Persona):

    def __init__(self, nombre, identificacion, correo, numero_de_empleado, facultad, tipo_de_contratacion, horas_semanales):
        super().__init__(nombre, identificacion, correo)
        self.numero_de_empleado = numero_de_empleado
        self.facultad = facultad
        self.tipo_de_contratacion = tipo_de_contratacion
        self.horas_semanales = horas_semanales

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Numero de Empleado: {self.numero_de_empleado}")
        print(f"Facultad: {self.facultad}")
        print(f"Tipo de Contratacion: {self.tipo_de_contratacion}")
        print(f"Horas Semanales: {self.horas_semanales}")

    def realizar_actividad_principal(self):
        print(
            f"{self.nombre} dicta sus clases en la facultad de {self.facultad}")
