from models.Personaje import Personaje
from models.Arma import Arma
import funcionalidades, os, random

os.system('cls')

salud = funcionalidades.user_input_for_float("Ingrese la salud del personaje: ")
if salud <= 0:
    salud = 100;
    print("[ERROR] La salud no puede ser 0 o menor. Se seteo 100 por defecto.")

hacha = Arma("Hacha pesada", 10, 12);
espada = Arma("Espada larga", 9, 11);

heroe = Personaje("Heroe", salud, espada);
enemigo = Personaje("Monstruo", 100, hacha);

turnos = 0

os.system('cls')
while heroe.obtener_salud() > 0 and enemigo.obtener_salud() > 0:
    turnos += 1;
    print(f"\nTURNO: {turnos}");
    print(heroe);
    print(enemigo);

    print("\n[ACCIONES]\n")
    if turnos % 2 == 0:
        opcion = funcionalidades.elegir_opcion_usuario();
        if opcion == 1:
            heroe.atacar(enemigo);
        else:
            heroe += random.randint(15, 20);
    else:
        enemigo.atacar(heroe);

    input("\nPresione [ENTER] para continuar...");

if heroe.obtener_salud() > 0:
    print(f"[GANASTE] en {turnos} turnos");
else:
    print(f"[PERDISTE] en {turnos} turnos");


