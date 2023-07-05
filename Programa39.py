def calcular_area_triangulo(Base, Altura):
    Area = (Base * Altura) / 2
    return Area

Base = float(input("Escribir la base: "))
Altura = float(input("Escribir la altura: "))

Area = calcular_area_triangulo(Base,Altura)
print("El area del triangulo ", Area)