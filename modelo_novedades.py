from modelo_producto import Producto

class Novedad(Producto):
    def __init__(self, nombre, precio, autor, editorial, anio_edicion, preferencias, clasificacion, tema):
        super().__init__(nombre, precio, autor, editorial, anio_edicion, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self, nueva):
        self.clasificacion = nueva


if __name__ == "__main__":
    nombre = input("Ingrese el nombre de la novedad: ")
    precio = input("Ingrese el precio: ")
    autor = input("Ingrese el autor: ")
    editorial = input("Ingrese la editorial: ")
    anio_edicion = input("Ingrese el año de edición: ")
    preferencias = input("Ingrese las preferencias (separadas por coma): ").split(",")
    clasificacion = input("Ingrese la clasificación: ")
    tema = input("Ingrese el tema: ")

    novedad = Novedad(nombre, precio, autor, editorial, anio_edicion, preferencias, clasificacion, tema)
    print(f"Novedad: {novedad.nombre}, Clasificación: {novedad.clasificacion}, Tema: {novedad.tema}")