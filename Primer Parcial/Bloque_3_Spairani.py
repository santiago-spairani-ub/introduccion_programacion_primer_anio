import os 
os.system('cls');

# Calcula la comision de un vendedor dado el monto y la categoria.
def calcular_comision(monto, cat):
    match cat:
        case 'A':
            return monto * 0.10
        case 'B':
            return monto * 0.15
        case 'C':
            return monto * 0.20

# Ingreso y validacion de la cantidad de vendedores.
cant_vendedores_valida = False;
while not cant_vendedores_valida:
    try:
        cant_vendedores = int(input("Ingrese el numero de vendedores: "))
        if cant_vendedores > 0:
            cant_vendedores_valida = True
        else:
            print("[ERROR] El numero de vendedores debe ser mayor a 0.")
    except ValueError:
        print("[ERROR] Debes ingresar un numero entero valido.")


cant_vendedores = int(input("Ingrese el numero de vendedores: "))
total_comisiones = 0
max_monto = 0
legajo_max = ""

for i in range(cant_vendedores):
    
    legajo = input(f"\nIngrese el legajo del vendedor {i+1}: ")
    cat = input(f"Ingrese la categoria del vendedor {i+1} (A, B o C): ").upper()
    
    while cat not in ['A', 'B', 'C']:
        cat = input(f"[ERROR] Categoria invalida.\nIngrese la categoria del vendedor {i+1} (A, B o C): ").upper()
    
    monto = float(input(f"Ingrese el monto total de ventas del vendedor {i+1}: "))
    comision = calcular_comision(monto, cat)
    total_comisiones += comision
    
    if monto > max_monto:
        max_monto = monto
        legajo_max = legajo

print(f"\nTotal de comisiones a pagar: ${total_comisiones:.2f}")
print(f"Legajo del vendedor con mayor monto de venta: {legajo_max}")