import os, random

os.system('cls');

valoresProporcionados = [];
for i in range(3):
    valoresProporcionados.append(random.randint(1, 10));
    print(f"{valoresProporcionados[i]}");


mayor = valoresProporcionados[0];

for i in range(3):
    if valoresProporcionados[i] > mayor:
        mayor = valoresProporcionados[i];

print(f"El mayor es: {mayor}")
