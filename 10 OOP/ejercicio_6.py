class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo;
        self.autor = autor;
        self.prestado = False;

    def prestar(self):
        self.prestado = True;
        print(f"El libro {self.titulo} fue prestado");

    def devolver(self):
        self.prestado = False;
        print(f"El libro {self.titulo} fue devuelto");

    def estado_actual(self):
        if(self.prestado):
            print(f"El libro: {self.titulo} se encuentra PRESTADO");
        else:
            print(f"El libro: {self.titulo} se encuentra en ALMACEN");
        

libro = Libro("libro epico", "autor epico");
libro.prestar()
libro.devolver();
libro.estado_actual();
