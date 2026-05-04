import os
os.system('cls');
numero = int(input("Ingrese un numero entero: "))

suma = 0

print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    suma += resultado

print(f"\nSuma de todos los resultados: {suma}")