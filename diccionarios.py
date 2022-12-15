#Primera forma de crear un diccionario.
"""
diccionario = {
    "Nombre": "Sara",
    "Edad": 28,
    "Cocumento": 456234
}

print (diccionario)


#Segunda forma de crear un diccionario.

diccionario_segunda_forma = dict(Nombre="Paola",
                                 Edad=37,
                                 Documento=2394534)

print(diccionario_segunda_forma)

#Tercera forma de crear un diccion

diccionario_tercera_forma = dict([
   ("Nombre", "Sara"),
   ("Edad", 37), 
   ("Documento", 232345)
])

print(diccionario_tercera_forma)

"""

inventario ={"Manazanas": 235, "Peras": 400, "Naranjas": 250, "Sandías": 500}

#print(inventario.keys())

#print(inventario.values())

print(inventario.items())