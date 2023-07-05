print("Programa12. \nPrograma que calcule el interes a pagar pr un prestamo \n")

monto = int(input("Escriba el valor monto "))
tasa = int(input("Escriba el valor tasa "))
plazo = int(input("Escriba el valor de plazo "))

tasa_Porcentaje = tasa * 100
tasa_Mensual =tasa / 12
cuota = monto * (tasa_Mensual / (1 -(1+tasa_Mensual)**(-plazo)))
interes_Mensual = monto * tasa_Mensual
capital_Mensual = cuota - interes_Mensual

print("Escribir el resultado de cuota es ",round(cuota,2))
print("Escribir el resultado de interes_Mensual es ",round(interes_Mensual,2))
print("Escribir el resultado de capital_Mensual es ",round(capital_Mensual,2))