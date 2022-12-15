""" Crear una tupla con números, luego de pedir un número por teclado, indicar
cuantas veces se repite."""

numeros =(5,6,7,8,5,5,6,90,12,1,12)

numero = int(input("Dame un número"))

#print("El número se repite: " + str(numeros.count(numero)))

print("El número " + str(numero) + " se encuentra en el indice:  " + str (numeros.index(numero)))
