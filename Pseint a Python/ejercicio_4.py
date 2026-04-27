import os;

continuar = True;
while continuar:
    os.system('cls');
    operacion = int(input("Seleccione la operacion\n\t1. Sumar\n\t2. Restar\n\t3. Multiplicar\n\t4. Dividir\n\t5. Salir\n\nOperacion: ").strip());

    num1 = 0;
    num2 = 0;
    if operacion > 0 and operacion < 5:
        num1 = int(input("Ingrese el primer numero a operar: ").strip())
        num2 = int(input("Ingrese el segundo numero a operar: ").strip())
        resultado = 0;

        match operacion:
            case 1:
                resultado = num1 + num2;
            case 2:
                resultado = num1 - num2;
            case 3:
                resultado = num1 * num2;
            case 4:
                if num2 == 0:
                    print("Error: No es posible dividir por 0.");
                else:
                    resultado = num1 / num2;
                    print(f"\nEl resultado es: ", resultado)
            case 5:
                continuar = False;

    if operacion != 4 and num2 != 0:
        print(f"\nEl resultado es: ", resultado)

    input("\nPresione Enter para continuar...")

