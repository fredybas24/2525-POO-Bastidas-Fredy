# Registro de temperaturas -- POO


# Creamos una clase que representa el clima semanal
class Clima:
    def __init__(self):
        # Encapsulamos la lista de temperaturas
        self.__temperaturas = []

    # Método para ingresar datos
    def ingresar_temperaturas(self):
        for dia in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
            self.__temperaturas.append(temperatura)

    # Método para calcular promedio
    def calcular_promedio(self):
        if len(self.__temperaturas) == 7:
            return sum(self.__temperaturas) / 7
        else:
            return 0

# Clase hija que hereda de Clima y añade una descripción
class ClimaConDescripcion(Clima):
    def describir_clima(self):
        promedio = self.calcular_promedio()
        if promedio > 30:
            return "Muy caluroso"
        elif promedio >= 20:
            return "Agradable"
        else:
            return "Frío"

# Mostramos en cosola
print("REGISTRO SEMANAL DE TEMPERATURAS (POO)")
clima = ClimaConDescripcion()  # Creamos un objeto

clima.ingresar_temperaturas() # Llamamos método
promedio = clima.calcular_promedio()
descripcion = clima.describir_clima()

print(f"Promedio: {promedio:.2f}°C")
print(f"Descripción del clima: {descripcion}")
