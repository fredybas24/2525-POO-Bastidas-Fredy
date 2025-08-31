import json

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

    # Convertir a diccionario para JSON
    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    # Crear Producto desde diccionario
    @staticmethod
    def from_dict(d):
        return Producto(d["id"], d["nombre"], d["cantidad"], d["precio"])

# Clase Inventario
class Inventario:
    def __init__(self):
        # Diccionario {id_producto: producto} para almacenar los productos
        self.productos = {}

    # Añadir producto (solo si el ID es único)
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El ID ya existe. No se agregó el producto")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado correctamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # Actualizar cantidad o precio de un producto
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    # Buscar producto por nombre
    def buscar_producto(self, nombre):
        resultados = []
        for p in self.productos.values():
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
            print("\nInventario del Videoclub Retro:")
            for p in self.productos.values():
                print(p)

    # Guardar en archivo de texto (JSON)
    def guardar_en_archivo(self, nombre_archivo="inventario.txt"):
        try:
            data = {}  # diccionario vacío
            for id_p, p in self.productos.items():
                data[id_p] = p.to_dict()
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                json.dump(data, archivo, indent=4) # indent para legibilidad
            print("Inventario guardado correctamente en texto.")
        except Exception as e:
            print(f"Error al guardar: {e}")

    # Cargar desde archivo de texto (JSON)
    def cargar_desde_archivo(self, nombre_archivo="inventario.txt"):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
                self.productos = {}
                for id_p, d in data.items():
                    producto = Producto.from_dict(d)  # reconstruye el objeto Producto
                    self.productos[id_p] = producto
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("No existe archivo de inventario. Se creará uno al guardar.")
        except Exception as e:
            print(f"Error al cargar: {e}")


# Menú interactivo

def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\n==== Videoclub Retro - Menu principal ====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario (manualmente)")
        print("7. Salir")

        opcion = input("Seleciona una opción: ").strip()

        if opcion == "1":
            # Añadir producto
            id_producto = input("Ingrese el ID de la película: ").strip()
            nombre = input("Ingrese el nombre de la película: ").strip()
            try:
                cantidad = int(input("Ingrese la catidad de copias: ").strip())
                precio = float(input("Ingrese el precio unitario: ").strip())
                if cantidad < 0 or precio < 0:
                    print("Error: Cantidad y precio deben ser positivos.")
                    continue
                inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            except ValueError:
                print("Error: Cantidad y precio deben ser números.")

        elif opcion == "2":
            # Eliminar producto
            id_producto = input("Ingrese el ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Actualizar producto
            id_producto = input("Ingrese el ID del producto a actualizar: ").strip()
            print("--Deje en blanco si no desea modificar un campo.--")
            nueva_cantidad = input("Nueva cantidad: ").strip()
            nuevo_precio = input("Nuevo precio: ").strip()
            try:
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None
                if nueva_cantidad < 0 or nuevo_precio < 0:
                    print("Error: Cantidad y precio deben ser positivos.")
                    continue
                if nuevo_precio is not None and nuevo_precio <= 0:
                    print("Error: El precio debe ser mayor que cero.")
                    continue
                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("Error: Cantidad y precio deben ser números.")

        elif opcion == "4":
            # Buscar producto
            nombre = input("Ingrese el nombre o parte del nombre: ").strip()
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            # Mostrar inventario
            inventario.mostrar_productos()

        elif opcion == "6":
            # Guardar inventario
            inventario.guardar_en_archivo()

        elif opcion == "7":
            # Salir
            inventario.guardar_en_archivo()
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo")

# Ejecutar programa
menu()