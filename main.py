from persona import Persona
from programa_academico import ProgramaAcademico
from asignatura import Asignatura
from estudiante import Estudiante
from docente import Docente
from administrativo import Administrativo

persona1 = Persona("Dani Diaz", "1245562187", "DaniDiaz@gmail.com")


programa1 = ProgramaAcademico(
    "SIS-001", "Ingenieria de Sistemas", "Ingenieria", 8)
programa1.mostrar_informacion()

programa2 = ProgramaAcademico(
    "ADM-001", "Administracion de Empresas", "Ciencias Economicas", 8)

asignatura1 = Asignatura("MAT-101", "Matematicas I", 4, programa1)
asignatura1.mostrar_informacion()

asignatura2 = Asignatura(
    "ADM-101", "Fundamentos de Administracion", 3, programa2)
asignatura2.mostrar_informacion()

estudiante1 = Estudiante("Dani Diaz", "1245562187",
                         "DaniDiaz@gmail.com", "D1010", programa1, 3, 4.5)


estudiante2 = Estudiante("Juan Castro", "1084726395",
                         "JuanCas@gmail.com", "JC2020", programa2, 5, 4.2)


docente1 = Docente("Mateo Palacios", "1038472619", "MateoPa@gmail.com",
                   "E304", programa1.facultad, "Tiempo Completo", 40)


docente2 = Docente("Laura Martinez", "1092837465", "LauMa@gmail.com",
                   "LM305", programa2.facultad, "Medio Tiempo", 20)

administrativo1 = Administrativo("Maria Lopez", "1355728010", "MariaLopez@gmail.com",
                                 "E512", "Secretaría Académica", "Secretaria", "Tiempo Completo")


administrativo2 = Administrativo("Natalia Orozco", "1075368294", "NataliaOrozco@gmail.com",
                                 "N513", "Recursos Humanos", "Auxiliar Administrativo", "Tiempo Completo")


personas = [estudiante1, estudiante2, docente1,
            docente2, administrativo1, administrativo2]
for persona in personas:
    persona.mostrar_informacion()
    persona.realizar_actividad_principal()
    print("-----------------------------")

asignatura1.cambiar_numero_de_creditos(5)
asignatura1.mostrar_informacion()

try:
    asignatura1.cambiar_numero_de_creditos(-3)
except ValueError as error:
    print(f"Error: {error}")

try:
    programa1.cambiar_numero_de_semestres(0)
except ValueError as error:
    print(f"Error: {error}")

try:
    estudiante1.cambiar_correo("")
except ValueError as error:
    print(f"Error: {error}")

asignatura2.mostrar_informacion()

try:
    asignatura2.cambiar_numero_de_creditos(-3)
except ValueError as error:
    print(f"Error: {error}")

try:
    programa2.cambiar_numero_de_semestres(0)
except ValueError as error:
    print(f"Error: {error}")


try:
    estudiante2.cambiar_correo("")
except ValueError as error:
    print(f"Error: {error}")
