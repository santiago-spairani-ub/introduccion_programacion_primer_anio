import os
os.system('cls');

def formato_miles(numero_str):
    # Invertir la cadena para procesar de derecha a izquierda
    invertida = numero_str[::-1]
    
    # Agrupar de 3 en 3 e insertar puntos
    grupos = [invertida[i:i+3] for i in range(0, len(invertida), 3)]
    
    resultado = '.'.join(grupos)[::-1]
    
    return resultado


print(formato_miles('1234567890'))  # 1.234.567.890
print(formato_miles('1234'))        # 1.234
print(formato_miles('123'))         # 123