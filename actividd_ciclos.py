# Para solicitar información

nombre = input("Ingresa tu nombre")
materias = 5

contador= 1
sumatoria=0

while contador <= materias:
    nombre_materia = input("Ingresa el nombre de la ("+str (contador)+ ") materia:")
    calificacion = float(input("calificiones obtenidas en" + str (nombre_materia)+ ": "))
    
#sumar la calificación de la sumatoria

sumatoria = sumatoria + calificacion

#aumentar el contador para no hacer un ciclo infinito

contador = contador + 1

#hacer calculos e imprimir resultados

promedio = sumatoria / materias

print ("*** Resultados ***")
print (f"Hola, {nombre} tienes un promedio de {promedio} en el 5to semestre.")
