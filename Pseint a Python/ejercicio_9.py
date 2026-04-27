import os

asientos = [False] * 10

continuar = True
while continuar:
    os.system('cls');
    opcion = int(input("Seleccione la operacion que desea realizar:\n\n\t1. Ver asientos disponibles.\n\t2. Vender entrada\n\t3. Salir.\n\nOpcion: ").strip());

    os.system('cls');
    match opcion:
        case 1:
            print("Disponibilidad de los asientos:\n")
            for i in range(len(asientos)):
                disponibilidad = ("Disponible", "Ocupado")[asientos[i]];
                print(f"\t{i + 1}. {disponibilidad}.");

        case 2:
            asiento = int(input(f"Seleccione el asiento a vender del 1 al {len(asientos)}: ").strip());

            while asiento < 0 or asiento > len(asientos):
                asiento = int(input("Error: Ingrese un asiento valido: ").strip())

            if(asientos[asiento - 1]):
                print(f"\nEl asiento se encuentra ocupado.");
            else:
                asientos[asiento - 1] = True;
                print("\nAsiento vendido exitosamente.");
        case 3:
            continuar = False

    if continuar:
        input("\nPresione Enter para continuar...")