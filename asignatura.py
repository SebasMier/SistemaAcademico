class Asignatura:
    def __init__(self, codigo, nombre, numero_de_creditos, programa_academico):
        self.codigo = codigo
        self.nombre = nombre
        self.cambiar_numero_de_creditos(numero_de_creditos)
        self.programa_academico = programa_academico

    def mostrar_informacion(self):
        print(f"Codigo: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Numero de Creditos: {self._numero_de_creditos}")
        print(f"Programa Academico: {self.programa_academico.nombre}")

    def cambiar_numero_de_creditos(self, nuevo_numero_de_creditos):
        if nuevo_numero_de_creditos <= 0:
            raise ValueError("El numero de creditos debe ser mayor a cero.")
        else:
            self._numero_de_creditos = nuevo_numero_de_creditos
