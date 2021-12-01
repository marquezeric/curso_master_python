from tkinter import *


ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana,text="Bienvenido a mi programa")
texto.config(
            fg= "White",
            bg = "#04238C", #  Se puede definir también por Hexadecimal
            padx = 50,
            pady = 20,
            font = ("Montserrat", 30)
            )
texto.pack()

texto = Label(ventana,text = "Soy Eric Márquez")
texto.config( 
            font = ("Montserrat", 16),
            height =3,
            bg = "orange",
            padx = 10,
            pady = 1,
            cursor = "clock"
)
texto.pack(anchor=NW)

def pruebas(nombre,apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"


texto = Label(ventana, text=pruebas( pais="México", nombre="Eric", apellidos="Márquez"))
texto.config( 
            font = ("Montserrat", 16),
            height =3,
            bg = "red",
            padx = 10,
            pady = 1,
            cursor = "clock"
)
texto.pack(anchor=SE)

ventana.mainloop()