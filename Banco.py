class Banco:

    def __init__(self,nombre, fundacion):
        self.__nombre = nombre
        self.__fundacion = fundacion
        self.__sucursales = []

    def __str__(self):
        return f"Banco: {self.__nombre}, Fundacion: {self.__fundacion}"
    