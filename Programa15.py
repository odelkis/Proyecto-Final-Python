print("Programa15. \nPrograma que calcule la compra de tres articulos en un supermercado \n")
a1 = input("Escriba el valor de precio1 ")
a2 = input("Escriba el valor de precio2 ")
a3 = input("Escriba el valor de precio3 ")

precio_1 = float(a1)
precio_2 = float(a2)
precio_3 = float(a3)

precio_Total = precio_1 + precio_2 + precio_3
costo_Sin_Impuesto = precio_Total * 0.07
total_De_Compra = precio_Total + costo_Sin_Impuesto

print("Escribir el resultado de total_De_Compra es ",round(total_De_Compra,2))
