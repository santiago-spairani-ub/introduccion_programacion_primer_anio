import random
import array
import os;

os.system('cls')

numeros = array.array('i', range(15));
mensaje = "Se ingresaron los numeros: ";

for i in range(len(numeros)):
    numeros[i] = random.randint(1, 100);
    mensaje += f"{numeros[i]}, ";

print(mensaje);

mas_alto = numeros[0];
mas_bajo = numeros[0];

for i in range(len(numeros)):
    if(numeros[i] > mas_alto):
        mas_alto = numeros[i];

    if(numeros[i] < mas_bajo):
        mas_bajo = numeros[i];

print(f"El numero mas alto es {mas_alto} y el mas bajo es {mas_bajo}");