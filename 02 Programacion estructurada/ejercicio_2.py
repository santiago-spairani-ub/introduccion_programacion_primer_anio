import os

os.system('cls')

cotizacion_dolar_hoy = float(input("Ingrese la cotizacion del dolar hoy (En pesos): "))
cant_dolares = float(input("Ingrese la cantidad de dolares que tiene: "))

input(f"Usted tiene ${cotizacion_dolar_hoy * cant_dolares} USD.")