class Celular:

    def __init__(self, marca, modelo, bateria: int):
        self.marca = marca;
        self.modelo = modelo;

        if bateria < 0 or bateria > 100:
            print(f"[ERROR] Se ingreso un numero invalido para la bateria. Se seteo a 0 por defecto.");
            self.bateria = 0;
        else:
            self.bateria = bateria;

    def hacer_llamada(self, minutos: int):
        bateria_restante = self.bateria - minutos;
        if(bateria_restante < 0):
            print(f"El celular modelo: {self.modelo}, marca: {self.marca}. Se quedo sin bateria. 0%")
            self.bateria = 0;
            return;

        self.bateria -= minutos;
        print(f"Modelo: {self.modelo}, Marca: {self.marca}. Bateria restante: {self.bateria}%");

    def cargar(self):
        self.bateria = 100;
        print(f"Modelo: {self.modelo}, Marca: {self.marca}. Cargado al maximo. 100%")


cel = Celular("Samsung", "S22", 20)
cel.hacer_llamada(11);
cel.cargar();
cel.hacer_llamada(110);