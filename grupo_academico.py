from horario import Horario


class GrupoAcademico:

    def __init__(self, codigo_del_grupo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_finalizacion, salon):
        self.codigo_del_grupo = codigo_del_grupo
        self.asignatura = asignatura
        self.docente = docente
        self.capacidad_maxima = capacidad_maxima
        self.estudiantes = []
        self.horario = Horario(dia, hora_inicio, hora_finalizacion, salon)

    def mostrar_informacion_grupo(self):
        print(f"Codigo del grupo: {self.codigo_del_grupo}")
        print(f"Asignatura: {self.asignatura.nombre}")
        print(f"Docente: {self.docente.nombre}")
        print(f"Capacidad maxima: {self.capacidad_maxima}")
        print(f"Estudiantes matriculados: {len(self.estudiantes)}")

        print(f"Dia: {self.horario.dia}")
        print(f"Hora de inicio: {self.horario.hora_inicio}")
        print(f"Hora de finalizacion: {self.horario.hora_finalizacion}")
        print(f"Salon: {self.horario.salon}")

    def matricular_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def retirar_estudiante(self, codigo_estudiantil):
        for estudiante_matriculado in self.estudiantes:
            if estudiante_matriculado.codigo_estudiantil == codigo_estudiantil:
                self.estudiantes.remove(estudiante_matriculado)

    def mostrar_estudiantes(self):
        for estudiante_matriculado in self.estudiantes:
            print(estudiante_matriculado.nombre)
