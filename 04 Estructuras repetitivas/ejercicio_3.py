import os

os.system('cls');

cant_alumnos = int(input("Ingrese la cantidad de alumnos que rindieron: "));
while cant_alumnos < 1:
    cant_alumnos = int(input("[ERROR] Ingrese una cantidad de alumnos valida: "));

suma_notas = 0;
for i in range(0, cant_alumnos):

    nota = int(input(f"Ingrese la nota del alumno [{i + 1}]: "));
    while nota < 1:
        nota = int(input("[ERROR] Ingrese un valor valido: "));

    suma_notas += nota;

print(f"\nEl promedio de notas es: {suma_notas / cant_alumnos}")
