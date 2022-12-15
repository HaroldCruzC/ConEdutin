"""def es_par(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")

es_par(56)
    """
"""
def saludar (nombre):
    print("Hola " + nombre + " eres el mejor programador")

saludar("Harold")
"""
"""
def resta(a = None, b=None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return
    return a-b
resutlado = resta(5, 2)

print(resutlado)

"""

def multiplicación(numero = None):
    if numero == None:
        print ("Por favor, introduce un número" )
    else:
        print(f"TABLA DE MULTIPLICAR del NÚMERO {numero}")
        for i  in range(1, 11):
            print (f"{i} x {numero}= {i * numero}")
            
multiplicación(5)
        