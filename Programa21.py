#Programa 21 - Calcular si una persona paga impuestos

salario = float(input("Escriba el Salario: "))
                
if salario > 3000:
    impuesto = salario * 0.07
    print("Esta Persona debe abonar impuesto", impuesto)
else:
    print("No Debe abonar impuestos")
    
print("\ Fin del programa ")