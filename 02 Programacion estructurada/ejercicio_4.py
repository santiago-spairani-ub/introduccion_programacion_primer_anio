import os

os.system('cls');

valor_producto = float(input("Ingrese el valor del articulo: "));
valor_descuento_20 = valor_producto * 0.80
IVA = 1.21
print(f"El valor del producto con 20% de descuento es: {valor_descuento_20}")
print(f"El precio final del articulo +IVA es: {valor_descuento_20 * IVA}")