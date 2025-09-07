# =========================================
# Sistema de gestión de biblioteca digital
# =========================================

# -------------------
# Clase Libro
# -------------------
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Guardamos título y autor en una tupla porque son inmutables
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria  # Género o tipo de libro
        self.isbn = isbn  # Identificador único del libro (clave en la biblioteca)

    def __str__(self):
        # Representación en texto del libro (para imprimirlo)
        return f"Titulo: {self.titulo_autor[0]} | Autor: {self.titulo_autor[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"


# -------------------
# Clase Usuario
# -------------------
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados a este usuario

    def __str__(self):
        # Representación en texto del usuario
        return f"Nombre: {self.nombre} | ID: {self.id_usuario} | Libros prestados: {[libro.titulo_autor[0] for libro in self.libros_prestados]}"


# -------------------
# Clase Biblioteca
# -------------------
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario {ISBN: Libro}
        self.usuarios_registrados = {}  # Diccionario {ID_usuario: Usuario}
        self.prestamos = {}  # Diccionario {ID_usuario: [lista de libros prestados]}

    # ---- Gestión de libros ----
    def añadir_libro(self, libro):
        # Añadir libro a la colección de la biblioteca
        if libro.isbn in self.libros_disponibles:
            print("El libro ya existe en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print("Libro añadido correctamente.")

    def quitar_libro(self, isbn):
        # Quitar libro de la colección (si existe)
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print("Libro eliminado de la biblioteca.")
        else:
            print("El libro no existe.")

    # ---- Gestión de usuarios ----
    def registrar_usuario(self, usuario):
        # Registrar un nuevo usuario
        if usuario.id_usuario in self.usuarios_registrados:
            print("El usuario ya está registrado.")
        else:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            self.prestamos[usuario.id_usuario] = []
            print("Usuario registrado correctamente.")

    def dar_debaja_usuario(self, id_usuario):
        # Eliminar un usuario de la biblioteca
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            del self.prestamos[id_usuario]
            print("Usuario eliminado correctamente.")
        else:
            print("El usuario no existe.")

    # ---- Gestión de préstamos ----
    def prestar_libro(self, id_usuario, isbn):
        # Prestar libro a un usuario (si existe y está disponible)
        if id_usuario not in self.usuarios_registrados:
            print("No se puede prestar el libro: el usuario no está registrado.")
        elif isbn not in self.libros_disponibles:
            print("No se puede prestar el libro: el libro no está disponible en la biblioteca.")
        else:
            libro = self.libros_disponibles[isbn]
            self.prestamos[id_usuario].append(libro)
            self.usuarios_registrados[id_usuario].libros_prestados.append(libro)
            del self.libros_disponibles[isbn]  # Se quita de los disponibles
            print(f"Libro '{libro.titulo_autor[0]}' prestado a {self.usuarios_registrados[id_usuario].nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        # Devolver libro (si el usuario y el préstamo existen)
        if id_usuario not in self.usuarios_registrados:
            print("No se puede devolver el libro: el usuario no está registrado.")
            return
        if id_usuario not in self.prestamos or not self.prestamos[id_usuario]:
            print("No se puede devolver el libro: el usuario no tiene préstamos registrados.")
            return

        for libro in self.prestamos[id_usuario]:
            if libro.isbn == isbn:
                self.prestamos[id_usuario].remove(libro)
                self.usuarios_registrados[id_usuario].libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro '{libro.titulo_autor[0]}' devuelto por {self.usuarios_registrados[id_usuario].nombre}")
                return

        print("No se puede devolver el libro: el usuario no tenía prestado este libro.")

    # ---- Búsqueda de libros ----
    def buscar_libro(self, criterio, valor):
        # Buscar libros por título, autor o categoría
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.titulo_autor[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.titulo_autor[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        if resultados:
            print("🔍 Resultados de búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron coincidencias.")

    # ---- Listar préstamos ----
    def listar_prestamos(self, id_usuario):
        # Mostrar todos los libros prestados a un usuario
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            print(f"Libros prestados a {usuario.nombre}:")
            if self.prestamos[id_usuario]:
                for libro in self.prestamos[id_usuario]:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no existe.")


# -------------------
# Menú principal
# -------------------
def menu():
    mi_biblioteca = Biblioteca()
    while True:
        # Opciones principales del sistema
        print("--Menú Principal--\n")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar Usuario")
        print("4. Dar de baja a usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar préstamos")
        print("9. Salir\n")

        opcion = input("\nElije una opción: ")

        if opcion == "1":
            # Añadir libro
            titulo = input("Ingrese el título del libro: ").strip()
            autor = input("Ingrese el autor del libro: ").strip()
            categoria = input("Ingrese la categoría del libro: ").strip()
            isbn = input("Ingrese el ISBN del libro: ").strip()
            libro = Libro(titulo, autor, categoria, isbn)
            mi_biblioteca.añadir_libro(libro)

        elif opcion == "2":
            # Quitar libro
            isbn = input("\nIngrese el ISBN del libro: ").strip()
            mi_biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            # Registrar usuario
            nombre = input("\nIngrese el nombre del usuario: ").strip()
            id_usuario = input("Ingrese ID del usuario: ").strip()
            usuario = Usuario(nombre, id_usuario)
            mi_biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            # Dar de baja a usuario
            id_usuario = input("Ingrese ID del usuario: ").strip()
            mi_biblioteca.dar_debaja_usuario(id_usuario)

        elif opcion == "5":
            # Prestar libro
            id_usuario = input("Ingrese ID del usuario: ").strip()
            isbn = input("Ingrese ISBN del libro: ").strip()
            mi_biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            # Devolver libro
            id_usuario = input("Ingrese ID del usuario: ").strip()
            isbn = input("Ingrese ISBN del libro: ").strip()
            mi_biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            # Buscar libro
            criterio = input("Ingrese el criterio de búsqueda (titulo, autor o categoria): ").strip()
            valor = input("Ingrese el valor a buscar: ").strip()
            mi_biblioteca.buscar_libro(criterio, valor)

        elif opcion == "8":
            # Listar préstamos
            id_usuario = input("Ingrese ID del usuario: ").strip()
            mi_biblioteca.listar_prestamos(id_usuario)

        elif opcion == "9":
            # Salir del programa
            print("Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente")


# Ejecutar menú
menu()