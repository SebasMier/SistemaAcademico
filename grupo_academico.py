from horario import Horario


class GrupoAcademico:

    def __init__(self, codigo_del_grupo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_finalizacion, salon):
        self.codigo_del_grupo = codigo_del_grupo
        self.asignatura = asignatura
        self.docente = docente
        self.capacidad_maxima = capacidad_maxima
        self.estudiantes = []
        self.horario = Horario(dia, hora_inicio, hora_finalizacion, salon)
