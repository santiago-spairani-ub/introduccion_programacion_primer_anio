import os;

os.system('cls');
precios = []

while True:

    precio = float(input("Ingrese el precio del producto adquirido (O 0 (cero) para salir): $"))
    while precio < 0:
        precio = float(input("[ERROR] Ingrese un valor valido: $"));
    
    if(precio == 0):
        break;

    precios.append(precio);


if(len(precios) != 0):
    total_compra = 0;

    print("\nLos precios ingresados son: \n")
    for i in range(0, len(precios)):
        precio_actual = precios[i];
        total_compra += precio_actual;

        print(f"\t{i + 1}. ${precio_actual}")


    print(f"\nEl total de la compra es ${total_compra}\n");




