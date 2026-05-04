import os

while True:
    os.system('cls');

    valor_producto = float(input("Ingrese el valor del producto (O ingrese 0 (cero) para salir.): "));
    while valor_producto < 0:
        valor_producto = float(input("[Error] Ingrse un numero valido: "))

    if(valor_producto == 0):
        break;

    dinero_usuario = float(input("Ingrese con cuanto va a pagar: "))
    while dinero_usuario < valor_producto:
        dinero_usuario = float(input("[Error] El dinero es insuficiente. Por favor ingrese un monto valido: "));

    vuelto = dinero_usuario - valor_producto;

    print(f"\nPrducto adquirido por ${valor_producto}.")
    if(vuelto != 0):
        print(f"\nSu vuelto es ${vuelto}.");

    input("\n\nPresione ENTER para continuar...")


print("\n\nFinalizando programa...\n")
