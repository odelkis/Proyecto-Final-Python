print("Programa20. \nCalcular la salario neto \n")
i1 = input("Escriba el valor de Salario Bruto ")

Salario_Bruto = float(i1)

Seguro_Social = Salario_Bruto * 0.08
Seguro_Educativo = Salario_Bruto * 0.02
Impuesto = Salario_Bruto * 0.15
Prestamo = 100
Salario_Neto = Salario_Bruto - Seguro_Social - Seguro_Educativo - Impuesto - Prestamo

print("Escribir el resultado de Salario_Neto es ",Salario_Neto)