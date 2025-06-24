# Programa: Calculadora de días para semanas y días restantes
# Convierte un número total de días ingresados por el usuario en semanas y días restantes.

def calcular_semanas_dias(total_dias):
    """
    Dado un número total de días, devuelve cuántas semanas completas y días sobrantes hay.
    """
    semanas = total_dias // 7    # división entera para semanas completas
    dias_restantes = total_dias % 7  # resto para días que no completan una semana
    return semanas, dias_restantes

print("Calculadora de semanas y días restantes")

entrada = input("Ingresa un número total de días (entero): ")

if entrada.isdigit():
    dias = int(entrada)
    semanas, dias_restantes = calcular_semanas_dias(dias)

    print(f"{dias} días equivalen a {semanas} semana(s) y {dias_restantes} día(s).")
else:
    print("Por favor, ingresa un número entero válido.")
