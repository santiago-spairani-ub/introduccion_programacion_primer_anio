meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    try:
        numero = int(input("Ingresa un numero entre 1 y 12: "))
        
        if 1 <= numero <= 12:
            print(f"El mes corresponde a: {meses[numero - 1]}")
            break
        else:
            print("Error: El numero debe estar entre 1 y 12.")
    except ValueError:
        print("Error: Debes ingresar un numero entero valido.")