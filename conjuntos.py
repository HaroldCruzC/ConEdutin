"""
add // Añade un leemnto al ifnal del conjunt.
clear// Elimina toda la información del conjunto.
pop// Devuelve y elimina un elemento arbritario o devuelve un error si está vacio.
remove// Intenta eliminiar un elemento del conjunto, si no existe eleva un error.
unión// Devuelve un conjunto con todos los elementos de ambos conjuntos.

"""

#1 forma de crear conjuntos

alumnos= {"Andrea", "Ruby", "Marcos", "Marlon", "Jose",}

#print(alumnos)

#2 forma de crear conjuntos
lenguajes = set(["Pyton", "PHP", "Java", "C", "C++",])
#lenguajes.add("C#")
#lenguajes.pop
#lenguajes.remove("Java")


todos = alumnos.union(lenguajes)

#print(lenguajes)

print(todos)

