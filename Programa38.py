def sumar_numeros_pares(num):
    suma = 0
    for num in range(num, 21):
        if num % 2 == 0:
            suma += num
    return suma

resultado = sumar_numeros_pares(1)
print("La suma de los numeros pares entre 1 y 20 es: ",resultado)