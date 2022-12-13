"""
edad= int(input("cuantos años tienes "))
graduacion= input(input("Ya te has graduado? (sí) o (no) "))

if edad >18:
    print("Felcitaciones! ya tienes la mayoría de edad")
    if graduacion == "sí":
        print("Felicitaciones por tu graduacion!")
        
"""
        
password = input("ingresa la contraseña: ")

if (len(password))>=8:
    print("Muy bien, contraseña suficientemente larga")
    
    if (password=="Prueba1235"):
        print("Además es la contraseña correcta")
    else:
        print("Pero es incorrecta")
else:
    print("Tu contraseña es correcta e insegura")
        