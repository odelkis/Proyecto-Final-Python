#Programa26 - Clasificacion de triangulos

a = float(input("Escribe el valor de lado1: "))
b = float(input("Escribe el valor de lado2: "))
c = float(input("Escribe el valor de lado3: "))

if a == b and b == c:
    print('El triangulo es equilatero')
else:
    if a == b or a == c or b == c:
        print('El triangulo es isosceles')
    else:
        print('El triangulo es escaleno')
    
print("\n Fin del programa")