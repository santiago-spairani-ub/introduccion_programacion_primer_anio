import random
class Arma:

    def __init__(self, nombre, danio_minimo, danio_maximo):
        self._nombre = nombre;
        self._danio_minimo = danio_minimo;
        self._danio_maximo = danio_maximo;

    #override del metodo str para mostrar el nombre y el rango de daño del arma
    def __str__(self):
        return f"{self._nombre} ({self._danio_minimo}-{self._danio_maximo})";

    def calcular_danio(self):
        return random.randint(self._danio_minimo, self._danio_maximo);

