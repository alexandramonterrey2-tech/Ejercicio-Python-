

class Revista(Producto):
    def __init__(self, nombre, precio, autor, editorial, anio_edicion, preferencias, categoria):
        super().__init__(nombre, precio, autor, editorial, anio_edicion, preferencias)
        self.categoria = categoria

    def detalles_revista(self):
        print(f"Categoría: {self.categoria}")   
    def mostrar_info(self):
        print(f"Revista: {self.nombre}")
        print(f"Autor: {self.autor} | Editorial: {self.editorial} | Año: {self.anio_edicion}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: {self.precio} | Preferencias: {self.preferencias}\n")
    def __str__(self):
        return f"Revista - Categoría: {self.categoria}"
        
    from modelo_producto import Producto
    nombre = input("Ingrese el nombre de la revista: ")
    precio = input("Ingrese el precio: ")
    autor = input("Ingrese el autor: ")
    editorial = input("Ingrese la editorial: ")
    anio_edicion = input("Ingrese el año de edición: ")
    preferencias = input("Ingrese las preferencias (separadas por coma): ").split(",")
    categoria = input("Ingrese la categoría: ")

    revista = Revista(nombre, precio, autor, editorial, anio_edicion, preferencias, categoria)
    revista.mostrar_info()
        
