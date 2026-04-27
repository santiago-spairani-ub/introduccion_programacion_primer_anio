import array;
numeros = array.array('i', range(10));

for i in range(10):
    numeros[i] = i + 1;
    print("Se ingreso el numero: ", numeros[i]);


print("Los numeros en orden inverso son: ");

for i in range(9, -1, -1):
    print(numeros[i]);