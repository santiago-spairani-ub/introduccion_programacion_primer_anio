import os
os.system('cls');

n = int(input("Ingrese cantidad de empleados: "))

total_salarios = 0
cantidad_mas_200k = 0
cantidad_categoria3_menos_50k = 0
legajo_mayor_salario = None
mayor_salario = -1
menor_salario = float('inf')
total_por_categoria = {1: 0, 2: 0, 3: 0}

for _ in range(n):
    legajo = input("Ingrese legajo: ")
    categoria = int(input("Ingrese categoría (1, 2 o 3): "))
    salario = float(input("Ingrese salario: "))
    
    total_salarios += salario
    
    if salario > 200000:
        cantidad_mas_200k += 1
    
    if categoria == 3 and salario < 50000:
        cantidad_categoria3_menos_50k += 1
    
    if salario > mayor_salario:
        mayor_salario = salario
        legajo_mayor_salario = legajo
    
    if salario < menor_salario:
        menor_salario = salario
    
    total_por_categoria[categoria] += salario

promedio_salario = total_salarios / n

print("\n" + "="*50)
print("INFORME DE SALARIOS")
print("="*50)
print(f"Importe total de salarios: ${total_salarios:,.2f}")
print(f"Empleados que ganan mas de $200000: {cantidad_mas_200k}")
print(f"Empleados categoría 3 con salario < $50000: {cantidad_categoria3_menos_50k}")
print(f"Legajo del empleado que mas gana: {legajo_mayor_salario} (${mayor_salario:,.2f})")
print(f"Sueldo mas bajo: ${menor_salario:,.2f}")
print(f"Total de sueldos por categoria:")
for cat in range(1, 4):
    print(f"  Categoria {cat}: ${total_por_categoria[cat]:,.2f}")
print(f"Salario promedio: ${promedio_salario:,.2f}")
print("="*50)