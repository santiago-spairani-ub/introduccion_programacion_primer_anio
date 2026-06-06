import math;
class Estudiante:

    def __init__(self, nombre: str, notas: list[int]):
        self.nombre = nombre;
        self.notas = notas;

    def Obtener_promedio(self):
        return sum(self.notas) / len(self.notas);

    def Aprobo(self):
        return self.Obtener_promedio() >= 6;
    
estudiante1 = Estudiante("Santi", [7,6,9]);
estudiante2 = Estudiante("pepe", [4,4,4]);


print(f"El promedio del estudiante 1 es: {estudiante1.Obtener_promedio()}. APROBO: {estudiante1.Aprobo()}")
print(f"El promedio del estudiante 2 es: {estudiante2.Obtener_promedio()}. APROBO: {estudiante2.Aprobo()}")





