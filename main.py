from persona import Persona
from programa_academico import ProgramaAcademico
from asignatura import Asignatura
from estudiante import Estudiante
from docente import Docente
from administrativo import Administrativo

persona1 = Persona("Dani Diaz", "1245562187", "DaniDiaz@gmail.com")
persona1.mostrar_informacion()


programa1 = ProgramaAcademico(
    "SIS-001", "Ingenieria de Sistemas", "Ingenieria", 8)
programa1.mostrar_informacion()


asignatura1 = Asignatura("MAT-101", "Matematicas I", 4, programa1)
asignatura1.mostrar_informacion()

estudiante1 = Estudiante("Dani Diaz", "1245562187",
                         "DaniDiaz@gmail.com", "D1010", programa1, 3, 4.5)
estudiante1.mostrar_informacion()
estudiante1.realizar_actividad_principal()


docente1 = Docente("Mateo Palacios", "1038472619", "MateoPa@gmail.com",
                   "E304", "Facultad de Ingenieria", "Tiempo Completo", 40)
docente1.mostrar_informacion()
docente1.realizar_actividad_principal()

administrativo1 = Administrativo("Maria Lopez", "1355728010", "MariaLopez@gmail.com",
                                 "E512", "Secretaría Académica", "Secretaria", "Tiempo Completo")
administrativo1.mostrar_informacion()
administrativo1.realizar_actividad_principal()
