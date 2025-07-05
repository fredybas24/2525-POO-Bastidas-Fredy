# Clase base: Empleado
class Empleado:
    def __init__(self, nombre, salario):
        # Atributos privados (encapsulación)
        self.__nombre = nombre
        self.__salario = salario

    # Métodos públicos para acceder (get) y modificar (set) los atributos privados
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_salario(self):
        return self.__salario

    def set_salario(self, nuevo_salario):
        # Validación (encapsulación + seguridad)
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("El salario debe ser mayor que 0.")

    # Método que será sobrescrito en las clases hijas (polimorfismo)
    def mostrar_info(self):
        print(f"Empleado: {self.__nombre}, Salario: ${self.__salario}")

# Clase derivada: Gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        # Heredamos atributos de Empleado
        super().__init__(nombre, salario)
        # Atributo propio del Gerente
        self.departamento = departamento

    # Sobrescribimos el método mostrar_info (polimorfismo)
    def mostrar_info(self):
        print(f"Gerente: {self.get_nombre()}, Departamento: {self.departamento}, Salario: ${self.get_salario()}")

# Clase derivada: Desarrollador
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        # Heredamos atributos de Empleado
        super().__init__(nombre, salario)
        # Atributo propio del Desarrollador
        self.lenguaje = lenguaje

    # Sobrescribimos el método mostrar_info (polimorfismo)
    def mostrar_info(self):
        print(f"Desarrollador: {self.get_nombre()}, Lenguaje: {self.lenguaje}, Salario: ${self.get_salario()}")


# Probamos el programa

# Creamos un gerente y un desarrollador
gerente1 = Gerente("Jacinto Mandamás", 5000, "Recursos Humanos")
desarrollador1 = Desarrollador("Alan Codeman", 4000, "Python")

# Mostramos su información (polimorfismo en acción)
gerente1.mostrar_info()
desarrollador1.mostrar_info()

print() # Espacio en blanco

# Probamos encapsulación: cambiar salario con validación
desarrollador1.set_salario(-1000)  # Salario inválido
desarrollador1.set_salario(4500)   # Salario válido
desarrollador1.mostrar_info()      # Muestra el nuevo salario

print() # Espacio en blanco

# Probamos modificar nombre con set
gerente1.set_nombre("Jacinto Jefazo")
gerente1.mostrar_info()