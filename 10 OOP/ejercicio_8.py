class Calculadora:

    def __init__(self):
        pass

    def sumar(self, a, b):
        return a + b;

    def restar(self, a, b):
        return a - b;

    def multiplicar(self, a, b):
        return a * b;

    def dividir(self, a, b):
        #si se intenta dividir por cero, devuelvo cero para simplificar
        if b == 0:
            return 0
        
        return a / b;


calc = Calculadora();
print(f"suma de 1 y 2: {calc.sumar(1, 2)}");
print(f"resta entre 5 y 3: {calc.restar(5, 3)}");
print(f"multi entre 2 y 3: {calc.multiplicar(2, 3)}");
print(f"dividir entre 10 y 5: {calc.dividir(10, 5)}")