from Cuenta import Cuenta
from Cliente import Cliente

class Tarjeta:
    def __init__(self, numero_tarjeta, cliente: Cliente, cuenta: Cuenta):
        self.__numero_tarjeta = numero_tarjeta
        self.__cliente = cliente
        self.__cuenta = cuenta  

    def __str__(self):
        return f"Tarjeta[Numero: {self.__numero_tarjeta}, Cliente: {self.__cliente}, Cuenta: {self.__cuenta}]"

    def cargoTarjeta(self, amount):
        return self.__cuenta.debito(amount)