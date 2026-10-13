from persona import Persona
from programa_academico import ProgramaAcademico
from asignatura import Asignatura

persona1 = Persona("Dani Diaz", "3245562187", "DaniDiaz@gmail.com")
persona1.mostrar_informacion()

programa1 = ProgramaAcademico(
    "SIS-001", "Ingenieria de Sistemas", "Ingenieria", 8)
programa1.mostrar_informacion()

asignatura1 = Asignatura("MAT-101", "Matematicas I", 4, programa1)
asignatura1.mostrar_informacion()
