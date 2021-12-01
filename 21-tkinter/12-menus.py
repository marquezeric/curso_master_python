from tkinter import *


ventana = Tk()
ventana.geometry("600x600")

mi_menu = Menu(ventana)
ventana.config(
    menu = mi_menu
)

# Creación de los submenus
archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Abrir carpeta")
archivo.add_separator()
archivo.add_command(label="salir", command=ventana.quit)

editar = Menu(mi_menu, tearoff=0)
editar.add_command(label="Deshacer")
editar.add_command(label="Hacer")
editar.add_separator()
editar.add_command(label="Copiar")
editar.add_command(label="Cotar")
editar.add_command(label="Pegar")

seleccionar = Menu(mi_menu, tearoff=0)
seleccionar.add_command(label="Seleccionar todo")
seleccionar.add_command(label="Expandir selcción")
seleccionar.add_command(label="Contraer selección")

#  Creación del menu principal

mi_menu.add_cascade(label= "Archivo", menu = archivo)
mi_menu.add_cascade(label= "Editar", menu = editar)
mi_menu.add_cascade(label= "Seleccionar", menu= seleccionar)


ventana.mainloop()

