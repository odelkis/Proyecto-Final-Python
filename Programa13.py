print("Programa13. \nPrograma que calcule el salario neto de sus empleados \n")
i1 = input("Escriba el valor salarioBruto ")

salario_Bruto = int(i1)

seguro_Social = salario_Bruto * 0.0514
seguro_Educativo = salario_Bruto * 0.02
cuota_Prestamo = 50
salario_Neto = salario_Bruto - seguro_Social - seguro_Educativo - cuota_Prestamo

print("Escribir el resultado de salario_Neto es ",round(salario_Neto,2))
