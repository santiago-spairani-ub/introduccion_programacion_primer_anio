import os, Utilidades, random;
os.system('cls');

continuar = True;
numero_buscado = random.randint(1000, 9999);
#print(f"El numero secreto es: {numero_buscado}")

while continuar:

    num_ingresado = int(input("\nIngrese el numero secreto: "));

    if(Utilidades.sonIguales(num_ingresado, -1)):
        print(f"Perdiste! El numero era: {numero_buscado}");
        continuar = False;
        continue;

    if(Utilidades.esMayor(num_ingresado, numero_buscado)):
        print("Te pasaste! El numero buscado es mas chico.");
        continue;

    if(Utilidades.esMenor(num_ingresado, numero_buscado)):
        print("Te quedaste corto! El numero buscado es mas grande");
        continue;

    if(Utilidades.sonIguales(num_ingresado, numero_buscado)):
        print("Felicidades! Encontraste el numero secreto.")
        continuar = False;


