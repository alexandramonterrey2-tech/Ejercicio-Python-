from modelo_producto import Producto

class Libro(Producto):
    def __init__(self, nombre, precio, autor, editorial, anio_edicion, preferencias, genero):
        super().__init__(nombre, precio, autor, editorial, anio_edicion, preferencias)
        self.genero = genero

    def detalles_libro(self):
        print(f"Género: {self.genero}")

    def mostrar_info(self):
        print(f"Libro: {self.nombre}")
        print(f"Autor: {self.autor} | Editorial: {self.editorial} | Año: {self.anio_edicion}")
        print(f"Género: {self.genero}")
        print(f"Precio: {self.precio} | Preferencias: {self.preferencias}\n")