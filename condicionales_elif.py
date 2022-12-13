###En una escuela de conducción se tiene un programa que dependiendo 
# de la edd del usuario debe mostar el tipo de licencia a la qu tiene derecho.
# condición 1:  si es menor a 16 no puede conducir
# condición 2: Si es menor a 18 puede obtener un permiso de conducir
# condición 3: si es menor a 70  entonces puede obtener una licencia estándar
# condición 4: si es mayor a 70 entonces necesita una licencia especial.

edad = int(input("introduce tu edad: "))

if edad <16:
    print("No tienes edad para conducir")
elif edad <18:
    print("Puedes obtener un permiso de conducir")
elif edad <70:
    print("Puedes obtener una licencia estándar")
else:
    print("Necesitas obtener una licencia especial")