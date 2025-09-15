import tkinter as tk
from tkinter import messagebox

# Función para agregar información
def agregar_datos():
    texto = entrada.get().strip()  # Obtener texto y quitar espacios al inicio y al final
    if texto != "":                # Verificar que no esté vacío
        listbox.insert(tk.END, texto)  # Agregar el texto al final de la lista
        entrada.delete(0, tk.END)      # Limpiar el campo de entrada para un nuevo dato
    else:
        # Mostrar ventana de error si el campo estaba vacío
        messagebox.showerror("Error", "Por favor ingresa un dato")

# Función para borrar todos los elementos de la lista
def limpiar_lista():
    listbox.delete(0, tk.END)  # 0 = primer elemento, tk.END = último elemento

#===================
# Ventana principal
#===================

ventana = tk.Tk()                      # Crear la ventana principal
ventana.title("Películas Favoritas")   # Título de la ventana
ventana.geometry("500x400")            # Tamaño de la ventana (ancho x alto)
ventana.resizable(False, False)        # Evitar que el usuario cambie el tamaño

# ================================
# Widgets (componentes de la GUI)
# ================================

# Etiqueta para indicar al usuario qué hacer
etiqueta = tk.Label(
    ventana,
    text="Ingresa tus películas favoritas",
    font=("Arial", 14)  # Tamaño y tipo de letra
)
etiqueta.grid(
    row=0, column=0, columnspan=2,  # Ocupa 2 columnas
    pady=10                          # Separación vertical con otros widgets
)

# Campo de entrada de texto
entrada = tk.Entry(
    ventana,
    width=50,          # Ancho del campo
    font=("Arial", 12) # Tipo y tamaño de letra
)
entrada.grid(
    row=1, column=0, columnspan=2,  # Ocupa 2 columnas
    padx=10, pady=5                 # Separación horizontal y vertical
)

# Botón "Agregar" para añadir datos a la lista
boton_agregar = tk.Button(
    ventana,
    text="Agregar",
    width=20,             # Ancho del botón
    command=agregar_datos # Función que se ejecuta al presionar
)
boton_agregar.grid(
    row=2, column=0,
    padx=10, pady=10
)

# Botón "Limpiar" para borrar todos los datos de la lista
boton_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    width=20,
    command=limpiar_lista
)
boton_limpiar.grid(
    row=2, column=1,
    padx=10, pady=10
)

# Lista para mostrar los datos agregados
listbox = tk.Listbox(
    ventana,
    height=15,         # Cantidad de filas visibles
    width=60,          # Ancho en caracteres
    font=("Arial", 12) # Tipo y tamaño de letra
)
listbox.grid(
    row=3, column=0, columnspan=2,  # Ocupa 2 columnas
    padx=10, pady=10
)


ventana.mainloop()  # Mantiene la ventana abierta y escucha los eventos
