for num in range(1,11):
    if num > 5:
        print('El numero es mayor')
    elif num <= 0:
        print('El numero es menor')
    else:
        print('El numero es igual a cero')
    if num == 9:
        break
    print(num)