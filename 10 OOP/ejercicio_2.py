class Rectangulo:

    def __init__(self, base, altura):
        self.base = base;
        self.altura = altura;

    def Calcular_area(self):
        return self.base * self.altura;

    def Calcular_perimetro(self):
        return (self.base * 2) + (self.altura * 2);

rect = Rectangulo(5, 2);

print(f"Se genero un rectangulo con area: {rect.Calcular_area()} y perimetro: {rect.Calcular_perimetro()}")