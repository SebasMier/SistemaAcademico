# 1. Importacion de clases
from grupo_academico import GrupoAcademico
from persona import Persona
from programa_academico import ProgramaAcademico
from asignatura import Asignatura
from estudiante import Estudiante
from docente import Docente
from administrativo import Administrativo

# 2. Creacion de programas academicos, asignaturas, estudiantes, docentes y administrativos
print("\n========== PROGRAMAS ACADEMICOS Y ASIGNATURAS ==========")


programa1 = ProgramaAcademico(
    "SIS-001", "Ingenieria de Sistemas", "Ingenieria", 8)
programa1.mostrar_informacion()
print("-----------------------------")

programa2 = ProgramaAcademico(
    "ADM-001", "Administracion de Empresas", "Ciencias Economicas", 8)
programa2.mostrar_informacion()
print("-----------------------------")

asignatura1 = Asignatura("MAT-101", "Matematicas I", 4, programa1)
asignatura1.mostrar_informacion()
print("-----------------------------")

asignatura2 = Asignatura(
    "ADM-101", "Fundamentos de Administracion", 3, programa2)
asignatura2.mostrar_informacion()


# Creacion de estudiantes

estudiante1 = Estudiante("Dani Diaz", "1245562187",
                         "DaniDiaz@gmail.com", "D1010", programa1, 3, 4.5)


estudiante2 = Estudiante("Juan Castro", "1084726395",
                         "JuanCas@gmail.com", "JC2020", programa2, 5, 4.2)

# Creacion de docentes

docente1 = Docente("Mateo Palacios", "1038472619", "MateoPa@gmail.com",
                   "E304", programa1.facultad, "Tiempo Completo", 40)


docente2 = Docente("Laura Martinez", "1092837465", "LauMa@gmail.com",
                   "LM305", programa2.facultad, "Medio Tiempo", 20)

# Creacion de administrativos

administrativo1 = Administrativo("Maria Lopez", "1355728010", "MariaLopez@gmail.com",
                                 "E512", "Secretaría Académica", "Secretaria", "Tiempo Completo")


administrativo2 = Administrativo("Natalia Orozco", "1075368294", "NataliaOrozco@gmail.com",
                                 "N513", "Recursos Humanos", "Auxiliar Administrativo", "Tiempo Completo")


# 3. PRUEBA DE POLIMORFISMO


personas = [estudiante1, estudiante2, docente1,
            docente2, administrativo1, administrativo2]
for persona in personas:
    persona.mostrar_informacion()
    persona.realizar_actividad_principal()


# 4. PRUEBA DE MODIFICACION VALIDA

print("\n========== MODIFICACION VALIDA ==========")

asignatura1.cambiar_numero_de_creditos(5)
asignatura1.mostrar_informacion()

# 5. PRUEBA DE MODIFICACION INVALIDA

print("\n========== MODIFICACIONES INVALIDAS ==========")

# Prueba de creditos invalidos

try:
    asignatura1.cambiar_numero_de_creditos(-3)
except ValueError as error:
    print(f"Error: {error}")

# Prueba de semestres invalidos

try:
    programa1.cambiar_numero_de_semestres(0)
except ValueError as error:
    print(f"Error: {error}")

# Prueba de correo vacio

try:
    estudiante1.cambiar_correo("")
except ValueError as error:
    print(f"Error: {error}")


# Prueba creditos invalidos

try:
    asignatura2.cambiar_numero_de_creditos(-3)
except ValueError as error:
    print(f"Error: {error}")

# Prueba de semestres invalidos

try:
    programa2.cambiar_numero_de_semestres(0)
except ValueError as error:
    print(f"Error: {error}")

# Prueba de correo vacio

try:
    estudiante2.cambiar_correo("")
except ValueError as error:
    print(f"Error: {error}")


# persona1 = Persona("Josefina Alba", "1234567", "JosefinaAlba@gmail.com")

grupo1 = GrupoAcademico("GP10", asignatura1, docente1,
                        22, "Lunes, martes, viernes", "8 am", "11 am", "A101")
grupo1.mostrar_informacion_grupo()
