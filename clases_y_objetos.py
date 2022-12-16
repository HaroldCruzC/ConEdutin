class Bicicleta:
    def __init__(self, color, cambios, rin):
        self.color = color
        self.cambios = cambios
        self.rin = rin
        
    def frenar(self):
        return "La bicicleta está frenada"
    
    def avanzar(self):
        return "La bicicle está en movimiento"
    
    def girar(self):
        return "La bicicle está girando"
    
urbana = Bicicleta("Rojo", 8, 27.5)
hibrida = Bicicleta("Azul", 1, 29)

print("Urbana: " +str(urbana.color))
print("Comportamiento de la bicicleta urbana: " +str(urbana.girar()))
print("\n")
print("Hibrida: " +str(hibrida.cambios))
print("Comportamiento de la bicicle hibrida: " +str(hibrida.avanzar()))