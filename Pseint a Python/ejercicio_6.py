import os, array, random

os.system('cls');
numeros = array.array("i", range(20))
valido = True;
contador = 0;

while valido and contador <= 19:
    os.system('cls');
    num = int(input(f"Ingrese el numero para la posicion {contador + 1}: ").strip());

    if num >= 0:
        numeros[contador] = num;
    elif num < 0:
        print("Error: Se ingreso un numero negativo. Finalizando programa.");
        valido = False;

    contador += 1;


if valido:
    suma = 0;
    for i in range(len(numeros)):
        suma += numeros[i];

    print(f"El promedio de los numeros ingresados es: {suma / len(numeros)}")






