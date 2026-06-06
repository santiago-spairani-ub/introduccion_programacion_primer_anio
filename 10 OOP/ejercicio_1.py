class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre;
        self.edad = edad;

    def Saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} anios");


persona = Persona("Santi", 24)

persona.Saludar();