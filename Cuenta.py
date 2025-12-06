from Movimiento import Movimiento

class Cuenta:
    def __init__(self, numero_cuenta, saldo, tipo_cuenta, tasa_interes):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__tipo_cuenta = tipo_cuenta
        self.__tasa_interes = tasa_interes
        self.__movimientos = [Movimiento("Credito", saldo)]
        #la relación cuenta-movimiento seria una
        #composición, ya que los movimientos no pueden existir sin una cuenta asociada.
    
    def __str__(self):
        return f"Cuenta {self.__numero_cuenta}, Tipo: {self.__tipo_cuenta}"
    
    def credito(self, amount):
        self.__saldo= self.__saldo + amount
        self.__movimientos.append(Movimiento("Credito", amount))

    def debito(self, amount):
        if amount > self.__saldo:
            return False
        else:
            self.__saldo= self.__saldo - amount
            self.__movimientos.append(Movimiento("Debito", amount))
            return True