#Programa25 - Calculadora de descuentos

precio_original = float(input("Escribe el valor de precio: "))
descuento = float(input("Escribe el valor de descuento: "))

precio_con_descuento = precio_original * descuento / 100
precio_final = precio_original - precio_con_descuento

print("Resultado de precio_final: ",precio_final)

if precio_final < 50:
    print('¡Oferta Especial!')
else:
    print('No hacer Oferta especial')
    
print("\n Fin del programa")