class Usuario:
    def __init__(self, nombre, apellido, n_cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.n_cuenta = n_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password 

    def imprimir_info(self):
        print(f"Usuario: {self.nombre} {self.apellido}")
        print(f"Cuenta: {self.n_cuenta}")
        print(f"Dirección: {self.direccion}")
        print(f"Login: {self.login}")


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


class Servidor:
    def pagina(self):
        print("\n[Servidor] Página del servidor fue visualizada...")

        obj_proc = Procesador()
        obj_proc.realiza_busqueda("libros ciencia ficción")


class Producto:
    def __init__(self, precio,titulo,autor,editorial,ano_de_edicion,preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ano_de_edicion = ano_de_edicion
        self.preferencias = preferencias     
    
    def imrpimir_info(self):
        print(f"Producto: {self.titulo} por {self.autor}")
        print(f"Precio:{self.precio}, Editorial: {self.editorial}, Año de Edición: {self.anio_de_edicion}")
        print(f"Preferencias: {(self.preferencias)}")
        
    def vender(self, vender):
            print("El producto se vendera: " + vender)
            return vender
    def comprar(self, comprar):
            print("El producto costara: " + comprar)
            return comprar
    def ver_catalogo(self, catalogo):
            print("El catalogo es: " + catalogo)
            return catalogo
                    
class Articulos:
    def articulos(self, tipo):
        match tipo:
            case "libro":
                genero=input("Ingrese el género del libro (aventura, ciencia ficción, fantasía, terror, romance): ")
                print("El artículo a comprar será un libro del género: " + genero)

            case "revista":
                print("El artículo a comprar será una revista")
                categoria=input("Ingrese la categoría de la revista (moda, tecnología, deportes, salud, entretenimiento): ")
                print("la categoria de la revista es: " + categoria)
            case "articulo":
                print("El artículo a comprar será un artículo de segunda mano")
                clasifiacion=input("ingrese el estado del articulo (como nuevo,bueno,aceptable):")
                tema=input("ingrese el tema del articulo (libro,revista,comic):")
                vendedor=input("ingrese el nombre del vendedor:")
                print("la clasificacion del articulo es: " + clasifiacion + ", el tema del articulo es: " + tema + ", el nombre del vendedor es: " + vendedor)
            case "novedad":
                print("El artículo a comprar será una novedad")
                clasifiacion=input("ingrese el estado del articulo (como nuevo,bueno,aceptable):")
                tema=input("ingrese el tema del articulo (libro,revista,comic):")
                print("la clasificacion del articulo es: " + clasifiacion + ", el tema del articulo es: " + tema)
            case "online":
                print("El artículo a comprar será un artículo online")
                tema=input("ingrese el tema del articulo (libro,revista,comic):")
                print("el tema del articulo es: " + tema)
            case _:
                print("El artículo a comprar será otro tipo de artículo")


class Indexador:
    def actualiza_almacen(self):
        print("Almacén actualizado")

    def envia_resultado_busqueda(self, dato_busqueda):
        print("Resultado de la búsqueda: " + dato_busqueda)
        print("Búsqueda realizada con éxito")

# Simulación de la plataforma
print("Simulación de una plataforma de compra-venta de productos\n")

# Registro de usuario

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
n_cuenta = input("Ingrese su número de cuenta: ")
direccion = input("Ingrese su dirección: ")
login = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")

obj_usuario = Usuario(nombre, apellido, n_cuenta, direccion, login, password)
obj_usuario.imprimir_info()

obj_servidor = Servidor()
obj_servidor.pagina()

# Procesamiento de datos
obj_proc = Procesador()
articulo = input("\nIngrese el nombre del artículo a comprar: ")
obj_proc.mandar_articulo_online(articulo)

venta = input("Ingrese los datos de la venta: ")
obj_proc.mandar_datos_venta(venta)

sugerencia = input("¿Desea enviar una sugerencia al administrador? (deje vacío si no): ")
if sugerencia:
    obj_proc.envia_sugerencia_administrador(sugerencia)
    
#acciones de producto
precio = input("\nIngrese el precio del producto: ")
titulo = input("Ingrese el título del producto: ")   
autor = input("Ingrese el autor del producto: ")
editorial = input("Ingrese la editorial del producto: ")
ano_de_edicion = input("Ingrese el año de edición del producto: ")
preferencias = input("Ingrese las preferencias del producto: ")

obj_producto = Producto(precio, titulo, autor, editorial, ano_de_edicion, preferencias.split(","))
vender = input("¿El producto se vendera por?: ")
obj_producto.vender(vender)

comprar = input("¿El producto se comprara por?: ")
obj_producto.comprar(comprar)

catalogo = input("¿Desea ver el catálogo? (si/no): ")
if catalogo == "si":
    obj_producto.ver_catalogo("Catálogo de productos")

# acciones de articulos
obj_articulos = Articulos()
tipo = input("Ingrese el tipo de artículo (libro,revista,articulo,novedades,online): ")
obj_articulos.articulos(tipo)
# Acciones del indexador
obj_indexador = Indexador()
obj_indexador.actualiza_almacen()
obj_indexador.envia_resultado_busqueda("artículos relacionados a tu compra")


class Hilo:
    def busca_novedades(self, dato_busqueda):
        print("Buscando novedades relacionadas con: " + dato_busqueda)
        print("Búsqueda realizada con éxito")
        return dato_busqueda

    def procesar_novedad(self, novedad):
        print("Procesando novedad ...")
        return novedad


class Recolector:
    def actualiza_almacen(self):
        print("Envía novedades al almacén")

    def envia_novedades(self, dato_busqueda):
        print("Resultado de la búsqueda: " + dato_busqueda)
        print("Búsqueda realizada con éxito")
        return dato_busqueda

    def procesar_novedad(self, novedad):
        print("Procesando novedad...")
        return novedad


if __name__ == "__main__":
    hilo = Hilo()
    dato_busqueda = input("\nIngrese el dato de búsqueda de novedades: ")
    hilo.busca_novedades(dato_busqueda)
    novedad = input("Ingrese la novedad para procesar: ")
    hilo.procesar_novedad(novedad)

    # Ejemplo de uso de Recolector
    recolector = Recolector()
    recolector.actualiza_almacen()
    recolector.envia_novedades(dato_busqueda)
    recolector.procesar_novedad(novedad)

    # Ejemplo de uso de Editorial
    nombre_editorial = input("\nIngrese el nombre de la editorial: ")
    direccion_editorial = input("Ingrese la dirección de la editorial: ")
    telefono_editorial = input("Ingrese el teléfono de la editorial: ")
    editorial = Editorial(nombre_editorial, direccion_editorial, telefono_editorial)
    editorial.imprimir_info()
    dato_busqueda_editorial = input("Ingrese el dato de búsqueda para ventas de la editorial: ")
    editorial.vender(dato_busqueda_editorial)

    print("\n Fin de la simulación ")

class Recolector:
        def actualiza_almacen(self):
                print("Envía novedades al almacén")

        def envia_novedades(self, dato_busqueda):
                print("Resultado de la búsqueda: " + dato_busqueda)
                print("Búsqueda realizada con éxito")
                return dato_busqueda

        def procesar_novedad(self, novedad):
                print("Procesando novedad...")
                return novedad  
        

# Ejemplo de uso de Editorial
nombre_editorial = input("\nIngrese el nombre de la editorial: ")
direccion_editorial = input("Ingrese la dirección de la editorial: ")
telefono_editorial = input("Ingrese el teléfono de la editorial: ")
editorial = Editorial(nombre_editorial, direccion_editorial, telefono_editorial)
editorial.imprimir_info()
dato_busqueda_editorial = input("Ingrese el dato de búsqueda para ventas de la editorial: ")
editorial.vender(dato_busqueda_editorial)

print("\n Fin de la simulación ")