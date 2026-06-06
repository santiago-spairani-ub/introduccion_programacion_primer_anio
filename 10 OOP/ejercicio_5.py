class Ventilador:
    
    def __init__(self):
        self.encendido = False;
        self.velocidad = 0;

    def encender(self):
        self.encedido = True;
        self.velocidad = 1;
        print("Ventilador encendido");

    def apagar(self):
        self.encedido = False;
        self.velocidad = 0;
        print("Ventilador apagado, velocidad 0");

    def cambiar_velocidad(self, velocidad: int):

        if(velocidad < 0 or velocidad > 3):
            print('[ERROR] Ingrese un valor valido para la velocidad (1, 2 o 3)');
        elif(velocidad == 0):
            self.velocidad = 0;
            self.encedido = False;
            print("Se apago el ventilador. Velocidad 0.")
        else:
            self.velocidad = velocidad;
            print(f"Se cambio la velocidad del ventilador a {self.velocidad}");


vent = Ventilador();
vent.encender();
vent.cambiar_velocidad(2);
vent.cambiar_velocidad(5);
vent.apagar();
