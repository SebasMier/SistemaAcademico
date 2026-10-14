from persona import Persona


class Estudiante(Persona):

    def __init__(self, nombre, identificacion, correo, codigo_estudiantil, programa_academico, semestre, promedio_acumulado):
        super().__init__(nombre, identificacion, correo)
        self.codigo_estudiantil = codigo_estudiantil
        self.programa_academico = programa_academico
        self.semestre = semestre
        self.promedio_acumulado = promedio_acumulado
