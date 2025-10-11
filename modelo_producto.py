

class Producto:
    def __init__(self, precio, titulo, autor, editorial, ano_de_edicion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ano_de_edicion = ano_de_edicion
        self.preferencias = preferencias

    def imprimir_info(self):
        print(f"Producto: {self.titulo} por {self.autor}")
        print(f"Precio: ${self.precio}, Editorial: {self.editorial}, Año de Edición: {self.ano_de_edicion}")
        print(f"Preferencias: {', '.join(self.preferencias)}")

    def vender(self, vender):
        print("El producto se venderá: " + vender)
        return vender

    def comprar(self, comprar):
        print("El producto costará: " + comprar)
        return comprar

    def ver_catalogo(self, catalogo):
        print("El catálogo es: " + catalogo)
        return catalogo


if __name__ == "__main__":
    precio = input("Ingrese el precio del producto: ")
    titulo = input("Ingrese el título del producto: ")
    autor = input("Ingrese el autor del producto: ")
    editorial = input("Ingrese la editorial del producto: ")
    ano_de_edicion = input("Ingrese el año de edición del producto: ")
    preferencias = input("Ingrese las preferencias del producto (separadas por coma): ").split(",")

    producto = Producto(precio, titulo, autor, editorial, ano_de_edicion, preferencias)
    producto.imprimir_info()

    vender = input("¿El producto se venderá por?: ")
    producto.vender(vender)

    comprar = input("¿El producto se comprará por?: ")
    producto.comprar(comprar)

    catalogo = input("¿Desea ver el catálogo? (si/no): ")
    if catalogo.lower() == "si":
        producto.ver_catalogo("Catálogo de productos")