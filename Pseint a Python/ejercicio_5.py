import os, array, random

productos = [""] * 5;
precios = array.array("i", range(5))

productos[0] = "Hamburguesa";
productos[1] = "Pizza";
productos[2] = "Tacos";
productos[3] = "Milanesa";
productos[4] = "Pancho";

for i in range(len(productos)):
    precios[i] = random.randint(100, 200);

continuar = True;
while continuar:
    os.system('cls');

    print("Seleccione una opcion del menu para conocer su precio: \n")
    for i in range (len(productos)):
        print(f"\t{i + 1}. {productos[i]}");
    
    print(f"\t{len(productos) + 1}. Salir")

    opcion = int(input("\nOpcion: ").strip())

    if opcion > 0 and opcion < (len(productos) + 1):
        print(f"\n\tProducto: {productos[opcion - 1]}.\n\tPrecio: ${precios[opcion - 1]}")
    elif opcion == 6:
        continuar = False;
    else:
        print("Error: Opcion invalida.")


    input("\nPresione Enter para continuar...");


