productos = 0
compra_total = 0

while productos < 5:
    precio_del_producto = float(input("Ingrese el precio del producto: "))
    a_impuesto = precio_del_producto * 0.07
    impuesto = a_impuesto + precio_del_producto
    compra_total += impuesto
    productos += 1
    
print(f"El total a pagar es de {round(compra_total,2)} Balboas")

print("Fin del programa")