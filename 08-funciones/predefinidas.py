"""
FUNCIONES PREDEFINIDAS

"""

nombre = "Eric Márquez"

#####   Funciones generales
print(nombre)

print(type(nombre))

#####   Detectar el tipado
comprobar = isinstance(nombre, str)

if comprobar:  #  Cuando no se le define algún valor, por default lo definira como True
    print("Esa variables es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un número con decimales")


#####   Limpiar espacios

frase = "      Hola Mundo"
print(frase.strip())


#####   Eliminar variables

year = 2021
print(year)
del year
#print(year)

#####   Comprobar variables vacías

texto = "   Mira Eric  "

if len(texto) <= 0:
    print("La variable está vacía")
else:
    print("La variable tiene contenido", len(texto))

print(len(texto))

#####   Encontar caracteres

frase = "La vida es bella"

print(frase.find("vida"))



#####   Reemplazar palabras en un string

nueva_frase = frase.replace("vida", "musica")
print(nueva_frase)

#####   Mayúsculas y Minúsculas

print(nombre)
print(nombre.upper())
print(nombre.lower())

#####   Funciones generales