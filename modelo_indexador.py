
class Indexador:
    def actualiza_almacen(self):
        print("Almacén actualizado")

    def envia_resultado_busqueda(self, dato_busqueda):
        print("Resultado de la búsqueda: " + dato_busqueda)
        print("Búsqueda realizada con éxito")


if __name__ == "__main__":
    indexador = Indexador()
    indexador.actualiza_almacen()
    dato_busqueda = input("Ingrese el dato de búsqueda: ")
    indexador.envia_resultado_busqueda(dato_busqueda)
