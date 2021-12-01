"""
1  Ventana
2  Tamaño fijo
3  No rredimensionble
4  Menu (Inicio, Añadir, Información, Salir)
4  Diferentes pantallas
5  Formulario de añadir productos
6  Guardar datos temporalmente
7  Mostrar datos listados en la pantalla Home
8  Opción de salir

"""

from tkinter import *
from tkinter import ttk

#  Definir ventana
ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(500, 500)
ventana.title("Proyecto Tkinter / Master en Python")
ventana.resizable(0,0)

#  Definir pantallas

def inicio():
    #  Montar pantalla
    #inicio_label=Label(ventana, text="Inicio")  #  No puede ir esta línea aquí
    inicio_label.config(
        fg="White",
        bg="Black",
        font=("Arial", 30),
        padx=200,
        pady=20
    )
    inicio_label.grid(row=0, column=0)
    
    products_box.grid(row=2)
    
    """
    #Listar productos que se vayan capturando
    for product in products:
        if len(product) == 3:
            product.append("agregado")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="----------------").grid()
    """
    for product in products:
        if len(product) == 3:
            product.append("agregado")
            products_box.insert('', 0, text=product[0], values=(product[1]))

    #  Ocultar pantalla
    anidar_label.grid_remove()
    anidar_frame.grid_remove()
    informa_label.grid_remove()
    acerca_label.grid_remove()
    """Sustituido por el frame
    anidar_name_label.grid_remove()
    anidar_name_entry.grid_remove()
    anidar_price_label.grid_remove()
    anidar_price_entry.grid_remove()
    anidar_descripcion_label.grid_remove()
    anidar_descripcion_entry.grid_remove()
    boton.grid_remove()"""

    return True
def anidar():
    #  Encabezado
    #anidar_label= Label(ventana, text="Anidar")  #  No puede ir esta línea aquí
    anidar_label.config(
        fg="White",
        bg="Black",
        font=("Arial", 30),
        padx=200,
        pady=20
    )
    anidar_label.grid(row=0, column=0, columnspan=10)

    #  Campos del formulario
    anidar_frame.grid(row=1)
    anidar_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    anidar_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    
    anidar_price_label.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    anidar_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    
    anidar_descripcion_label.grid(row=4, column=0, padx=5, pady=5, sticky=NW)
    anidar_descripcion_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
    anidar_descripcion_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )   
    anidar_separator.grid(row=5)
    #  Ubicación y Config del botón Guardar
    boton.grid(row=6, column=1, sticky=E)
    boton.config(
        bg="green",
        fg="white",
        padx=15,
        pady=5
    )

    #  Ocultar pantallas
    inicio_label.grid_remove()
    informa_label.grid_remove()
    acerca_label.grid_remove()
    products_box.grid_remove()

    #return True

def informa():
    #informa_label= Label(ventana, text="Informar")  #  No puede ir esta línea aquí
    informa_label.config(
        fg="White",
        bg= "Black",
        font=("Arial", 30),
        padx=200,
        pady=20
    )
    informa_label.grid(row=0,column=0)
    acerca_label.grid(row=1, column=0)

    #  Ocultar pantallas
    inicio_label.grid_remove()
    anidar_label.grid_remove()
    anidar_frame.grid_remove()
    products_box.grid_remove()
    """Sustituido por el frame
    anidar_name_label.grid_remove()
    anidar_name_entry.grid_remove()
    anidar_price_label.grid_remove()
    anidar_price_entry.grid_remove()
    anidar_descripcion_label.grid_remove()
    anidar_descripcion_entry.grid_remove()"""

    return True

#  Función para almacenar en variables temporales los productos
def anidar_product():
    products.append([
        name_data.get(),
        price_data.get(),
        anidar_descripcion_entry.get("1.0","end-1c")
    ])
    name_data.set("")
    price_data.set("")
    anidar_descripcion_entry.delete("1.0",END)

    #print(products)  # Solo para visualizar lo que vamos capturando
    inicio()

#  Variables importantes
products = []
name_data = StringVar()
price_data = StringVar()


#  Definir campos de pantallas Inicio---------------------------------
inicio_label=Label(ventana, text="Inicio")
#products_box = Frame(ventana, width=250)

Label(ventana).grid(row=1)
#Label(products_box).grid(row=0)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)

#  Definir campos de pantallas Añadir---------------------------------
anidar_label= Label(ventana, text="Añadir")

#  Campos del formulario-----------------------------------------------
anidar_frame=Frame(ventana)  #  Esto se agrega para evitar todas las sentencias de ocultar
anidar_name_label=Label(anidar_frame, text="Nombre: ")
anidar_name_entry=Entry(anidar_frame, textvariable=name_data)

anidar_price_label=Label(anidar_frame,text="Precio:")
anidar_price_entry=Entry(anidar_frame, textvariable=price_data)

anidar_descripcion_label=Label(anidar_frame, text="Descripción:")
anidar_descripcion_entry=Text(anidar_frame)
#  Separador entre ultimo campo y el botón
anidar_separator=Label(anidar_frame)
#  Botón Guardar
boton = Button(anidar_frame, text="Guardar", command=anidar_product)

#  Definir campos de pantallas Informar--------------------------------
informa_label= Label(ventana, text="Informar")
acerca_label=Label(ventana, text="Eric Márquez Salas")

#  cargar la pantalla de inicio

inicio()

#  Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=inicio)
menu_superior.add_command(label="Añadir", command=anidar)
menu_superior.add_command(label="Información", command=informa)
menu_superior.add_command(label="Salir", command=ventana.quit)
#  Cargar Menú
ventana.config(menu = menu_superior)

#  Cargar ventana
ventana.mainloop()