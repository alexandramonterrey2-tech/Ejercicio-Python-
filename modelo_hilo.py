class Hilo:
    def busca_novedades(self, dato_busqueda):
        print("Buscando novedades relacionadas con: " + dato_busqueda)
        print("Búsqueda realizada con éxito")
        return dato_busqueda

    def procesar_novedad(self, novedad):
        print("Procesando novedad desde Hilo...")
        return novedad


if __name__ == "__main__":
    hilo = Hilo()
    dato_busqueda = input("Ingrese el dato de búsqueda de novedades: ")
    hilo.busca_novedades(dato_busqueda)
    novedad = input("Ingrese la novedad para procesar: ")
    hilo.procesar_novedad(novedad)