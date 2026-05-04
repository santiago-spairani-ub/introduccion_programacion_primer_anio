import os

os.system('cls')

def es_alfabetica(palabra):
    palabra = palabra.lower()
    
    for i in range(len(palabra) - 1):
        if palabra[i] > palabra[i + 1]:
            return False
    
    return True


palabra = input("Ingrese una palabra: ").strip()

if es_alfabetica(palabra):
    print(f"'{palabra}' es una palabra alfabética.")
else:
    print(f"'{palabra}' no es una palabra alfabética.")