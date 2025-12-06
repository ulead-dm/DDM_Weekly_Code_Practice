class Cliente:
    def __init__(self, id, nombre, categoria):
        self.__id = id
        self.__nombre = nombre
        self.__categoria = categoria
        self.__cuentas = []
        # La relación cliente-cuenta seria una
        #agregación, ya que el cliente puede existir sin cuentas,
        # y las cuentas pueden existir sin un cliente asociado.

    def __str__(self):
        return f"Cliente[ID: {self.id}, Nombre: {self.nombre}, Categoria: {self.categoria}]"  
    
    def agregar_cuenta(self, nueva_cuenta):
        self.__cuentas.append(nueva_cuenta)