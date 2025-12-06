from Animal import Animal

class Perro(Animal):
    def __init__(self, nombre,raza,edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad} de la raza {self.raza}'
    def hacer_sonido(self):
        return "Guau"
