from Animal import Animal
from Perro import Perro
from Automovil import Automovil

#un_animal = Animal()
#print(un_animal)

un_perro = Perro('pedro', 'dalmatian', 12)
print(un_perro)
print(un_perro.hacer_sonido())

un_automovil = Automovil("Toyota", "Tercel")
print(un_automovil.arrancar())
print(un_automovil.detener())
print(un_automovil.marca)
print(un_automovil.modelo)
