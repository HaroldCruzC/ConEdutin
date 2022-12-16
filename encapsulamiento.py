class Persona:
        def __init__(self, identificacion, nombre, edad):
            self.__identificacion = identificacion
            self.nombre = nombre
            self.edad = edad
            
        def saludo(self):
            return "Hola " + self.nombre
        
        def getIdentificacion(self):
            return self.__identificacion
        
persona1 = Persona(106980893, "Harold", 55)
    
#print(persona1._Persona__identificacion)

print(persona1.getIdentificacion())
print(persona1.nombre)
print(persona1.edad)


    