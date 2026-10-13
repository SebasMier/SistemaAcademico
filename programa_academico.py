class ProgramaAcademico:
    def __init__(self, codigo, nombre, facultad, numero_de_semestres):
        self.codigo = codigo
        self.nombre = nombre
        self.facultad = facultad
        self.cambiar_numero_de_semestres(numero_de_semestres)

    def mostrar_informacion(self):
        print(f"Codigo: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Facultad: {self.facultad}")
        print(f"Numero de Semestres: {self._numero_de_semestres}")

    def cambiar_numero_de_semestres(self, nuevo_numero_de_semestres):
        if nuevo_numero_de_semestres <= 0:
            raise ValueError("El numero de semestres debe ser mayor a cero.")
        else:
            self._numero_de_semestres = nuevo_numero_de_semestres
