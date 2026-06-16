class Carrito:

    def __init__(self):
        self.productos = [];

    def agregar_producto(self, nombre_producto):
        if nombre_producto == "":
            print("[ERROR] Nombre de producto invalido.");
            return;

        self.productos.append(nombre_producto);
        print("[EXITO] Item agregado correctamente.")

    def mostrar_carrito(self):
        print(f"[ITEMS EN EL CARRITO]\n")
        for index, item in enumerate(self.productos):
            print(f"\t{index + 1}. {item}")


cart = Carrito();

cart.agregar_producto("Chicle");
cart.agregar_producto("");
cart.agregar_producto("Gaseosa");

cart.mostrar_carrito();
        