def problema1():
    print("Programa 1. Intercambiar valores")
    A = 10
    B = 0
    C = 0
    B = A
    C = B
    A = A
    return A,B,C

def problema2():
    print("Programa 2. Asignar variables")
    A = 10
    B = 20
    AUX = 0
    Aux = A
    A = B
    B = AUX
    return A,B,AUX

def problema3():
    print("Programa 3. Suma de tres valores")
    A = float(input("Escribir el valor de A: "))
    B = float(input("Escribir el valor de B: "))
    C = float(input("Escribir el valor de C: "))
    D = (A + B + C) / 3
    return D
    
def problema4():
    print("Programa 4. Area de un triangulo")
    Base = float(input("Escribir la base: "))
    Altura = float(input("Escribir la altura: "))
    Area = (Base * Altura) / 2
    return Area

def problema5():
    print("Programa 5. Perimetro de un triangulo")
    AB = float(input("Escriba el valor AB "))
    BC = float(input("Escriba el valor BC "))
    CD = float(input("Escriba el valor CD "))
    DA = float(input("Escriba el valor DA "))
    PR = (AB + BC + CD + DA)/2
    return PR
    
def problema6():
    print("Programa 6. Area de un trapecio")
    Base1 = float(input("Escriba el valor Base 1 "))
    Base2 = float(input("Escriba el valor Base 2 "))
    Altura = float(input("Escriba el valor de la Altura "))
    AR = (( Base1 + Base2)*Altura)/2
    return AR

def problema7():
    print("Programa 7. Volumen de un prisma")
    Largo = float(input("Escriba el valor Largo "))
    Ancho = float(input("Escriba el valor Ancho "))
    Altura = float(input("Escriba el valor de la Altura "))
    Vol = Largo * Ancho * Altura
    return Vol

def problema8():
    print("Programa 8. Ecuaciones algebraicas")
    x = float(input("Escriba el valor de x "))
    A = 20 - (7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 +(9 * x) + 18
    D = (6 * x) + 4 +(8 * x) + 2
    E = ((5 * x) + 78) / 28
    F = (((6 * x) - 7) / 4) + (((3 * 7) -5)/7)
    return A, B, C, D, E, F

def problema9():
    print("Programa 9. Ecuaciones algebraicas")
    a = float(input("Escriba el valor de a "))
    b = float(input("Escriba el valor de b "))
    c = float(input("Escriba el valor de c "))
    c1 = (4 * a) + (3 * b)
    c2 = (21 * a) - 18 + (8 * b) - 5
    c3 = (4 * a) + (3 * b) + 7
    c4 = (2 * a) + (3 * b) - (c**5)
    c5 = (2 * a) + (3 * b) - (c**2)
    return c1,c2,c3,c4,c5

def problema10():
    print("Programa 10. Conversion de unidades")
    m = float(input("Escribir el valor de m "))
    pies = m * 3.2801
    pulgadas = m * 39.37
    return pies,pulgadas

def problema11():
    print("Programa 11. Regla de tres simples")
    a = float(input("Escriba el valor de a "))
    b = float(input("Escriba el valor de b "))
    c = float(input("Escriba el valor de c "))
    D = (b * c) / a
    return D

def problema12():
    print("Programa 12. Calcular interes a pagar")
    monto = int(input("Escriba el valor monto "))
    tasa = int(input("Escriba el valor tasa "))
    plazo = int(input("Escriba el valor de plazo "))
    tasa_Porcentaje = tasa * 100
    tasa_Mensual =tasa / 12
    cuota = monto * (tasa_Mensual / (1 -(1+tasa_Mensual)**(-plazo)))
    interes_Mensual = monto * tasa_Mensual
    capital_Mensual = cuota - interes_Mensual
    return cuota,interes_Mensual,capital_Mensual

def problema13():
    print("Programa 13. Calcular Salario Neto")
    salario_Bruto = float(input("Escriba el valor salario Bruto "))
    seguro_Social = salario_Bruto * 0.0514
    seguro_Educativo = salario_Bruto * 0.02
    cuota_Prestamo = 50
    salario_Neto = salario_Bruto - seguro_Social - seguro_Educativo - cuota_Prestamo
    return salario_Neto

def problema14():
    print("Programa 14. Costo total de combustible")
    precioGasolina95 = float(input("Escriba el valor de precioGasolina95 "))
    cantidadLitros = float(input("Escriba el valor de cantidadLitros "))
    costo_Sin_Impuesto = precioGasolina95 * cantidadLitros
    costo_Total = costo_Sin_Impuesto * 1.07
    return costo_Total

def problema15():
    print("Programa 15. Compra de tres articulos")
    precio1 = float(input("Escriba el valor de precio1 "))
    precio2 = float(input("Escriba el valor de precio2 "))
    precio3 = float(input("Escriba el valor de precio3 "))
    precio_Total = precio1 + precio2 + precio3
    costo_Sin_Impuesto = precio_Total * 0.07
    total_De_Compra = precio_Total + costo_Sin_Impuesto
    return total_De_Compra

def problema16():
    print("Programa 16. Calcular nota final")
    evaluacion_1 = float(input("Escriba el valor de evaluacion_1 "))
    evaluacion_2 = float(input("Escriba el valor de evaluacion_2 "))
    evaluacion_3 = float(input("Escriba el valor de evaluacion_3 "))
    evaluacion_4 = float(input("Escriba el valor de evaluacion_4 "))
    evaluacion_5 = float(input("Escriba el valor de evaluacion_5 "))
    nota_Final = (evaluacion_1 * 0.20) + (evaluacion_2 * 0.15) + (evaluacion_3 * 0.25) + (evaluacion_4 * 0.10) + (evaluacion_5 * 0.30) / 100
    return nota_Final

def problema17():
    print("Programa 17. Unidades de Medidas")
    unidad = float(input("Ingresar la cantidad "))
    gramos = unidad / 0.001
    kilogramos = unidad / 1000
    centimetros = unidad / 0.01
    metros = unidad / 100
    return gramos,kilogramos,centimetros,metros

def problema18():
    print("Programa 18. Interes Compuesto")
    ci = float(input("Ingrese la capital inicial "))
    i = float(input("Ingrese la tasa de interes "))
    n = float(input("Ingrese el periodo de ahorro "))
    cf = ci * (1 + i) ** n
    return cf

def problema19():
    print("Programa 19. Compra de 5 articulos")
    articulo1 = float(input("Escriba el valor articulo1 "))
    articulo2 = float(input("Escriba el valor articulo2 "))
    articulo3 = float(input("Escriba el valor articulo3 "))
    articulo4 = float(input("Escriba el valor articulo4 "))
    articulo5 = float(input("Escriba el valor articulo5 "))
    Total_Sin_Impuesto = articulo1 + articulo2 + articulo3 + articulo4 + articulo5
    Costo_Con_Impuesto = Total_Sin_Impuesto * 0.07
    Total_Con_Impuesto = Total_Sin_Impuesto + Costo_Con_Impuesto
    Total_De_Compra = Total_Sin_Impuesto / 5
    return Total_Sin_Impuesto,Total_Con_Impuesto,Total_De_Compra

def problema20():
    print("Programa 20. Calcular salario neto de los empleados")
    Salario_Bruto = float(input("Escriba el valor de Salario Bruto "))
    Seguro_Social = Salario_Bruto * 0.08
    Seguro_Educativo = Salario_Bruto * 0.02
    Impuesto = Salario_Bruto * 0.15
    Prestamo = 100
    Salario_Neto = Salario_Bruto - Seguro_Social - Seguro_Educativo - Impuesto - Prestamo
    return Salario_Neto

def problema21():
    print("Programa 21. Calcular si la persona debe pagar impuesto")
    salario = float(input("Escriba el Salario: "))
    if salario > 3000:
        impuesto = salario * 0.07
        return("Esta Persona debe abonar impuesto", impuesto)
    else:
        return("No Debe abonar impuestos")

def problema22():
    print("Programa 22. Calcular la temperatura")
    temperature = float(input("Escriba la temperatura: "))
    if temperature < 20:
        if temperature < 10:
            return('Nivel azul')
        else:
            return('Nivel verde')
    else:
        if temperature < 30:
            return('Nivel naranja')
        else:
            return('Nivel rojo')
    
def problema23():
    print("Programa 23. Calcular edad")
    valor = float(input("Escriba su edad: "))
    if valor > 6 and valor < 18:
        return('Cierto')
    else:
        return('False')
        
def problema24():
    print("Programa 24. Calcular el valor mayor de tres numeros")
    a = int(input("Escriba el numero1: "))
    b = int(input("Escriba el numero2: "))
    c = int(input("Escriba el numero3: "))
    if a > b and a > c :
        return('El numero1 mayor es a =', a)
    if b > a and b > c :
        return('El numero2 mayor es b =', b)
    if c > a and c > b :
        return('El numero3 mayor es c =', c)

def problema25():
    print("Programa 25. Calculadora de descuentos")
    precio_original = float(input("Escribe el valor de precio: "))
    descuento = float(input("Escribe el valor de descuento: "))
    precio_con_descuento = precio_original * descuento / 100
    precio_final = precio_original - precio_con_descuento
    print("El resultado de precio_final es",precio_final)
    if precio_final < 50:
        return('¡Oferta Especial!')
    else:
        return('No hacer Oferta especial')
    
def problema26():
    print("Programa 26. Clasificacion de triangulos")
    a = float(input("Escribe el valor de lado1: "))
    b = float(input("Escribe el valor de lado2: "))
    c = float(input("Escribe el valor de lado3: "))
    if a == b and b == c:
        return('El triangulo es equilatero')
    else:
        if a == b or a == c or b == c:
            return('El triangulo es isosceles')
        else:
            return('El triangulo es escaleno')
        
def problema27():
    print("Programa 27. Clasificar el numero segun su signo")
    numero = float(input("Escribir el numero: "))
    if  numero > 0:
        return('El numero es positivo')
    elif numero < 0:
        return('El numero es negativo')
    else:
        return('El numero es igual a cero')

def problema28():
    print("Programa 28. Evaluar Calificacion")
    calif = float(input("Escribir la calificacion: "))
    if calif >= 90 and calif <= 100 :
        return('Evaluacion de A')
    if calif >= 80 and calif <= 89 :
        return('Evaluacion de B')
    if calif >= 70 and calif <= 79 :
        return('Evaluacion de C')
    if calif >= 60 and calif <= 69 :
        return('Evaluacion de D')
    if calif < 60 :
        return('Evaluacion de F')

def problema29():
    print("Programa 29. Evaluacion de Nota (while)")
    valor = 1
    while valor <= 5:
        calif = float(input("Escribir la calificacion: "))
        if calif >= 90 and calif <= 100 :
            Evaluacion = 'A'
        if calif >= 80 and calif <= 89 :
            Evaluacion = 'B'
        if calif >= 70 and calif <= 79 :
            Evaluacion = 'C'
        if calif >= 60 and calif <= 69 :
            Evaluacion = 'D'
        if calif < 60 :
            Evaluacion = 'F'
            
        print(f"La calificacion es {Evaluacion}")
        valor += 1
        
def problema30():
    print("Programa 30. Clasificacion de numero segun su signo (while)")
    valor = 1
    while valor <= 3:
        numero = float(input("Escribir el numero: "))
        if numero > 0:
            numero = "positivo"
        elif numero < 0:
            numero = "negativo"
        else:
            numero = "igual a cero"
        
        print(f"La respuesta es {numero}")
        valor +=1

def problema31():
    print("Programa 31. Bucle de while utilizando break")
    valor = 1
    while valor <= 10:
        print(valor)
        if valor == 7:
            break
        valor += 1
        
def problema32():
    print("Programa 32. Secuencia de numero utilizando for")
    valor = 1
    for valor in range(1, 10):
        print(valor)

def problema33():
    print("Programa 33. Tabla de Multiplicar con ciclos for")
    for i in range(1, 13):
        print("Tabla de multiplicar del", i)
        print("--------------------------")
        for j in range(1, 13):
            resultado = i * j
            print(i, "x", j, "=", resultado)
        print()

def problema34():
    print("Programa 34. Bucle while (Numeros par o impar)")
    num = 0
    while num <= 15:
        print(num)
        if num % 2 == 0:
            print('el numero es un par')
        else:
            print('el numero es impar')
        num += 1

def problema35():
    print("Programa 35. Bucle for (Lista de numeros del 1 al 10)")
    for num in range(1,11):
        if num > 5:
            print('El numero es mayor')
        elif num <= 0:
            print('El numero es menor')
        else:
            print('El numero es igual a cero')
        if num == 9:
            break
        print(num)
        
def problema36():
    print("Programa 36. Bucle while (Compra de 5 productos)")
    productos = 0
    compra_total = 0
    while productos < 5:
        precio_del_producto = float(input("Ingrese el precio del producto: "))
        a_impuesto = precio_del_producto * 0.07
        impuesto = a_impuesto + precio_del_producto
        compra_total += impuesto
        productos += 1
    
    return compra_total
   
def problema37():
    print("Programa 37. Bucle while (Calcular el valor mayor de tres numeros)")
    num = 1
    a = int(input("Escriba el numero1: "))
    b = int(input("Escriba el numero2: "))
    c = int(input("Escriba el numero3: "))

    while num <= 5:
        print(num)
        if a > b and a > c :
            print('El numero1 mayor es a =', a)
        if b > a and b > c :
            print('El numero2 mayor es b =', b)
        if c > a and c > b :
            print('El numero3 mayor es c =', c)
        num += 1
        
def problema38():
    print("Programa 38. Calcular los numeros pares entre 1 y 20")
    suma = 0
    for num in range(2, 21, 2):
        suma += num
    return suma

def problema39():
    print("Programa 39. Area de un triangulo")
    Base = 8
    Altura = 2
    Area = (Base * Altura) / 2
    return Area    
