# Tkinter
# Módulo para crear interfaces gráficas de usuario

from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title = "BC&B PI-Evolución"
        self.icon = './imagenes/BCBIcono.ico'
        self.icon_alt = './21-tkinter/imagenes/BCBIcono.ico'
        self.size = "770x470"
        self.resizable = False
    
    def cargar(self):

        # Crear la ventana raíz

        ventana = Tk()
        self.ventana = ventana
        # Titulo de la ventana
        # ventana.title("Bc&B")
        ventana.title(self.title)

        # Comprobar si existe una ruta
        #ruta_icono = os.path.abspath('./imagenes/BCBIcono.ico')
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            #ruta_icono = os.path.abspath('./21-tkinter/imagenes/BCBIcono.ico')
            ruta_icono = os.path.abspath(self.icon_alt)

        # Icono de la ventana
        #ventana.iconbitmap("./21-tkinter/imagenes/BCBIcono.ico")
        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Cambio en el tamaño de la ventana
        #ventana.geometry("750x450")
        ventana.geometry(self.size)

        # Bloquear tamaño de la ventana
        #ventana.resizable(0,0)
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)

        # Arrancar y mostrar la ventana hasta que se cierre
        #ventana.mainloop()

    def addTexto(self, dato):
        texto = Label(self.ventana, text= dato)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

#    Instanciar mi progrma

programa = Programa()
programa.cargar()
programa.addTexto("Hola")
programa.addTexto("Soy Eric Márquez")
programa.addTexto("Estoy realizando el curso")
programa.addTexto("Master en Python")
programa.mostrar()