class ProgramaAcademico:
    def __init__(self, codigo, nombre, facultad, numero_de_semestres):
        self.codigo = codigo
        self.nombre = nombre
        self.facultad = facultad
        self.numero_de_semestres = numero_de_semestres

    def mostrar_informacion(self):
        print(f"Codigo: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Facultad: {self.facultad}")
        print(f"Numero de Semestres: {self.numero_de_semestres}")
