
class Procesador:
    def mandar_datos_venta(self, venta):
        print("Los datos de la venta son: " + venta)
        return venta

    def mandar_articulo_online(self, articulo):
        print("El artículo a comprar es: " + articulo)
        return articulo

    def envia_sugerencia_administrador(self, sugerencia):
        print("La sugerencia para el administrador es: " + sugerencia)
        return sugerencia

    def modificar_stock(self, stock):
        print("Stock modificado a: " + stock)
        return stock

    def realizar_cobro(self, cobro):
        print("Monto a cobrar: " + cobro)
        return cobro

    def realizar_pago(self, pago):
        print("Monto a pagar: " + pago)
        return pago

    def actualizar_catalogo(self):
        print("Catálogo actualizado")

    def realiza_busqueda(self, dato_busqueda):
        print("Dato buscado: " + dato_busqueda)
        return dato_busqueda


if __name__ == "__main__":
    proc = Procesador()
    articulo = input("Ingrese el nombre del artículo a comprar: ")
    proc.mandar_articulo_online(articulo)

    venta = input("Ingrese los datos de la venta: ")
    proc.mandar_datos_venta(venta)

    sugerencia = input("¿Desea enviar una sugerencia al administrador? (deje vacío si no): ")
    if sugerencia:
        proc.envia_sugerencia_administrador(sugerencia)