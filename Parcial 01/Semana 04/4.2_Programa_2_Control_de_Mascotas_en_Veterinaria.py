# Clase que representa una mascota
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_info(self):
        print(f"{self.nombre} es un {self.especie} de {self.edad} años.")


# Clase que representa una veterinaria
class Veterinaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"Mascota registrada: {mascota.nombre}")

    def mostrar_mascotas(self):
        print(f"Mascotas en la veterinaria {self.nombre}:")
        for mascota in self.mascotas:
            mascota.mostrar_info()


# Simulación del programa
vet = Veterinaria("La Clínica del Guau y Miau")

mascota1 = Mascota("Otis", "perro", 3)
mascota2 = Mascota("Milo", "gato", 2)

vet.registrar_mascota(mascota1)
vet.registrar_mascota(mascota2)

vet.mostrar_mascotas()
