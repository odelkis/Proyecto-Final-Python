print("Programa6. \nPrograma que calcula el area de un trapecio \n")
i1 = input("Escriba el valor Base 1 ")
i2 = input("Escriba el valor Base 2 ")
i3 = input("Escriba el valor de la Altura ")

Base1 = float(i1)
Base2 = float(i2)
Altura = float(i3)

A = (( Base1 + Base2)*Altura)/2

AR = round(A,2)

print("El area de un trapecio es ",AR)
