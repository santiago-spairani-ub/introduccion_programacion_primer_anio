import array, random, os;

os.system('cls');

numeros = array.array('i', range(10));
mensaje = "numeros ingresados: ";

for i in range(len(numeros)):
    numeros[i] = random.randint(1, 100);
    mensaje += f"{numeros[i]}, ";


print(mensaje);

continuar = True;
while continuar:
    buscado = int(input("Ingrese el numero buscado: ").strip());
    for i in range(len(numeros)):
        if(numeros[i] == buscado):
            continuar = False;
            print(f"Se encontro el numero buscado en el indice: {i}") 

    if(continuar):
        print("No se encontro el numero buscado.");

