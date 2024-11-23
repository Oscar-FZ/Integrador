import tkinter as tk
from tkinter import font as tkfont

# Lista circular de opciones
options = ["Ventilador", "Luces", "Emergencia", "Llamada"]
colors = ["#CCFFCC", "#CCCCFF", "#FFCCCC", "#FFFFCC"]  # Verde, Azul, Rojo, Amarillo
current_index = 1  # Empezamos con "Luces" en el centro

# Función para actualizar los botones según la opción central
def update_buttons():
    # Determinar posiciones izquierda, centro y derecha
    left_index = (current_index - 1) % len(options)
    right_index = (current_index + 1) % len(options)

    # Actualizar botones
    left_button.config(image=images[left_index], bg=colors[left_index])
    center_button.config(image=images[current_index], bg=colors[current_index])
    right_button.config(image=images[right_index], bg=colors[right_index])

    # Actualizar etiquetas de texto
    left_label.config(text=options[left_index])
    center_label.config(text=options[current_index])
    right_label.config(text=options[right_index])

# Mover hacia la derecha
def move_right(event=None):
    global current_index
    current_index = (current_index + 1) % len(options)
    update_buttons()

# Mover hacia la izquierda
def move_left(event=None):
    global current_index
    current_index = (current_index - 1) % len(options)
    update_buttons()

# Acción del botón central
def handle_center_button():
    print(f"Opción seleccionada: {options[current_index]}")

# Configuración de la ventana
root = tk.Tk()
root.title("Navegación Circular")
root.geometry("900x600")  # Ajuste de tamaño para incluir todo

# Fuentes para texto
button_font = tkfont.Font(size=16)
label_font = tkfont.Font(size=40)
header_font = tkfont.Font(size=40, weight="bold")

# Cargar imágenes (reemplazar con tus archivos)
image_paths = [
    "FAN.png", "BOMBILLO - icons chaves-01.png",
    "AMBULANCIA - icons chaves-05.png", "TELEFONO.png"
]
images = [tk.PhotoImage(file=image_path) for image_path in image_paths]

# Botones para las opciones
left_button = tk.Button(root, command=move_left, height=450, width=300)
center_button = tk.Button(root, command=handle_center_button, height=500, width=350)
right_button = tk.Button(root, command=move_right, height=450, width=300)

# Etiquetas debajo de los botones
left_label = tk.Label(root, font=label_font)
center_label = tk.Label(root, font=label_font)
right_label = tk.Label(root, font=label_font)

# Etiquetas encima de los botones
left_header = tk.Label(root, text="Anterior", font=header_font)
center_header = tk.Label(root, text="Selección", font=header_font)
right_header = tk.Label(root, text="Siguiente", font=header_font)

# Líneas separadoras
left_separator = tk.Frame(root, bg="black", width=2)
right_separator = tk.Frame(root, bg="black", width=2)

# Posicionar etiquetas superiores
left_header.place(relx=0.2, rely=0.03, anchor="center")
center_header.place(relx=0.5, rely=0.03, anchor="center")
right_header.place(relx=0.8, rely=0.03, anchor="center")

# Posicionar botones
left_button.place(relx=0.2, rely=0.4, anchor="center")
center_button.place(relx=0.5, rely=0.4, anchor="center")
right_button.place(relx=0.8, rely=0.4, anchor="center")

# Posicionar etiquetas inferiores
left_label.place(relx=0.2, rely=0.8, anchor="center")
center_label.place(relx=0.5, rely=0.8, anchor="center")
right_label.place(relx=0.8, rely=0.8, anchor="center")

# Posicionar líneas separadoras
left_separator.place(relx=0.35, rely=0.1, relheight=0.8)
right_separator.place(relx=0.65, rely=0.1, relheight=0.8)

# Actualizar botones y etiquetas iniciales
update_buttons()

# Asociar teclas de flecha
root.bind("<Right>", move_right)
root.bind("<Left>", move_left)

# Ejecutar la aplicación
root.mainloop()