print("Programa16. \nPrograma que calcule la nota final de asignatura \n")
E1 = input("Escriba el valor de evaluacion_1 ")
E2 = input("Escriba el valor de evaluacion_2 ")
E3 = input("Escriba el valor de evaluacion_3 ")
E4 = input("Escriba el valor de evaluacion_4 ")
E5 = input("Escriba el valor de evaluacion_5 ")

evaluacion_1 = float(E1)
evaluacion_2 = float(E2)
evaluacion_3 = float(E3)
evaluacion_4 = float(E4)
evaluacion_5 = float(E5)

nota_Final = (evaluacion_1 * 0.20) + (evaluacion_2 * 0.15) + (evaluacion_3 * 0.25) + (evaluacion_4 * 0.10) + (evaluacion_5 * 0.30) / 100

print("Escribir el resultado de nota_Final ",round(nota_Final,2))