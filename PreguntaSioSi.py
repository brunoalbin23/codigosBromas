import tkinter as tk
import random

def mover_boton_no(event):
    nuevo_x = random.randint(0, ventana.winfo_width() - boton_no.winfo_width())
    nuevo_y = random.randint(0, ventana.winfo_height() - boton_no.winfo_height())
    boton_no.place(x=nuevo_x, y=nuevo_y)

def respuesta_si():
    label.config(text="¡Sabía que dirías que sí!") #Cambiar dpendiendo de lo que queremos al responder la pregunta 

ventana = tk.Tk()
ventana.title("Pregunta Importante")
ventana.geometry("400x200")

label = tk.Label(ventana, text="¿Quieres ser mi novia?") #Cambiar pregunta
label.pack(pady=20)

boton_si = tk.Button(ventana, text="Sí", command=respuesta_si)
boton_si.pack(side=tk.LEFT, padx=20)

boton_no = tk.Button(ventana, text="No")
boton_no.pack(side=tk.RIGHT, padx=20)

boton_no.bind("<Enter>", mover_boton_no)

ventana.mainloop()