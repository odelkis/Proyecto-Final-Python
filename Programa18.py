print("Programa 18. \nCalcule del interes compuesto ")

ci = float(input("Ingrese la capital inicial "))
i = float(input("Ingrese la tasa de interes "))
n = float(input("Ingrese el periodo de ahorro "))

cf = Ci * (1 + i) ** n

print(f"La capital final es de {round(cf,2)} ")