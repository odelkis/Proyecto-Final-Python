valor = 1

while valor <= 3:
    numero = float(input("Escribir el numero: "))
    if numero > 0:
        print('El numero es positivo')
    elif numero < 0:
        print('El numero es negativo')
    else:
        print('El numero es igual a cero')
    
    valor += 1