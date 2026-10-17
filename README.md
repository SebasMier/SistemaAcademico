
# Sistema de Gestión Académica

El **Sistema de Gestión Académica** es un proyecto desarrollado en **Python**, el cual nos permite organizar la información de una institución educativa, en este caso la información de una universidad.

El sistema incluye programas académicos, asignaturas, estudiantes, docentes y administrativos. El desarrollo de este sistema fue realizado con base en la Programación Orientada a Objetos (POO).

## Objetivo del proyecto

El objetivo de este proyecto fue poder aplicar los conceptos básicos aprendidos de la Programación Orientada a Objetos mientras se realizaba el Sistema Académico.

## Estructura del proyecto

El proyecto se divide de la siguiente manera:

- **`persona.py`**: contiene la clase `Persona`, la cual guarda los datos básicos de las personas (nombre, identificación y correo).

- **`programa_academico.py`**: contiene la clase `ProgramaAcademico`, la cual guarda los datos básicos de los programas de la universidad (código, nombre, facultad y número de semestres).

- **`asignatura.py`**: contiene la clase `Asignatura`, la cual guarda los datos básicos de las asignaturas (código, nombre, número de créditos y el programa académico al cual pertenece).

- **`estudiante.py`**: contiene la clase `Estudiante`, que hereda de `Persona` y agrega datos como: código estudiantil, programa académico, semestre y promedio acumulado.

- **`docente.py`**: contiene la clase `Docente`, que también hereda de `Persona` y agrega datos como: número de empleado, facultad, tipo de contratación y las horas que trabaja semanalmente.

- **`administrativo.py`**: contiene la clase `Administrativo`, que también hereda de `Persona` y agrega datos como: cargo, dependencia, jornada y número de empleado.

- **`main.py`**: es el archivo principal del programa donde se crean los objetos y nos permite comprobar que las clases y sus métodos están funcionando de manera correcta.

- **`README.md`**: en este archivo se realiza la descripción del proyecto, su objetivo y las instrucciones para poder ejecutar el proyecto.

## Conceptos de POO utilizados

### 1. Clases y objetos

Se crearon diferentes clases para poder organizar la información del sistema académico, como `Persona`, `Docente`, `Asignatura`, `ProgramaAcademico`, `Estudiante` y `Administrativo`, y a partir de estas se crearon los objetos `programa1`, `programa2`, `estudiante1`, `estudiante2`, `asignatura1`, `asignatura2`, `docente1`, `docente2`, `administrativo1` y `administrativo2`.

### 2. Encapsulamiento

Se utilizó el encapsulamiento para controlar la modificación de algunos atributos, como `_correo`, `_numero_de_semestres` y `_numero_de_creditos`, y así evitar cambios incorrectos, por ejemplo, que haya semestres negativos.

**Algunos ejemplos de encapsulamiento:**

- **`_correo`**: guarda el correo de una persona.
- **`_numero_de_semestres`**: guarda el número de semestres de un programa académico.
- **`_numero_de_creditos`**: guarda el número de créditos de una asignatura.

Para modificar estos atributos se crearon métodos:

- **`cambiar_correo()`**: permite modificar el correo de una persona.
- **`cambiar_numero_de_semestres()`**: permite modificar el número de semestres de un programa académico.
- **`cambiar_numero_de_creditos()`**: permite modificar el número de créditos de una asignatura.

Estos métodos comprueban que los valores ingresados cumplan con las condiciones que se establecieron antes de que se realicen cambios.

### 3. Herencia

Se usó la herencia para que clases como `Estudiante`, `Docente` y `Administrativo` hereden de la clase `Persona` sus atributos y métodos.

Así, las 3 clases hacen uso de los datos y métodos ya creados en la clase `Persona`, como `nombre`, `identificacion` y `_correo`, para evitar escribir estos nuevamente.

### 4. Sobreescritura de métodos

La **sobreescritura de métodos** se aplicó en las clases `Estudiante`, `Docente` y `Administrativo`.

Cada una tiene su propia versión del método `mostrar_informacion()`, que permite mostrar los datos generales heredados de `Persona` junto con la información específica de cada clase.

Por ejemplo:

- **`Estudiante`**: muestra `codigo_estudiantil`, `programa_academico`, `semestre` y `promedio_acumulado`.
- **`Docente`**: muestra `numero_de_empleado`, `facultad`, `tipo_de_contratacion` y `horas_semanales`.
- **`Administrativo`**: muestra `numero_de_empleado`, `dependencia`, `cargo` y `jornada`.

### 5. Polimorfismo

Se creó una lista llamada `personas` que contiene objetos como:

- `estudiante1`
- `estudiante2`
- `docente1`
- `docente2`
- `administrativo1`
- `administrativo2`

Esta lista se recorre mediante un ciclo `for`, donde se ejecutan los métodos:

- **`mostrar_informacion()`**
- **`realizar_actividad_principal()`**

Aunque se llaman los mismos métodos, cada objeto muestra información y realiza una actividad diferente dependiendo de su clase.

## Instrucciones de ejecución

Para poder ejecutar este proyecto debes tener instalado Python 3. Durante el desarrollo se utilizó la versión 3.14.7.

1. Descarga el repositorio desde GitHub.
2. Abre la carpeta del proyecto en Visual Studio Code.
3. Ejecuta el comando `python main.py`.

Al hacer esto, el programa mostrará la información de los objetos creados, las actividades que realizan y los resultados de las pruebas de validación.

## Uso de herramientas de apoyo

- **Visual Studio Code**: editor usado para escribir y ejecutar el código.

- **Git y GitHub**: utilizados para guardar cambios y almacenar el proyecto.

- **[Markdown Guide](https://www.markdownguide.org/basic-syntax/)**: se uso esta pagina para aprender la sintaxis básica de Markdown y elaborar el archivo `README.md`.


## Autor

**Nombre: Juan Sebastian Mier Acevedo**