import os 
os.system('cls');

nombre = input("Ingrese un nombre: ")
nombre_invertido = ""

for i in range(len(nombre) - 1, -1, -1):
    nombre_invertido += nombre[i]

print(f"Nombre original: {nombre}")
print(f"Nombre invertido: {nombre_invertido}")