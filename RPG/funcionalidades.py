import os

def user_input_for_float(mensaje: str = "Ingrese un valor numerico: ") -> float:
    num = 0;
    invalido = True;
    while invalido:
        try:
            num = float(input(mensaje));
            invalido = False
        except ValueError:
            print("[ERROR] Valor ingresado invalido.");
            num = 100
    
    return num;

def elegir_opcion_usuario() -> int:
    invalido = True;
    opcion = 0;
    print("[QUE DESEA REALIZAR?]\n\t1. Atacar\n\t2. Curarse\n");
    while invalido:
        try:
            opcion = float(input("Opcion: "));
            if (opcion != 1 and opcion != 2):
                invalido = False
                print("Opcion invalida. Intente nuevamente.")
            else:
                invalido = False;

        except ValueError:
            print("[ERROR] Valor ingresado invalido.");

    return opcion;