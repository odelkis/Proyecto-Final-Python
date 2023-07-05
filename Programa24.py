#Programa - Calcular tres valores que indique cual es el mayor

a = int(input("Escriba el numero1: "))
b = int(input("Escriba el numero2: "))
c = int(input("Escriba el numero3: "))

if a > b and a > c :
    print('El numero1 mayor es a =', a)
if b > a and b > c :
    print('El numero2 mayor es b =', b)
if c > a and c > b :
    print('El numero3 mayor es c =', c)
    
print("\n Fin del programa ")    