import os

os.system('cls');

salario = float(input("Ingrese su salario mensual: "));
porcentaje_ahorro = float(input("Ingrese su porcentaje de ahorro: "));
precio_producto = float(input("Ingrese el valor del producto que quiere comprar: "));

ahorro = salario * (porcentaje_ahorro / 100);
meses = 0;
falta_comprar = True;

while falta_comprar:
    meses += 1;

    total_ahorrado = ahorro * meses;
    if(total_ahorrado >= precio_producto):
        falta_comprar = False;

print(f"\nPara comprar ese producto, debes ahorrar {meses} meses.");
