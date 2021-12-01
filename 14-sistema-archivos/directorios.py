import os
import shutil

#  Crear carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Directorio ya existe")


#  Borrar Directorio

#os.rmdir('./mi_carpeta')

#  Copiar un Directorio

"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"

shutil.copytree(ruta_original, ruta_nueva)
"""
"""
os.rmdir('./mi_carpeta_COPIADA')

"""

#  Mostrar lo que contiene una carpeta

print("Contenido de mi carpeta")

contenido = os.listdir("./mi_carpeta")

print(contenido)

for fichero in contenido:
    print("Fichero: " + fichero)