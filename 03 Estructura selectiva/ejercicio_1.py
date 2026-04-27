import os

os.system('cls')
cantidadBoletosMaxima = 5;

precioBoleto = float(input("Ingrese el precio del boleto: "));
while precioBoleto <= 0:
    precioBoleto = float(input("Error. Ingrese un valor valido para el precio del boleto: "));

os.system('cls');

cantidadSolicitada = int(input("Ingrese la cantidad solicitada por el cliente: "));
while cantidadSolicitada <= 0:
    cantidadSolicitada = float(input("Error. Ingrese un valor valido para la cantidad solicitada: "));

os.system('cls');

if cantidadSolicitada > cantidadBoletosMaxima:
    print(f"Error: No se pueden vender mas de {cantidadBoletosMaxima} boletos por persona");
else:
    print(f"Debe abonar ${precioBoleto * cantidadSolicitada}");