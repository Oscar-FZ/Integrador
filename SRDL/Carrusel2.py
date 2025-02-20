import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
import test_wifi as wifi
import RPi.GPIO as GPIO
from gpiozero import LED 
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.HIGH)
print("Iniciando conexion")
# Inicializar la conexión Wi-Fi
s = wifi.init()

options = ["Ventilador", "Luces", "Emergencia", "Llamada"]
colors = ["#CCFFCC", "#CCCCFF", "#FFCCCC", "#FFFFCC"]
current_index = 1

def update_buttons():
    left_index = (current_index - 1) % len(options)
    right_index = (current_index + 1) % len(options)
    left_button.config(image=images[left_index], bg=colors[left_index])
    center_button.config(image=images[current_index], bg=colors[current_index])
    right_button.config(image=images[right_index], bg=colors[right_index])
    left_label.config(text=options[left_index])
    center_label.config(text=options[current_index])
    right_label.config(text=options[right_index])

def create_custom_messagebox(title, message, red_blink=False):
    custom_box = tk.Toplevel(root)
    custom_box.title(title)
    custom_box.geometry("400x200")
    message_font = tkfont.Font(size=32)
    message_label = tk.Label(custom_box, text=message, wraplength=350, font=message_font)
    message_label.pack(pady=20)
    if red_blink:
        def toggle_color():
            current_color = message_label.cget("foreground")
            next_color = "red" if current_color == "black" else "black"
            message_label.config(foreground=next_color)
            custom_box.after(500, toggle_color)
        toggle_color()
    ok_button = tk.Button(custom_box, text="OK", command=custom_box.destroy)
    ok_button.pack(pady=10)
    custom_box.update_idletasks()
    width = custom_box.winfo_width()
    height = custom_box.winfo_height()
    x = (custom_box.winfo_screenwidth() // 2) - (width // 2)
    y = (custom_box.winfo_screenheight() // 2) - (height // 2)
    custom_box.geometry(f'{width}x{height}+{x}+{y}')
    custom_box.transient(root)
    custom_box.grab_set()
    root.wait_window(custom_box)

def move_right(event=None):
    global current_index
    current_index = (current_index + 1) % len(options)
    update_buttons()

def move_left(event=None):
    global current_index
    current_index = (current_index - 1) % len(options)
    update_buttons()

def show_message(title, message):
    messagebox.showinfo(title, message)

# Función que maneja la acción del botón central (Enviar mensaje)
def handle_center_button(event=None):
    selected_option = options[current_index]
    if selected_option == "Ventilador":
        wifi.send_message("b", s)
    elif selected_option == "Luces":
            wifi.send_message("c", s)
    elif selected_option == "Emergencia":
        wifi.send_message("a", s)  # Enviar mensaje para Emergencia
        create_custom_messagebox("Llamado de Emergencia", "Llamando por emergencia", True)
    elif selected_option == "Llamada":
        
        wifi.send_message("d", s)  # Enviar mensaje para Llamada
        create_custom_messagebox("Llamando Asistente", "Llamando asistente", False)

root = tk.Tk()
root.title("Navegación Circular")
root.geometry("900x600")

button_font = tkfont.Font(size=16)
label_font = tkfont.Font(size=30)
header_font = tkfont.Font(size=30, weight="bold")

image_paths = [
    "FAN.png", "BOMBILLO - icons chaves-01.png",
    "AMBULANCIA - icons chaves-05.png", "TELEFONO.png"
]
images = [tk.PhotoImage(file=image_path) for image_path in image_paths]

left_button = tk.Button(root, command=move_left, height=300, width=300)
center_button = tk.Button(root, command=handle_center_button, height=350, width=300)
right_button = tk.Button(root, command=move_right, height=300, width=300)

left_label = tk.Label(root, font=label_font)
center_label = tk.Label(root, font=label_font)
right_label = tk.Label(root, font=label_font)

left_header = tk.Label(root, text="<-------", font=header_font)
center_header = tk.Label(root, text="Selección", font=header_font)
right_header = tk.Label(root, text="------->", font=header_font)

response_label = tk.Label(root, text="", font=label_font, fg="black")
left_separator = tk.Frame(root, bg="black", width=2)
right_separator = tk.Frame(root, bg="black", width=2)

left_header.place(relx=0.1, rely=0.05, anchor="center")
center_header.place(relx=0.5, rely=0.05, anchor="center")
right_header.place(relx=0.9, rely=0.05, anchor="center")

left_button.place(relx=0.2, rely=0.4, anchor="center")
center_button.place(relx=0.5, rely=0.4, anchor="center")
right_button.place(relx=0.8, rely=0.4, anchor="center")

left_label.place(relx=0.2, rely=0.8, anchor="center")
center_label.place(relx=0.5, rely=0.8, anchor="center")
right_label.place(relx=0.8, rely=0.8, anchor="center")

response_label.place(relx=0.5, rely=0.9, anchor="center")
left_separator.place(relx=0.35, rely=0.1, relheight=0.8)
right_separator.place(relx=0.65, rely=0.1, relheight=0.8)

update_buttons()

root.bind("<Right>", move_right)
root.bind("<Left>", move_left)
root.bind("<Return>", handle_center_button)  # Asegúrate de que la función se llame al presionar Enter

root.wm_attributes('-zoomed', 1)
root.mainloop()

