"""

def suma(*args):
    s=0
    for arg in args:
        s += arg
    
    return s

resultado = suma(3,4,5,)

print (resultado)

"""
"""
def lenguaje(nombre, *lenguajes):
    print(f"Hola {nombre}")
    print ("Tus lenguajes favoritos son: {lenguajes}")
    
lenguaje("Harold","Python", "JavaScript", "html")

"""

def lenguaje(nombre, **kwargs):
    print(f"Hola {nombre}")
    print ("Buscando información acerca de tus lenguajes favoritos...")
    print ("Cargando información...\n")
    
    print ("Información:  ")
    contador = 0
    for clave in kwargs:
        contador +=1
        print (f"Tu {contador} lenguaje favorito es: {kwargs[clave]}")
        
lenguaje("Harold", lenguaje1= "Python", lenguaje2 ="HTML", lenguaje3="JavaScript")
    