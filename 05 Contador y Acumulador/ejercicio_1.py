import os

os.system('cls');

menor = None
mayor = None

while True:
    entrada = input("Ingrese un numero entero positivo (-1 para finalizar): ")
    
    try:
        numero = int(entrada)
    except ValueError:
        print("Error: Debe ingresar un numero entero.")
        continue
    
    if numero == -1:
        break
    
    if numero < 0:
        print("Error: El numero debe ser positivo.")
        continue
    
    if menor is None:
        menor = numero
        mayor = numero
    else:
        if numero < menor:
            menor = numero
        if numero > mayor:
            mayor = numero

if menor is not None:
    print(f"\nMenor numero: {menor}")
    print(f"Mayor numero: {mayor}")
else:
    print("\nNo se ingresaron numeros.")