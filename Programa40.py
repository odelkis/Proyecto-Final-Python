print("programa 40. calcular el area de un triángulo")

import FunciónB
Base = float(input("escribir la base: "))
Altura = float(input("escribir la altura: "))
Area = FunciónB.calcular_area_triangulo(Base,Altura)
     
print(f"El area de un triangulo es", Area)
