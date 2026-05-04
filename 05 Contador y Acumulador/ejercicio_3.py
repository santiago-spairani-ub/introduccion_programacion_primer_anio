import os 
os.system('cls');

pares = 0
impares = 0

while True:
    numero = int(input("Ingrese la terminacion de la patente (0-9) o -1 para salir: "))
    
    if numero == -1:
        break
    
    if 0 <= numero <= 9:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        print("Error: Ingrese un numero entre 0 y 9")

print(f"\nVehiculos con patente par: {pares}")
print(f"Vehiculos con patente impar: {impares}")
print(f"Total de vehiculos: {pares + impares}")