import os, array, random;

os.system('cls')
diasSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"];
temperaturas = array.array("i", range(7));

continuar = True;

for i in range(len(temperaturas)):
    temperaturas[i] = int(input(f"Ingrese la temperatura del dia {diasSemana[i]} en celcius: ").strip());

suma = 0;
indiceDiaMasCaluroso = 0;

for i in range(len(temperaturas)):
    suma += temperaturas[i];
    if temperaturas[i] > temperaturas[indiceDiaMasCaluroso]:
        indiceDiaMasCaluroso = i;

promedio = suma / len(temperaturas);


while continuar:
    os.system('cls');
    opcion = input("Seleccione la opcion que desee realizar:\n\tA. Ver temperaturas.\n\tB. Ver promedio.\n\tC. Ver dia mas caluroso.\n\tD. Salir\n\nOpcion: ").strip().upper();

    os.system('cls');
    match opcion:
        case "A":
            for i in range(len(temperaturas)):
                print(f"{diasSemana[i]}: {temperaturas[i]} C")
        case "B":
            print(f"El promedio de temperatura de la semana es: {promedio} C");
        case "C":
            print(f"El dia mas caluroso fue el {diasSemana[indiceDiaMasCaluroso]} con {temperaturas[indiceDiaMasCaluroso]} C");
        case "D":
            continuar = False;

    if(continuar):
        input("\n\nPresione Enter para continuar...");
    
