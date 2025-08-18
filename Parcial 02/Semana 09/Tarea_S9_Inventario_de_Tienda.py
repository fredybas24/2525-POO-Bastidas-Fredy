# =================================================
# Sistema de Gestión de Inventario: Videoclub Retro
# =================================================

# Clase Producto: Representa una película en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos privados (convención con "_") para aplicar encapsulamiento
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters (obtener atributos)
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters (modificar atributos)
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio

    # Método para mostrar los datos del producto como string
    def __str__(self):
        return f"ID: {self._id} |Película: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio}"


class Inventario:
    def __init__(self):
        # La lista contendrá objetos de tipo producto
        self.productos = []

    # Añadir producto (solo si el ID es único)
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado corretamente.")
                return
        print("Producto no encontrado.")

    # Actualizar cantidad o precio de un producto
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    # Buscar producto por nombre
    def buscar_producto(self, nombre):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        if resultados:
            print("Resultados de búsqueda:")
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos en inventario
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario del Videoclub Retro:")
            for p in self.productos:
                print(p)


# Menú interactivo en consola

def menu():
    inventario = Inventario()

    while True:
        print("\n==== Videoclub Retro - Menu principal ====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleciona una opción: ")

        if opcion == "1":
            # Añadir producto
            id_producto = input("Ingrese el ID de la película: ")
            nombre = input("Ingrese el nombre de la película: ")
            cantidad = int(input("Ingrese la catidad de copias: "))
            precio = float(input("Ingrese el precio unitario: "))

            nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(nuevo_producto)
        elif opcion == "2":
            # Eliminar producto
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Actualizar producto
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            print("Deje en blanco si no desea modificar un campo.")
            nueva_cantidad = input("Nueva cantidad: ")
            nuevo_precio = input("Nuevo precio: ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            # Buscar producto
            nombre = input("Ingrese el nombre o parte del nombre: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            # Mostrar inventario
            inventario.mostrar_productos()
        elif opcion == "6":
            # Salir
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo")

# Ejecutar programa
menu()