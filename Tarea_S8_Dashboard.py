import os

# Función que muestra el contenido de un archivo .py en la consola
def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    # MODIFICACIÓN: Se añadieron 9 scripts correspondientes a las semanas 2 a 7 del Parcial 01
    opciones = {
        '1': 'Parcial 01/Semana 02/Tarea_S2.py',
        '2': 'Parcial 01/Semana 03/3.1_Tarea_S3_Programación_Tradicional.py',
        '3': 'Parcial 01/Semana 03/3.2_Tarea_S3_POO.py',
        '4': 'Parcial 01/Semana 04/4.1_Programa_1_ Seguimiento_de_Hábitos.py',
        '5': 'Parcial 01/Semana 04/4.2_Programa_2_Control_de_Mascotas_en_Veterinaria.py',
        '6': 'Parcial 01/Semana 04/4.3_Programa_3_Registro_de_Curso.py',
        '7': 'Partial 01/Semana 05/Tarea_S5_Identificadores.py',
        '8': 'Parcial 01/Semana 06/Tarea_S6_Aplicación_de_Conceptos_de_POO.py',
        '9': 'Parcial 01/Semana 07/Tarea_S7_Constructores_Destructores.py'
    }

    while True:
        print("\nMi panel de Programación Orientada a Objetos")
        print("Bienvenid@. Elige un ejemplo para ver su código.")
        print("=============================================")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()