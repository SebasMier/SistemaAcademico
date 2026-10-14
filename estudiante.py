from persona import Persona


class Estudiante(Persona):

    def __init__(self, nombre, identificacion, correo, codigo_estudiantil, programa_academico, semestre, promedio_acumulado):
        super().__init__(nombre, identificacion, correo)
        self.codigo_estudiantil = codigo_estudiantil
        self.programa_academico = programa_academico
        self.semestre = semestre
        self.promedio_acumulado = promedio_acumulado

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Codigo Estudiantil: {self.codigo_estudiantil}")
        print(f"Programa Academico: {self.programa_academico.nombre}")
        print(f"Semestre: {self.semestre}")
        print(f"Promedio Acumulado: {self.promedio_acumulado}")

    def realizar_actividad_principal(self):
        print(
            f"El estudiante {self.nombre} esta cursando el programa {self.programa_academico.nombre} y se encuentra en el semestre {self.semestre}.")
