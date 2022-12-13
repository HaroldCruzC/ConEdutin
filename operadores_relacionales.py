# a = 5
# b = 8

#  print ( a == b)  ¿No iguales a y b?
#  print ( a != b) ¿son distintos a y b?
#  print ( a > b) ¿Esa  mayor que b?
#  print ( a >= b) ¿Es a mayor o igual que b?
#  print ( a < b) ¿Es a menor que b?
#  print ( a <= b) ¿es a menor o igual que b?



#Solicitud de datos al usuario

a = int(input(f'Ingrese el primer numero (1): '))
b = int(input(f'Ingrese el segundo numero (2): '))

# Numeros iguales "=="
print(f'Los Numero son iguales?: {a == b}')
#Numeros distintos "!="
print(f'Los Numero son distintos?: {a != b}')
#Numero mayor que otro
print(f'El primer numero (1) es mayor que el segundo numero(2)?: {a >b}')