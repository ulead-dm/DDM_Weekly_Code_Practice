# Patron para evitar muchos IF si usted tiene que llamar funciones
# que implementan distintas veerciones dee un algoritmo
# y reciben los mismos resultados

def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b

operaciones= {
    "sumar":sumar,
    "restar":restar,
    "multiplicar":multiplicar,
    "dividir":dividir}

def ejecutar_operacion(operacion, valor_1, valor_2):
    if operacion not in operaciones:
        print("Esa operacion no es valida")
    else:
        mi_operacion = operaciones[operacion]
        print(f"La operacion {operacion} tiene por resultado: {mi_operacion(valor_1, valor_2)}")


print(ejecutar_operacion("sumar", 2, 3))
print(ejecutar_operacion("restar", 2, 3))
print(ejecutar_operacion("multiplicar", 2, 3))
print(ejecutar_operacion("dividir", 2, 3))
print(ejecutar_operacion("sumare", 2, 3))