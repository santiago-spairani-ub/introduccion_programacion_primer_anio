import os, random, Validaciones

os.system("cls");


cant_nums_esperados = int(input("Ingrese la cantidad de numeros a cargar: "));
cant_nums_ingresados = 0;
lista_nums = [];

# Primer metodo
while cant_nums_ingresados != cant_nums_esperados:

    num_generado = random.randint(0, 100);

    if Validaciones.elementoRepetido(lista_nums, num_generado):
        continue;
    else:
        lista_nums.append(num_generado);
        cant_nums_ingresados+=1;

# Segundo metodo
while cant_nums_ingresados != cant_nums_esperados:

    for i in range(0, cant_nums_esperados):
        num_generado = random.randint(0, 100);
        lista_nums.append(num_generado);

    Validaciones.limpiarElementosRepetidos(lista_nums);

    cant_nums_ingresados = len(lista_nums);

