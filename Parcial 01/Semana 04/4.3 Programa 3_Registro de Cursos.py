# Clase que representa un curso
class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def mostrar_info(self):
        print(f"{self.nombre} ({self.codigo})")


# Clase que representa un estudiante
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos_inscritos = []

    def inscribir(self, curso):
        self.cursos_inscritos.append(curso)
        print(f"{self.nombre} se ha inscrito en {curso.nombre}.")

    def mostrar_cursos(self):
        print(f"Cursos de {self.nombre}:")
        for curso in self.cursos_inscritos:
            curso.mostrar_info()


# Uso del sistema
curso1 = Curso("Programación I", "TI101")
curso2 = Curso("Sistemas Operativos", "TI202")

estudiante1 = Estudiante("Fredy Bastidas")

estudiante1.inscribir(curso1)
estudiante1.inscribir(curso2)

estudiante1.mostrar_cursos()
