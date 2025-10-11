class Editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def imprimir_info(self):
        print(f"Editorial: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")

    def vender(self, dato_busqueda):
        recolector = Recolector()
        recolector.envia_novedades(dato_busqueda)
        print("Buscando ventas relacionadas con: " + dato_busqueda)
        print("Venta realizada con éxito")
        print("Gracias por su compra")

if __name__ == "__main__":
    nombre = input("Ingrese el nombre de la editorial: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el teléfono: ")
    editorial = Editorial(nombre, direccion, telefono)
    editorial.imprimir_info()
    dato_busqueda = input("Ingrese el dato de búsqueda para ventas: ")
    editorial.vender(dato_busqueda)

        
