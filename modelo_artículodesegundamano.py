from modelo_producto import Producto

class ArticuloSegundaMano(Producto):
    def __init__(self, nombre, precio, autor, editorial, anio_edicion, preferencias, clasificacion, tema, vendedor):
        super().__init__(nombre, precio, autor, editorial, anio_edicion, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor
        self.vendido = False

    def detalles_articulo_segunda_mano(self):
        print(f"Clasificación: {self.clasificacion}, Tema: {self.tema}, Vendedor: {self.vendedor}")

    def mostrar_info(self):
        print(f"Artículo de segunda mano: {self.nombre}")
        print(f"Autor: {self.autor} | Editorial: {self.editorial} | Año: {self.anio_edicion}")
        print(f"Clasificación: {self.clasificacion} | Tema: {self.tema}")
        print(f"Vendedor: {self.vendedor}")
        print(f"Precio: ${self.precio} | Preferencias: {self.preferencias}")
        print(f"Estado: {'VENDIDO' if self.vendido else 'DISPONIBLE'}\n")

    def __str__(self):
        return f"Artículo de Segunda Mano - Clasificación: {self.clasificacion}, Tema: {self.tema}, Vendedor: {self.vendedor}"
