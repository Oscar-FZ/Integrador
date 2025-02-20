import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
import test_wifi as wifi
print("Hola")
#s=wifi.init()
s=1
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

def create_custom_messagebox(title, message, red_blink = False):
    #Nuevo top level
    custom_box = tk.Toplevel(root)
    custom_box.title(title)
 
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

def show_message(title, message):
    messagebox.showinfo(title, message)
def create_custom_messagebox(title, message, red_blink = False):
     #Nuevo top level
     custom_box = tk.Toplevel(root)
     custom_box.title(title)
     
     # Tamaño
     custom_box.geometry("400x200")  # Width x Height
     message_font = tkfont.Font(size=32)
     # Mensaje
     message_label = tk.Label(custom_box, text=message, wraplength=350, font=message_font)
     message_label.pack(pady=20)
     if red_blink:
         # Function to toggle the text color
         def toggle_color():
             current_color = message_label.cget("foreground")
             next_color = "red" if current_color == "black" else "black"
             message_label.config(foreground=next_color)
             custom_box.after(500, toggle_color)  # Toggle every 500ms
         
         # Start the blinking effect
         toggle_color()
     # Ok
     ok_button = tk.Button(custom_box, text="OK", command=custom_box.destroy)
     ok_button.pack(pady=10)
     # Centrar el messagebox
     custom_box.update_idletasks()                                                                                                
     width = custom_box.winfo_width()
     height = custom_box.winfo_height()
     x = (custom_box.winfo_screenwidth() // 2) - (width // 2)
     y = (custom_box.winfo_screenheight() // 2) - (height // 2)
     custom_box.geometry(f'{width}x{height}+{x}+{y}')
     
     # Crear la nueva ventana
     custom_box.transient(root)
     custom_box.grab_set()
     root.wait_window(custom_box)

# Acción del botón central (con respuestas según la opción seleccionada)
def handle_center_button( event=None):
    selected_option = options[current_index]
    # Respuesta según la opción seleccionada
    if selected_option == "Ventilador":
        print("A")
        #  wifi.send_message("d",s)
    elif selected_option == "Luces":
        print("B")  #  wifi.send_message("c",s)
    elif selected_option == "Emergencia":
        create_custom_messagebox("Llamado de Emergencia", "Llamando por emergencia", True)
      #  wifi.send_message("a",s)
    elif selected_option == "Llamada":
     #   wifi.send_message("b",s)
        create_custom_messagebox("Llamando Asistente", "Llamando asistente", False)
# Configuración de la ventana
root = tk.Tk()
root.title("Navegación Circular")
root.geometry("900x600")  # Ajuste de tamaño para incluir todo

# Fuentes para texto
button_font = tkfont.Font(size=16)
label_font = tkfont.Font(size=60)
header_font = tkfont.Font(size=60, weight="bold")

# Cargar imágenes (reemplazar con tus archivos)
image_paths = [
    "FAN.png", "BOMBILLO - icons chaves-01.png",
    "AMBULANCIA - icons chaves-05.png", "TELEFONO.png"
]
images = [tk.PhotoImage(file=image_path) for image_path in image_paths]

# Botones para las opciones
left_button = tk.Button(root, command=move_left, height=600, width=500)
center_button = tk.Button(root, command=handle_center_button(s), height=700, width=600)
right_button = tk.Button(root, command=move_right, height=600, width=500)

# Etiquetas debajo de los botones
left_label = tk.Label(root, font=label_font)
center_label = tk.Label(root, font=label_font)
right_label = tk.Label(root, font=label_font)

# Etiquetas encima de los botones
left_header = tk.Label(root, text="Anterior", font=header_font)
center_header = tk.Label(root, text="Selección", font=header_font)
right_header = tk.Label(root, text="Siguiente", font=header_font)

# Etiqueta para mostrar las respuestas
response_label = tk.Label(root, text="", font=label_font, fg="black")

# Líneas separadoras
left_separator = tk.Frame(root, bg="black", width=2)
right_separator = tk.Frame(root, bg="black", width=2)

# Posicionar etiquetas superiores
left_header.place(relx=0.2, rely=0.05, anchor="center")
center_header.place(relx=0.5, rely=0.05, anchor="center")
right_header.place(relx=0.8, rely=0.05, anchor="center")

# Posicionar botones
left_button.place(relx=0.2, rely=0.4, anchor="center")
center_button.place(relx=0.5, rely=0.4, anchor="center")
right_button.place(relx=0.8, rely=0.4, anchor="center")

# Posicionar etiquetas inferiores
left_label.place(relx=0.2, rely=0.8, anchor="center")
center_label.place(relx=0.5, rely=0.8, anchor="center")
right_label.place(relx=0.8, rely=0.8, anchor="center")

# Posicionar la etiqueta de respuesta
response_label.place(relx=0.5, rely=0.9, anchor="center")

# Posicionar líneas separadoras
left_separator.place(relx=0.35, rely=0.1, relheight=0.8)
right_separator.place(relx=0.65, rely=0.1, relheight=0.8)

# Actualizar botones y etiquetas iniciales
update_buttons()

# Asociar teclas de flecha
root.bind("<Right>", move_right)
root.bind("<Left>", move_left)
root.bind("<Return>", handle_center_button())
root.wm_attributes('-zoomed', 1) 
# Ejecutar la aplicación
root.mainloop()

