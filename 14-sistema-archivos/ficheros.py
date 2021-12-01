from io import open
import pathlib
import shutil #  módulo que sirve para copiar archivos



#  Abrir Archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta,"a+")


#  Escribir en Archivo

archivo.write("* Soy un texto introducido desde Python #######\n")


#  Cerrar Archivo  #  Cada archivo que se abra se debe de cerrar

archivo.close()


#  Abrir Archivo Solo Lectura

ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta,"r+")

#  Leer contenido
"""
contenido = archivo_lectura.read()
print(contenido)

"""
#  Leer contenido y guardarlo en una lista

lista = archivo_lectura.readlines()
archivo_lectura.close()

#print(lista)

#  Recorrer el archivo

for frase in lista:
    print("---", frase)

#  Copiar archivo
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"

shutil.copyfile(ruta_original, ruta_nueva)
"""
#  Mover Archivo
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)

"""
#  Eliminar Archivo
"""
import os

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

os.remove(ruta_nueva)

"""

#  Comprobar si existe  achivo

import os.path

#print(os.path.abspath("./"))
ruta_coprobar = os.path.abspath("./") + "/fichero_texto.txt"
print(ruta_coprobar)

if os.path.isfile(ruta_coprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")
    

