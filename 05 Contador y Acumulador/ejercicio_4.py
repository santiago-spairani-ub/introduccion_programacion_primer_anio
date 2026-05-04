import os
os.system('cls');

def calcular_factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


while True:
    try:
        numero = int(input("Ingrese un numero entero: "))
        
        if numero < 0:
            print("Error: El numero debe ser mayor o igual a 0")
            continue
        
        resultado = calcular_factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
        break
        
    except ValueError:
        print("Error: Ingrese un numero entero valido")