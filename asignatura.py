class Asignatura:
    def __init__(self, codigo, nombre, numero_de_creditos, programa_academico):
        self.codigo = codigo
        self.nombre = nombre
        self.numero_de_creditos = numero_de_creditos
        self.programa_academico = programa_academico

    def mostrar_informacion(self):
        print(f"Codigo: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Numero de Creditos: {self.numero_de_creditos}")
        print(f"Programa Academico: {self.programa_academico.nombre}")
