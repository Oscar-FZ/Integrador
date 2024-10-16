import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont  

def BotonMenuPrincipal(opcion):
    if opcion == 1:
        print("Encendiendo luces")
    elif opcion == 2:
        create_submenu()
    elif opcion == 3: 
       create_custom_messagebox("Llamando Asistente", "Llamando Asistente", False)
    elif opcion == 4: 
        create_custom_messagebox("Llamado de emergencia", "Llamando por emergencia", True)
def BotonMenuSecundario(opcion,submenu_frame):
    if opcion==1:
        print("Encenciendo Televisor")
    elif opcion == 2: 
        print("Encendiendo Ventilador")    
    elif opcion ==3:
        menuprincipal(submenu_frame)
    elif opcion==4:
        create_custom_messagebox("Llamado de emergencia", "Llamando por emergencia", True)    
def create_submenu():
    # Oculto el menu principal
    main_frame.pack_forget()

    # Defino el frame nuevo
    submenu_frame = tk.Frame(root)
    submenu_frame.pack(fill="both", expand=True)

    #Defino el grid del submenu
    submenu_frame.columnconfigure(0, weight=1)
    submenu_frame.columnconfigure(1, weight=1)
    submenu_frame.rowconfigure(0, weight=1)
    submenu_frame.rowconfigure(1, weight=1)
    # Defino los botones
    submenu_button_texts = ["Televisor", "Ventilador", "Atrás", "Emergencia"]

    # Defino colores
    submenu_colors = ["#FFFFCC", "#CCFFCC", "#CCCCFF", "#FFCCCC"]

    # Cargo imagenes
    submenu_image_paths = ["TELE.png", "FAN.png", "back.png", "AMBULANCIA - icons chaves-05.png"]
    submenu_images = [tk.PhotoImage(file=image_path) for image_path in submenu_image_paths]

    # Creo los botones del submenu en sí
    for i, (text, image) in enumerate(zip(submenu_button_texts, submenu_images), start=1):
        btn = tk.Button(submenu_frame, text=text,
                        image=image,  #Pongo la imagen
                        compound="top",  # Pongo la imagen sobre el texto
                        bg=submenu_colors[i-1],  # Pongo el color
                        font=button_font,  # Ajusto la fuente
                        command=lambda i=i: BotonMenuSecundario(i, submenu_frame))
        btn.grid(row=(i-1)//2, column=(i-1)%2, sticky="nsew")
        btn.image = image  # Mantengo una referencia

def menuprincipal(submenu_frame):
    # Vuelvo al menu principal
    submenu_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)
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
root = tk.Tk()
root.title("Prueba base")

button_font = tkfont.Font(size=32)  # Incremento el tamaño de fuente

# Maximizo
root.state('zoomed')  # Windows
#root.wm_attributes('-zoomed', 1)  #  Linux

# Defino el main frame
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Defino el texto
button_texts = ["Luces", "Electrodomesticos", "Llamada", "Emergencia"]

# Defino colores
colors = ["#FFFFCC", "#CCFFCC", "#CCCCFF", "#FFCCCC"]


image_paths = ["BOMBILLO - icons chaves-01.png", "CONTROL - icons chaves-02.png", "TELEFONO.png", "AMBULANCIA - icons chaves-05.png"]
images = [tk.PhotoImage(file=image_path) for image_path in image_paths]

# Creo botones
for i, (text, image) in enumerate(zip(button_texts, images), start=1):
    btn = tk.Button(main_frame, text=text,
                    image=image,  #Setteo imagen
                    compound="top",  # Arriba del texto
                    bg=colors[i-1],  # Color
                    font=button_font,  # Fuente
                    command=lambda i=i: BotonMenuPrincipal(i))
    btn.grid(row=(i-1)//2, column=(i-1)%2, sticky="nsew") #Acomodo en grid
    btn.image = image  

# Configuro el grid
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

root.mainloop()
