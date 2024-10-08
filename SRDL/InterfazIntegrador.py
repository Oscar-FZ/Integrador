import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont  

def BotonMenuPrincipal(opcion):
    if opcion == 1:
        print("Encendiendo luces")
    elif opcion == 2:
        create_submenu()
    elif opcion == 3: 
        messagebox.showinfo("Llamando asistente", "Llamando Asistente")
    elif opcion == 4: 
        messagebox.showinfo("Llamado de emergencia", "Llamando por emergencia")
def BotonMenuSecundario(opcion,submenu_frame):
    if opcion==1:
        print("Encenciendo Televisor")
    elif opcion == 2: 
        print("Encendiendo Ventilador")    
    elif opcion ==3:
        menuprincipal(submenu_frame)
    elif opcion==4:
        messagebox.showinfo("Llamado de emergencia", "Llamando por emergencia")    
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
    submenu_colors = ["#FFCCCC", "#CCFFCC", "#CCCCFF", "#FFFFCC"]

    # Cargo imagenes
    submenu_image_paths = ["Image1.png", "Image1.png", "Image1.png", "Image1.png"]
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
colors = ["#FFCCCC", "#CCFFCC", "#CCCCFF", "#FFFFCC"]


image_paths = ["Luces.png", "Control.png", "Llamada.png", "Emergencia1.png"]
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
