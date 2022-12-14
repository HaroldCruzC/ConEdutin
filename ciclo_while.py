#calculadora de Indide de Masas Corportal

print("Calculadora de Indide de Masa Corportal")

contador = 0

while contador !=2:
    contador = int(input("Quieres seguir calculando el IMC? 1.Sí y 2.No \n"))
    
    if contador ==1:
        estatura = float(input("Ingrese su estatura en metros: "))
        peso = float(input("Ingrese su peso en Kilogramos: "))
        resultado=round(peso/(estatura ** 2))
    
        if resultado<18.5:
            print(f"IMC {resultado}=Bajo de peso")
        elif 18.5 < resultado <24.99:
            print(f"IMC {resultado}= Peso Normal")
        elif 25 < resultado < 30:
            print(f"IMC {resultado}= Sobre Peso")
        elif resultado >30:
            print(f"IMC {resultado}=Tiene obesidad")

    elif contador ==2:
        print("Hasta pronto")

print("Gracias por utilizar la calculadora de IMC")

