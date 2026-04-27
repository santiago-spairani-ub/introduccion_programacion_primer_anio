import os, random

os.system('cls')

clientesTipo = [0] * 10;
clientesLimiteActual = [0.0] * 10;

print("Clientes actuales: \n");
for i in range(len(clientesTipo)):
    clientesTipo[i] = random.randint(1, 7);
    clientesLimiteActual[i] = random.uniform(1000, 10000)
    print(f"\t{i + 1}. Cliente tipo: {clientesTipo[i]}. Limite actual: {clientesLimiteActual[i]}");

print("\n\n")

print("Segun los tipos de cliente, los limites quedarian: \n\n")
for i in range(len(clientesTipo)):
    
    tipoClienteActual = clientesTipo[i];
    limiteActual = clientesLimiteActual[i];

    match tipoClienteActual:
        case 1:
            clientesLimiteActual[i] = limiteActual * 1.25
        case 2: 
            clientesLimiteActual[i] = limiteActual * 1.35
        case 3:
            clientesLimiteActual[i] = limiteActual * 1.40
        case _:
            clientesLimiteActual[i] = limiteActual * 1.50

    print(f"\t{i + 1}. Cliente tipo: {tipoClienteActual}. Nuevo limite: {clientesLimiteActual[i]}");

