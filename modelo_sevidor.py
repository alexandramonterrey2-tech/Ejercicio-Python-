
class Servidor:
    def muestra_pagina(self):
        print("\n[Servidor] Página del servidor fue visualizada...")

    def envia_sugerencia(self, sugerencia):
        print("La sugerencia para el administrador es: " + sugerencia)
        print("Sugerencia enviada con éxito")

    def envia_datosdecompra(self, datos_compra):
        print("Los datos de la compra son: " + datos_compra)
        print("Datos enviados con éxito")

    def envia_datosdeventa(self, datos_venta):
        print("Los datos de la venta son: " + datos_venta)
        print("Datos enviados con éxito")


if __name__ == "__main__":
    servidor = Servidor()
    servidor.muestra_pagina()
    sugerencia = input("Ingrese una sugerencia para el administrador: ")
    servidor.envia_sugerencia(sugerencia)
    datos_compra = input("Ingrese los datos de la compra: ")
    servidor.envia_datosdecompra(datos_compra)
    datos_venta = input("Ingrese los datos de la venta: ")
    servidor.envia_datosdeventa(datos_venta)