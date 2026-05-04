import os
os.system('cls');

menores_de_18 = 0
mayores_igual_18 = 0
suma_menores = 0
suma_mayores = 0

while True:
    edad = int(input("Ingrese una edad (-1 para finalizar): "))
    
    if edad == -1:
        break

    if edad < 0 or edad > 100:
        print("Edad invalida. Ingrese un valor entre 0 y 100.")
        continue

    if edad < 18:
        menores_de_18 += 1
        suma_menores += edad
    else:
        mayores_igual_18 += 1
        suma_mayores += edad

promedio_menores = suma_menores / menores_de_18 if menores_de_18 > 0 else 0
promedio_mayores = suma_mayores / mayores_igual_18 if mayores_igual_18 > 0 else 0

print(f"\nMenores de 18 años: {menores_de_18}")
print(f"Promedio de edad (menores de 18): {promedio_menores:.2f}")
print(f"\nMayores o iguales a 18 años: {mayores_igual_18}")
print(f"Promedio de edad (18 años o más): {promedio_mayores:.2f}")