print("Programa14. \nPrograma que calcule el costo total de una compra de combustible \n")
i1 = input("Escriba el valor de precioGasolina95 ")
i2 = input("Escriba el valor de cantidadLitros ")

precio_Gasolina_95 = float(i1)
cantidad_Litros = float(i2)

costo_Sin_Impuesto = precio_Gasolina_95 * cantidad_Litros
costo_Total = costo_Sin_Impuesto * 1.07

print("Escribir el resultado de costo_Total es ",round(costo_Total,2))
