print("Bienvenido al conversor de monedas")

def conversor(moneda_actual, valor, moneda_a_convertir):
    if moneda_actual == 1:
        
            def dolarTo():
                if moneda_a_convertir =="1":
                    print(f"{valor} dolares equivale a ${valor * 600} colones costarricenses")
                elif moneda_a_convertir == "2":
                    print(f"${valor} dolares equivale a ¥{valor * 6.37} Yuanes")
                elif moneda_a_convertir == "3":
                    print(f"${valor} dolares equivale a €{valor * 0.76} Euros")
                else:
                    print("No se reconece la moneda_a_convertir")
                    
            dolarTo
            
    if moneda_actual == 2:
        
            def euroTo():
                if moneda_a_convertir =="1":
                    print(f"{valor} euros equivale a ${valor * 635} colones costarricenses")
                elif moneda_a_convertir == "2":
                    print(f"${valor} euros equivale a ¥{valor * 7.41} Yuanes")
                elif moneda_a_convertir == "3":
                    print(f"${valor} euros equivale a €{valor * 0.86} Euros")
                else:
                    print("No se reconece la moneda_a_convertir")
                    
            euroTo
            
            
            
moneda_actual= int(input("Ingrese su moneda actual: \n 1.Dolar \n 2.Euros \n"))

valor = float(input("Ingrese el valor a convertir: \n"))

moneda_a_convertir=input("¿A qué moneda quiere convertirlo? \n 1.Color Costarricense \n 2.Yuanes \n 3.Libras Esterlinas \n")

conversor(moneda_actual, valor, moneda_a_convertir)