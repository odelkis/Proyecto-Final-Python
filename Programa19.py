print("Programa19. \nCalcular la compra de 5 articulos \n")
a1 =input("Escriba el valor articulo1 ")
a2 =input("Escriba el valor articulo2 ")
a3 =input("Escriba el valor articulo3 ")
a4 =input("Escriba el valor articulo4 ")
a5 =input("Escriba el valor articulo5 ")
     
articulo1 = float(a1)
articulo2 = float(a2)     
articulo3 = float(a3)
articulo4 = float(a4)
articulo5 = float(a5)

Total_Sin_Impuesto = articulo1 + articulo2 + articulo3 + articulo4 + articulo5
Costo_Con_Impuesto = Total_Sin_Impuesto * 0.07
Total_Con_Impuesto = Total_Sin_Impuesto + Costo_Con_Impuesto
Total_De_Compra = Total_Sin_Impuesto / 5

print("Escribir el resultado de Total_Sin_Impuesto es ", round(Total_Sin_Impuesto,2))
print("Escribir el resultado de Total_Con_Impuesto es ", round(Total_Con_Impuesto,2))
print("Escribir el resultado de Total_De_Compra es ", round(Total_De_Compra,2))