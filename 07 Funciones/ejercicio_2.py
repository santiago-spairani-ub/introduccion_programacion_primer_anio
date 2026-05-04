import os
os.system('cls');

def esPanvocalica(palabra):
    palabra = palabra.lower()
    vocales = {'a', 'e', 'i', 'o', 'u'}
    encontradas = set()
    
    for letra in palabra:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            encontradas.add(letra)
    
    return encontradas == vocales


print(esPanvocalica("centrifugado"))  # True
print(esPanvocalica("bisabuelo"))     # True
print(esPanvocalica("hipotenusa"))    # True
print(esPanvocalica("hola"))          # False