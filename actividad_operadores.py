#Programa que raliza operaciones básicas y compara los núneros ingresados

#aquí el programa pide dos números
print("ingresa dos números cualquiera para realizar las operaciones básicas y compararlos")
primerNumero = int(input("ingresa el primer número"))
segundoNumero = int(input("ingresa el segundo número"))

#resultados de las operaciones entre los números ingresados

#suma de dos núemros de la manera chiva
print(f"la suma de los dos números es :{primerNumero + segundoNumero}")

#Multiplicación de dos números de la manera chiva
print(f"la multiplicación de los dos números es :{primerNumero * segundoNumero}")



# Comparación de dos números, y de la manera chiva

print(f"¿los números son iguales?: {primerNumero == segundoNumero}")

print(f"¿El primer número es menor que el segundo?: {primerNumero < segundoNumero}")

print(f"¿El segundo número es mayor o igual al primero?: {segundoNumero >= primerNumero}")
