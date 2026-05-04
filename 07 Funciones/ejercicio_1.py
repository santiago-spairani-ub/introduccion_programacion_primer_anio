import os
os.system('cls');

def temperatura_minima(temperaturas):
    return min(temperaturas)

def temperatura_maxima(temperaturas):
    return max(temperaturas)

def temperatura_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def temperaturas_bajo_cero(temperaturas):
    return sum(1 for temp in temperaturas if temp < 0)

temperaturas = [15, 18, 20, 22, 25, 28, 30, 29, 27, 24, 21, 19, 17, 16, 14, 
                12, 10, 8, 5, 3, 0, -2, -1, 2, 6, 11, 13, 19, 23, 26]

minima = temperatura_minima(temperaturas)
maxima = temperatura_maxima(temperaturas)
promedio = temperatura_promedio(temperaturas)
bajo_cero = temperaturas_bajo_cero(temperaturas)

print("=" * 50)
print("INFORME DE TEMPERATURAS DEL MES")
print("=" * 50)
print(f"Temperatura minima: {minima}°C")
print(f"Temperatura maxima: {maxima}°C")
print(f"Temperatura promedio: {promedio:.2f}°C")
print(f"Dias con temperaturas bajo cero: {bajo_cero}")
print("=" * 50)