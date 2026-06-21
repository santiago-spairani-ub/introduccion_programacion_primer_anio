import random
from models.Arma import Arma
class Personaje:

    def __init__(self, nombre: str, salud: float, arma: Arma):
        self.nombre = nombre;
        self._salud = salud;
        self._salud_maxima = salud
        self._arma_equipada = arma;

    def obtener_salud(self) -> int:
        return round(self._salud, 2);

    def __str__(self):
        return f"Nombre: {self.nombre}. Salud: {round(self._salud, 2)}. Ataque: {self._arma_equipada}";

    def __add__(self, cantidad_curacion: float):
        if (self._salud + cantidad_curacion) >= self._salud_maxima:
            self._salud = self._salud_maxima;
        else:
            self._salud += cantidad_curacion

        print(f"Pocion bebida. Vida actual de {self.nombre}: {self.obtener_salud()}")
        return self;

    def recibir_danio(self, cantidad: float):
        if (self._salud - cantidad) <= 0:
            self._salud = 0;
        else:
            self._salud -= round(cantidad, 2);
    
        print(f"La salud de {self.nombre} es de {self._salud}")

    def atacar(self, enemigo: Personaje):
        damage = self._arma_equipada.calcular_danio();
        print(f"{self.nombre} ataca a {enemigo.nombre} con {damage} de danio");

        enemigo.recibir_danio(damage);


