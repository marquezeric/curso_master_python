from tkinter import *


ventana = Tk()
#  ventana.geometry("700x500")

texto = Label(ventana,text="Bienvenido a mi programa")
texto.config(
            fg= "White",
            bg = "#04238C", #  Se puede definir también por Hexadecimal
            padx = 50,
            pady = 20,
            font = ("Montserrat", 30)
            )
texto.pack(side=TOP)

texto = Label(ventana,text = "Soy Eric Márquez")
texto.config( 
            font = ("Montserrat", 16),
            height =3,
            bg = "orange",
            padx = 10,
            pady = 1,
            cursor = "clock"
)
texto.pack(side=TOP,expand=YES,fill=X)

texto = Label(ventana, text="Básico1")
texto.config( 
            font = ("Montserrat", 16),
            height =3,
            bg = "green",
            padx = 10,
            pady = 20,
            cursor = "clock"
)
texto.pack(side=LEFT, expand=YES, fill=X)

texto = Label(ventana, text="Básico2")
texto.config( 
            font = ("Montserrat", 16),
            height =3,
            bg = "red",
            padx = 10,
            pady = 20,
            cursor = "clock"
)
texto.pack(side=LEFT, expand=YES, fill=X)

texto = Label(ventana, text="Básico3")
texto.config( 
            font = ("Montserrat", 16),
            height =3,
            bg = "gray",
            padx = 10,
            pady = 20,
            cursor = "clock"
)
texto.pack(side=LEFT, expand=YES, fill=X)

ventana.mainloop()