"""
SET Es un tipo de dato, para tener una colección de valores,
pero no tiene ni indice ni orden

"""

personas = {
    "Víctor",
    "Manolo",
    "Francisco"
}

personas.add("Paco")
personas.remove("Francisco")

print(type(personas))
print(personas)

