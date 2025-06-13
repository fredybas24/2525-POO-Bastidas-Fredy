# Registro de temperaturas -- Programación Tradicional


# Función para ingresar las temperaturas de 7 días
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Mostramos en consola
print("REGISTRO SEMANAL DE TEMPERATURAS")
temperaturas = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas)
print(f"El promedio semanal es: {promedio:.2f}°C")
