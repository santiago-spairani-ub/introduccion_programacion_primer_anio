class Coche:

    def __init__(self, marca, modelo):
        self.marca = marca;
        self.modelo = modelo;
        self.kilometraje = 0;

    def conducir(self, distancia):
        if distancia <= 0:
            print("\n[ERROR] La distancia debe ser un numero positivo.");
            return;

        self.kilometraje += distancia;
        print("\n[EXITO] Se registraron los kilometros realizados.");
    
    def mostrar_info(self):
        print(f"\n[INFORMACION DEL COCHE]\n\n\tMarca: {self.marca}.\n\tModelo: {self.modelo}.\n\tKilometraje: {self.kilometraje} kms.\n");


coche1 = Coche("Toyota", "Etios");
coche1.mostrar_info();

coche1.conducir(1000);
coche1.conducir(-3);

coche1.mostrar_info();