import os, random

os.system('cls')
precioProducto = random.randint(10, 100);
precioAbonado = random.randint(10, 100);

print(f"El precio del producto es: ${precioProducto}\nEl precio abonado es: ${precioAbonado}");

if(precioAbonado < precioProducto):
    print("Error. Falta dinero para poder adquirir este producto.");
else:
    print(f"Producto abonado. Su vuelto es {precioProducto - precioAbonado}")
