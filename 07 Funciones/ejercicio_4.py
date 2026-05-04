import os
os.system('cls');

def mayusculas_vocales(texto):
    vocales = "aeiouáéíóú"
    resultado = ""
    for caracter in texto:
        if caracter.lower() in vocales:
            resultado += caracter.upper()
        else:
            resultado += caracter
    return resultado

texto_ingresado = input("Ingrese el texto: ")
texto_procesado = mayusculas_vocales(texto_ingresado)
print(texto_procesado)