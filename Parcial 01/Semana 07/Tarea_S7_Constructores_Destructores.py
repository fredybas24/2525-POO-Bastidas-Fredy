# Clase que representa un planeta
class Planeta:
    def __init__(self, nombre, habitantes):
        """
        Constructor: se llama automáticamente cuando se crea un objeto Planeta.
        Inicializa el nombre y la cantidad de habitantes del planeta.
        """
        self.nombre = nombre
        self.habitantes = habitantes
        print(f"🌍 El planeta {self.nombre} ha sido creado con {self.habitantes} habitantes.")

    def __del__(self):
        """
        Destructor: se llama automáticamente cuando el objeto es eliminado
        (usando 'del' o al final del programa).
        Simula la destrucción del planeta por Freezer.
        """
        print(f"💥 ¡Freezer ha destruido el planeta {self.nombre}! Sus {self.habitantes} habitantes han desaparecido...\n")


# --- Simulación de la historia ---
print("🧊 Freezer ha llegado al sistema estelar...\n")

# Creamos algunos planetas
planeta1 = Planeta("Namek", 100000)
planeta2 = Planeta("Vegeta", 200000)
planeta3 = Planeta("Tierra", 8000000000)

print("\n😈 Freezer decide destruir los planetas uno por uno...\n")

# Freezer destruye Namek
del planeta1  # Se llama automáticamente al destructor

# Freezer destruye Vegeta
del planeta2

# La Tierra se destruye al final del programa, el destructor se llama automáticamente al cerrar
print("🌌 El universo continúa... por ahora...\n")


