class Recolector:
        def actualiza_almacen(self):
                print("Envía novedades al almacén")

        def envia_novedades(self, dato_busqueda):
                print("Resultado de la búsqueda: " + dato_busqueda)
                print("Búsqueda realizada con éxito")
                return dato_busqueda

        def procesar_novedad(self, novedad):
                proc = Procesador()
                print("Procesando novedad...")
                proc.mandar_datos_venta(novedad)


if __name__ == "__main__":
        recolector = Recolector()
        recolector.actualiza_almacen()
        dato_busqueda = input("Ingrese el dato de búsqueda de novedades: ")
        recolector.envia_novedades(dato_busqueda)
        novedad = input("Ingrese la novedad para procesar: ")
        recolector.procesar_novedad(novedad)




