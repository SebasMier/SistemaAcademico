# ==================================================
# 1. IMPORTACION DE CLASES
# ==================================================

from grupo_academico import GrupoAcademico
from persona import Persona
from programa_academico import ProgramaAcademico
from asignatura import Asignatura
from estudiante import Estudiante
from docente import Docente
from administrativo import Administrativo
from excepciones import EstudianteMatriculadoError, CapacidadGrupoMaxima, EstudianteNoMatriculado, AsignaturaNoEncontrada, ProgramaAcademicoNoEncontrado

# ==================================================
# 2. FUNCIONES DE BUSQUEDA
# ==================================================


def buscar_asignatura(lista_asignaturas, codigo_buscado):
    for asignatura in lista_asignaturas:
        if asignatura.codigo == codigo_buscado:
            return asignatura
    raise AsignaturaNoEncontrada("La asignatura no existe")


def buscar_programa(lista_programas, codigo_buscado):
    for programa in lista_programas:
        if programa.codigo == codigo_buscado:
            return programa
    raise ProgramaAcademicoNoEncontrado("El programa academico no existe")


# ==================================================
# 3. CREACION DE PROGRAMAS ACADEMICOS
# ==================================================


print("\n========== PROGRAMAS ACADEMICOS ==========")


programa1 = ProgramaAcademico(
    "SIS-001", "Ingenieria de Sistemas", "Ingenieria", 8)
programa1.mostrar_informacion()
print("-----------------------------")

programa2 = ProgramaAcademico(
    "ADM-001", "Administracion de Empresas", "Ciencias Economicas", 8)
programa2.mostrar_informacion()
print("-----------------------------")


programas = [programa1, programa2]


# ==================================================
# 4. CREACION DE ASIGNATURAS
# ==================================================

print("\n========== ASIGNATURAS ==========")

asignatura1 = Asignatura("MAT-101", "Matematicas I", 4, programa1)
asignatura2 = Asignatura(
    "ADM-101", "Fundamentos de Administracion", 3, programa2)

asignatura1.mostrar_informacion()
print("-----------------------------")
asignatura2.mostrar_informacion()

asignaturas = [asignatura1, asignatura2]

# ==================================================
# 5. CREACION DE ESTUDIANTES
# ==================================================


estudiante1 = Estudiante("Dani Diaz", "1245562187",
                         "DaniDiaz@gmail.com", "D1010", programa1, 3, 4.5)


estudiante2 = Estudiante("Juan Castro", "1084726395",
                         "JuanCas@gmail.com", "JC2020", programa2, 5, 4.2)

estudiante3 = Estudiante("Pedro Almada", "1114253860",
                         "PA@gmail.com", "PA2022", programa1, 3, 4)


# ==================================================
# 6. CREACION DE DOCENTES
# ==================================================


docente1 = Docente("Mateo Palacios", "1038472619", "MateoPa@gmail.com",
                   "E304", programa1.facultad, "Tiempo Completo", 40)


docente2 = Docente("Laura Martinez", "1092837465", "LauMa@gmail.com",
                   "LM305", programa2.facultad, "Medio Tiempo", 20)


# ==================================================
# 7. CREACION DE ADMINISTRATIVOS
# ==================================================


administrativo1 = Administrativo("Maria Lopez", "1355728010", "MariaLopez@gmail.com",
                                 "E512", "Secretaría Académica", "Secretaria", "Tiempo Completo")


administrativo2 = Administrativo("Natalia Orozco", "1075368294", "NataliaOrozco@gmail.com",
                                 "N513", "Recursos Humanos", "Auxiliar Administrativo", "Tiempo Completo")


# ==================================================
# 8. PRUEBA DE CLASE ABSTRACTA PERSONA
# ==================================================

print("\n========== PRUEBA DE CLASE ABSTRACTA ==========")

try:
    persona1 = Persona(
        "Josefina Alba", "1234567", "JosefinaAlba@gmail.com"
    )
except TypeError as error:
    print(error)


# ==================================================
# 9. PRUEBA DE POLIMORFISMO
# ==================================================


print("\n========== PRUEBA DE POLIMORFISMO ==========")

personas = [estudiante1, estudiante2, docente1,
            docente2, administrativo1, administrativo2]
for persona in personas:
    persona.mostrar_informacion()
    persona.realizar_actividad_principal()

# ==================================================
# 10. PRUEBAS DE MODIFICACIONES
# ==================================================


print("\n========== MODIFICACION VALIDA ==========")

asignatura1.cambiar_numero_de_creditos(5)
asignatura1.mostrar_informacion()


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


# ==================================================
# 11. CREACION DE GRUPOS ACADEMICOS
# ==================================================

print("\n========== GRUPOS ACADEMICOS ==========")


grupo1 = GrupoAcademico("GP10", asignatura1, docente1,
                        2, "Lunes, martes, viernes", "8 am", "11 am", "A101")
grupo2 = GrupoAcademico("GP20", asignatura2, docente2,
                        18, "Miercoles y jueves", "7:45 am", "10:30 am", "B200")


grupo1.mostrar_informacion_grupo()
print("-----------------------------")
grupo2.mostrar_informacion_grupo()

# ==================================================
# 12. PRUEBAS DE MATRICULA Y RETIRO
# ==================================================

print("\n========== MATRICULA DE ESTUDIANTES ==========")

# Matricula exitosa
grupo1.matricular_estudiante(estudiante1)
grupo1.matricular_estudiante(estudiante2)
grupo1.mostrar_estudiantes()
grupo1.mostrar_informacion_grupo()

# Prueba de capacidad maxima del grupo
try:
    grupo1.matricular_estudiante(estudiante3)
except CapacidadGrupoMaxima as error:
    print(error)

print("\n========== RETIRO DE ESTUDIANTE ==========")

# Retiro exitoso
grupo1.retirar_estudiante("D1010")

grupo1.mostrar_informacion_grupo()


# ==================================================
# 13. PRUEBAS DE EXCEPCIONES PERSONALIZADAS
# ==================================================

print("\n========== PRUEBAS DE EXCEPCIONES ==========")

# Prueba de programa academico no encontrado
try:
    buscar_programa(programas, "MED-999")
except ProgramaAcademicoNoEncontrado as error:
    print(error)

# Prueba de asignatura no encontrada
try:
    buscar_asignatura(asignaturas, "MAT-999")
except AsignaturaNoEncontrada as error:
    print(error)

# Prueba de estudiante duplicado
try:
    grupo1.matricular_estudiante(estudiante2)
except EstudianteMatriculadoError as error:
    print(error)


# Prueba de estudiante no matriculado
try:
    grupo1.retirar_estudiante("D9999")
except EstudianteNoMatriculado as error:
    print(error)
