import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
import pyautogui
import cv2
from GazeTracking.gaze_tracking import GazeTracking

# Inicializamos el seguimiento ocular
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

# Lista de opciones y variables globales
options = ["Ventilador", "Luces", "Emergencia", "Llamada"]
colors = ["#CCFFCC", "#CCCCFF", "#FFCCCC", "#FFFFCC"]  # Verde, Azul, Rojo, Amarillo
current_index = 1  # Empezamos con "Luces" en el centro

# Función para actualizar los botones según la opción central
def update_buttons():
    left_index = (current_index - 1) % len(options)
    right_index = (current_index + 1) % len(options)

    # Actualizamos los botones y las etiquetas
    left_button.config(bg=colors[left_index])
    center_button.config(bg=colors[current_index])
    right_button.config(bg=colors[right_index])

    left_label.config(text=options[left_index])
    center_label.config(text=options[current_index])
    right_label.config(text=options[right_index])

def move_right():
    global current_index
    current_index = (current_index + 1) % len(options)
    update_buttons()

def move_left():
    global current_index
    current_index = (current_index - 1) % len(options)
    update_buttons()

def handle_center_button():
    selected_option = options[current_index]
    if selected_option == "Ventilador":
        print("Activando Ventilador")
    elif selected_option == "Luces":
        print("Activando Luces")
    elif selected_option == "Emergencia":
        print("Llamado de Emergencia")
    elif selected_option == "Llamada":
        print("Llamando Asistente")

# Configuración de la ventana
root = tk.Tk()
root.title("Navegación Circular")
root.geometry("900x600")

# Fuentes para texto
button_font = tkfont.Font(size=16)
label_font = tkfont.Font(size=60)

# Cargar imágenes (puedes usar iconos si lo deseas)
images = [tk.PhotoImage(file="FAN.png"), tk.PhotoImage(file="BOMBILLO.png"),
          tk.PhotoImage(file="AMBULANCIA.png"), tk.PhotoImage(file="TELEFONO.png")]

# Botones para las opciones
left_button = tk.Button(root, command=move_left, height=600, width=500)
center_button = tk.Button(root, command=handle_center_button, height=700, width=600)
right_button = tk.Button(root, command=move_right, height=600, width=500)

# Etiquetas debajo de los botones
left_label = tk.Label(root, font=label_font)
center_label = tk.Label(root, font=label_font)
right_label = tk.Label(root, font=label_font)

# Posicionar los elementos
left_button.place(relx=0.2, rely=0.4, anchor="center")
center_button.place(relx=0.5, rely=0.4, anchor="center")
right_button.place(relx=0.8, rely=0.4, anchor="center")

left_label.place(relx=0.2, rely=0.8, anchor="center")
center_label.place(relx=0.5, rely=0.8, anchor="center")
right_label.place(relx=0.8, rely=0.8, anchor="center")

# Actualizar botones y etiquetas iniciales
update_buttons()

# Función para manejar la detección de la mirada
def track_gaze():
    global current_index

    # Leemos un frame de la cámara
    _, frame = webcam.read()

    # Enviamos el frame a GazeTracking
    gaze.refresh(frame)

    # Dibujamos la anotación sobre el frame
    frame = gaze.annotated_frame()

    # Si se está mirando hacia la derecha
    if gaze.is_right():
        print("Mirando a la derecha")
        move_right()  # Simulamos la pulsación de la tecla de flecha derecha
    # Si se está mirando hacia la izquierda
    elif gaze.is_left():
        print("Mirando a la izquierda")
        move_left()  # Simulamos la pulsación de la tecla de flecha izquierda

    # Mostramos el texto de lo que está haciendo el usuario
    text = ""
    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    # Mostramos los resultados de la posición de las pupilas
    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    # Mostramos el frame con anotaciones
    cv2.imshow("Gaze Tracking", frame)

    # Llamamos a la función nuevamente en el próximo ciclo
    root.after(10, track_gaze)

# Iniciamos el seguimiento ocular en la interfaz
track_gaze()

# Ejecutamos la aplicación
root.mainloop()

# Liberamos los recursos de la cámara al salir
webcam.release()
cv2.destroyAllWindows()

