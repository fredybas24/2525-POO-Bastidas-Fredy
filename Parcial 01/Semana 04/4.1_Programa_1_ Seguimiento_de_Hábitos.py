# Clase que representa un hábito que se desea seguir
class Habito:
    def __init__(self, nombre):
        self.nombre = nombre
        self.completado = False  # Estado del hábito diario

    def marcar_completado(self):
        self.completado = True
        print(f"Hábito completado: {self.nombre}")

    def reiniciar(self):
        self.completado = False

    def estado(self):
        estado = "✅" if self.completado else "❌"
        print(f"{estado} {self.nombre}")


# Clase que gestiona el seguimiento diario de los hábitos
class Seguimiento:
    def __init__(self):
        self.habitos = []

    def agregar_habito(self, habito):
        self.habitos.append(habito)
        print(f"Hábito agregado: {habito.nombre}")

    def mostrar_estado_diario(self):
        print("\nEstado diario de hábitos:")
        for habito in self.habitos:
            habito.estado()

    def reiniciar_todos(self):
        for habito in self.habitos:
            habito.reiniciar()
        print("Estado de todos los hábitos reiniciado.")


# Simulación del programa
seguimiento = Seguimiento()

# Crear algunos hábitos
leer = Habito("Leer 20 minutos")
agua = Habito("Beber 8 vasos de agua")
ejercicio = Habito("Hacer ejercicio 30 minutos")

# Agregar al sistema de seguimiento
seguimiento.agregar_habito(leer)
seguimiento.agregar_habito(agua)
seguimiento.agregar_habito(ejercicio)

seguimiento.mostrar_estado_diario()

# Marcar algunos como completados
leer.marcar_completado()
agua.marcar_completado()

seguimiento.mostrar_estado_diario()

# Reiniciar todos para un nuevo día
seguimiento.reiniciar_todos()
seguimiento.mostrar_estado_diario()
