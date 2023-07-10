#Se importan las funciones de "FuncionP.py"
from FuncionP import problema1, problema2, problema3, problema4, problema5, problema6, problema7, problema8, problema9, problema10, problema11, problema12, problema13, problema14, problema15, problema16, problema17, problema18, problema19, problema20, problema21, problema22, problema23, problema24, problema25, problema26, problema27, problema28, problema29, problema30, problema31, problema32, problema33, problema34, problema35, problema36, problema37, problema38, problema39

print("Bienvenido al Programa Principal")
    
#Bucle Inicial
while True:
    #Se ingresa el nombre del programa que desea llamar
    nom_programa = input("Ingresar el numero del programa que desea ejecutar (o 'salir' para terminar): ")
    
    #Se utiiza la estructura condicionales para la funcion llamada
    if nom_programa == "salir":
        print("¡Muchas Gracias!")
        break
    elif nom_programa == "1":
        respuesta = problema1()
        print("La respuesta al intercambiar variable A, B y C es ", respuesta)
    elif nom_programa == "2":
        respuesta = problema2()
        print("La respuesta al asignar valores de A, B y AUX es ", respuesta)
    elif nom_programa == "3":
        D = problema3()
        print("La respuesta de la suma de valores es: ", round(D,2))
    elif nom_programa == "4":
        Area = problema4()
        print("El area del triangulo es: ", Area)
    elif nom_programa == "5":
        respuesta = problema5()
        print("El area del perimetro es: ", respuesta)
    elif nom_programa == "6":
        respuesta = problema6()
        print("El area de trapecio es: ", respuesta)
    elif nom_programa == "7":
        Vol = problema7()
        print("El volumen del prisma es: ", Vol)
    elif nom_programa == "8":
        A, B, C, D, E, F = problema8()
        print("La respuesta de A es ", round(A,2))
        print("La respuesta de B es ", round(B,2))
        print("La respuesta de C es ", round(C,2))
        print("La respuesta de D es ", round(D,2))
        print("La respuesta de E es ", round(E,2))
        print("La respuesta de F es ", round(F,2))
    elif nom_programa == "9":
        c1,c2,c3,c4,c5 = problema9()
        print("La respuesta de c1 es ", round(c1,2))
        print("La respuesta de c2 es ", round(c2,2))
        print("La respuesta de c3 es ", round(c3,2))
        print("La respuesta de c4 es ", round(c4,2))
        print("La respuesta de c5 es ", round(c5,2))
    elif nom_programa == "10":
        pies,pulgadas = problema10()
        print("La respuesta de pies es ", pies)
        print("La respuesta de pulgadas es ", pulgadas)
    elif nom_programa == "11":
        D = problema11()
        print("La regla de tres simple es ",round(D,2))
    elif nom_programa == "12":
        cuota, interes_Mensual, capital_Mensual = problema12()
        print("La cuota a pagar es ",round(cuota,2))
        print("El interes_Mensual es ",round(interes_Mensual,2))
        print("La capital_Mensual es ",round(capital_Mensual,2))
    elif nom_programa == "13":
        salario_Neto = problema13()
        print("El salario_Neto es ",round(salario_Neto,2))
    elif nom_programa == "14":
        costo_Total = problema14()
        print("El costo_Total es ",round(costo_Total,2))
    elif nom_programa == "15":
        total_De_Compra = problema15()
        print("El total_De_Compra es ",round(total_De_Compra,2))
    elif nom_programa == "16":
        nota_Final = problema16()
        print("El resultado de la nota_Final es",round(nota_Final,2))
    elif nom_programa == "17":
        gramos,kilogramos,centimetros,metros = problema17()
        print("La medida de gramos es ", gramos)
        print("La medida de kilogramos es ", kilogramos)
        print("La medida de centimetros es ", centimetros)
        print("La medida de metros es ", metros)
    elif nom_programa == "18":
        cf = problema18()
        print(f"La capital final es ", round(cf,2))
    elif nom_programa == "19":
        Total_Sin_Impuesto,Total_Con_Impuesto,Total_De_Compra = problema19()
        print("El Total_Sin_Impuesto es ", round(Total_Sin_Impuesto,2))
        print("El Total_Con_Impuesto es ", round(Total_Con_Impuesto,2))
        print("El Total_De_Compra es de ", round(Total_De_Compra,2))
    elif nom_programa == "20":
        Salario_Neto = problema20()
        print("El Salario_Neto es ",Salario_Neto)
    elif nom_programa == "21":
        respuesta = problema21()
        print(respuesta)
    elif nom_programa == "22":
        respuesta = problema22()
        print(respuesta)
    elif nom_programa == "23":
        respuesta = problema23()
        print(respuesta)
    elif nom_programa == "24":
        respuesta = problema24()
        print(respuesta)
    elif nom_programa == "25":
        precio_final = problema25()
        print(precio_final)
    elif nom_programa == "26":
        respuesta = problema26()
        print(respuesta)
    elif nom_programa == "27":
        respuesta = problema27()
        print(respuesta)
    elif nom_programa == "28":
        respuesta = problema28()
        print(respuesta)
    elif nom_programa == "29":
        respuesta = problema29()
    elif nom_programa == "30":
        respuesta = problema30()
    elif nom_programa == "31":
        respuesta = problema31()
    elif nom_programa == "32":
        respuesta = problema32()
    elif nom_programa == "33":
        respuesta = problema33()
    elif nom_programa == "34":
        respuesta = problema34()
    elif nom_programa == "35":
        respuesta = problema35()
    elif nom_programa == "36":
        compra_total = problema36()
        print(f"El total a pagar es ", round(compra_total,2))
    elif nom_programa == "37":
        respuesta = problema37()
    elif nom_programa == "38":
        respuesta = problema38()
        print(f"La suma de los numeros pares entre 1 y 20 es", respuesta)
    elif nom_programa == "39":
        Area = problema39()
        print("El area del triangulo ", Area)
        
    else:
        print("Nombre del problema no valido")