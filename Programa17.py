print("Programa 17. \nConversion de unidades de medidas ")

unidad = float(input("Ingresar la cantidad "))
gramos = unidad / 0.001
kilogramos = unidad / 1000
centimetros = unidad / 0.01
metros = unidad / 100

print(f"La medida equivalente de {unidad} kilogramos a gramos es de {gramos} gramos \nDe {unidad} gramos a kilogramos es de {kilogramos} kilogramos \nDe {unidad} metros a centimetros es de {centimetros} centimetros \nDe {unidad} centimetros a metros es de {metros} metros ")