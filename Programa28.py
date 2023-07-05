#Programa28 - Usuario ingrese una calificacion

calif = float(input("Escribir la calificacion: "))

if calif >= 90 and calif <= 100 :
    print('Evaluacion de A')
if calif >= 80 and calif <= 89 :
    print('Evaluacion de B')
if calif >= 70 and calif <= 79 :
    print('Evaluacion de C')
if calif >= 60 and calif <= 69 :
    print('Evaluacion de D')
if calif < 60 :
    print('Evaluacion de F')
    
print("\n Fin del programa")
