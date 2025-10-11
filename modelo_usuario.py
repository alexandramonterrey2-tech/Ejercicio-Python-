
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


if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    n_cuenta = input("Ingrese su número de cuenta: ")
    direccion = input("Ingrese su dirección: ")
    login = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    usuario = Usuario(nombre, apellido, n_cuenta, direccion, login, password)
    usuario.imprimir_info()