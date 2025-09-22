import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import tkinter.messagebox as messagebox


# ---------------- FUNCIONES ----------------

def agregar_evento():
    # Agrega un evento al TreeView con los datos ingresados.
    fecha = entry_fecha.get()
    hora = entry_hora.get().strip()
    descripcion = entry_desc.get().strip()

    if not fecha or not hora or not descripcion:
        messagebox.showerror("Error", "Por favor completa todos los campos")
        return

    # Insertar el evento en el TreeView
    mi_arbol.insert(
        parent='', index='end',
        values=(fecha, hora, descripcion)
    )

    # Limpiar campos después de agregar
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)


def eliminar_evento():
    # Elimina el evento seleccionado del TreeView.
    seleccionado = mi_arbol.selection()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")
        return

    for item in seleccionado:
        mi_arbol.delete(item)


def salir():
    # Cierra la aplicación.
    root.quit()


# ---------------- VENTANA PRINCIPAL ----------------

root = tk.Tk()
root.title("Agenda Personal")
root.geometry("650x500")

# ---------------- FRAME: VISUALIZACIÓN DE EVENTOS ----------------
frame_lista = ttk.Frame(root)
frame_lista.pack(pady=10, fill="x")

label_lista = tk.Label(frame_lista, text="Eventos Programados", font=("Times New Rowman", 12, "bold"))
label_lista.pack()

# Scrollbar
scroll = ttk.Scrollbar(frame_lista)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# TreeView
mi_arbol = ttk.Treeview(
    frame_lista,
    columns=("Fecha", "Hora", "Descripción"),
    yscrollcommand=scroll.set,
    selectmode="extended"
)
mi_arbol.pack(fill="x")

scroll.config(command=mi_arbol.yview)

# Configurar columnas
mi_arbol.column("#0", width=0, stretch=tk.NO) # Columna oculta
mi_arbol.column("Fecha", anchor=tk.CENTER, width=100)
mi_arbol.column("Hora", anchor=tk.CENTER, width=80)
mi_arbol.column("Descripción", anchor=tk.W, width=300)

# Encabezados
mi_arbol.heading("#0", text="", anchor=tk.W)
mi_arbol.heading("Fecha", text="Fecha", anchor=tk.CENTER)
mi_arbol.heading("Hora", text="Hora", anchor=tk.CENTER)
mi_arbol.heading("Descripción", text="Descripción", anchor=tk.CENTER)

# ---------------- FRAME: FORMULARIO DE ENTRADA ----------------
frame_form = ttk.Frame(root)
frame_form.pack(pady=20)

# Etiquetas y campos

# Fecha
tk.Label(frame_form, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_fecha = DateEntry(frame_form, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

# Hora
tk.Label(frame_form, text="Hora (HH:MM):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_hora = tk.Entry(frame_form, width=15)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

# Descripción
tk.Label(frame_form, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_desc = tk.Entry(frame_form, width=40)
entry_desc.grid(row=2, column=1, padx=5, pady=5)

# ---------------- FRAME: BOTONES ----------------
frame_botones = ttk.Frame(root)
frame_botones.pack(pady=20)

# Agregar Evento
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

# Eliminar evento
btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

# Salir de la GUI
btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=10)

# ---------------- LOOP PRINCIPAL ----------------
root.mainloop()
