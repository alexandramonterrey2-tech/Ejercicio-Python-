class Articulo_online(Producto):
    def __init__(self, nombre, precio, autor, editorial, anio_edicion, preferencias, tema):
        super().__init__(nombre, precio, autor, editorial, anio_edicion, preferencias)
        self.tema = tema

    def publicar(self):
        print(f"El artículo online '{self.nombre}' ha sido publicado.")


if __name__ == "__main__":
    nombre = input("Ingrese el nombre del artículo online: ")
    precio = input("Ingrese el precio: ")
    autor = input("Ingrese el autor: ")
    editorial = input("Ingrese la editorial: ")
    anio_edicion = input("Ingrese el año de edición: ")
    preferencias = input("Ingrese las preferencias (separadas por coma): ").split(",")
    tema = input("Ingrese el tema: ")

    articulo = Articulo_online(nombre, precio, autor, editorial, anio_edicion, preferencias, tema)

    articulo.publicar()
