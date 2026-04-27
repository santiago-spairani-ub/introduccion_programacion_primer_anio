import os

codigoProducto = ["P001", "P002", "P003", "P004", "P005"]
nombreProducto = ["Manzana", "Leche", "Pan", "Arroz", "Aceite"]
cantidadStock  = [50, 30, 20, 40, 1]

continuar = True
while continuar:
    os.system('cls')
    opcion = int(input("Seleccione la operacion que desea realizar:\n\n\t1. Mostrar inventario\n\t2. Vender producto\n\t3. Reponer producto\n\t4. Salir\n\nOpcion: "))

    os.system('cls')
    match opcion:
        case 1:
            print("Inventario actual:\n")
            for i in range(len(codigoProducto)):
                print(f"\t{i + 1}. [{codigoProducto[i]}] {nombreProducto[i]} - Stock: {cantidadStock[i]}")

        case 2:
            codigo = input("Ingrese el codigo del producto: ").strip().upper()

            i = 0
            encontrado = False
            while i < len(codigoProducto):
                if codigoProducto[i] == codigo:
                    encontrado = True
                    break
                i += 1

            if not encontrado:
                print("\nError: Codigo no encontrado.")
            elif cantidadStock[i] == 0:
                print(f"\nSin stock para '{nombreProducto[i]}'.")
            else:
                cantidadStock[i] -= 1
                print(f"\nVenta realizada. Stock de '{nombreProducto[i]}': {cantidadStock[i]}")

        case 3:
            codigo = input("Ingrese el codigo del producto: ").strip().upper()

            i = 0
            encontrado = False
            while i < len(codigoProducto):
                if codigoProducto[i] == codigo:
                    encontrado = True
                    break
                i += 1

            if not encontrado:
                print("\nError: Codigo no encontrado.")
            else:
                cantidad = int(input(f"Cantidad a reponer para '{nombreProducto[i]}': "))

                while cantidad <= 0:
                    cantidad = int(input("Error: Ingrese una cantidad valida: "))

                cantidadStock[i] += cantidad
                print(f"\nStock de '{nombreProducto[i]}' actualizado: {cantidadStock[i]}")

        case 4:
            continuar = False

    if continuar:
        input("\nPresione Enter para continuar...")