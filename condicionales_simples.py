# primer ejemplo  Crear un programa que reciba el número de años que tiene nuestra computadora
#imprimir en consola si es nueva o vieja
#  Condiciones: si es menor o igual a 2 años es nuevo.
# pero si es mayor a 2 años es viejo.

anios = int(input("cuantos años tiene tu computadora: "))

if anios >= 0 and anios <=2:
    print("tu computadora es nueva")
else:
    print("tu computadora es vieja")
    
edad = int(input("cuantos años tiene"))

if edad >=18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad, no puede pasar")
    
print("hasta la próxima")
