import os

os.system('cls');

pago_por_hora = float(input("Ingrese cuando cobra por hora (En pesos): "));
horas_semanales = float(input("Ingrese cuantas horas realizo esta semana: "));

print(f"Esta semana cobrara ${pago_por_hora * horas_semanales}");