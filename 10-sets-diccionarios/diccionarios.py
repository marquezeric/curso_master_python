"""
Diccionario:
Almacena un conjunto de datos, pero con indice alfanumerico
En formato clave > valor
Es parecido a un array asociativo o un objeto Json

"""

persona = {
    "nombre": "Víctor",
    "apellidos": "Robles",
    "web": "victorrobles.es"
}

print(persona)
print(type(persona))
print(persona["web"])  #  Imprimir el indice específicado


# Lista con diccionarios

contactos = [
    {
        'nombre':'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
        'nombre':'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre':'Salvador',
        'email': 'salvador@salvador.com'
    }
]

print(contactos[1]['email'])  #  Imprimir un contacto, pero definiendo el indice

contactos[0]['nombre'] = "Antoñito"
print(contactos[0]['nombre'])

print("\n######  Listado de contactos  #######")

print("------------------------------------------------")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("------------------------------------------------")