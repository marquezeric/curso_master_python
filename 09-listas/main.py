"""
LISTAS  (arrays)
Son colecciones o conjuntos de datos / valores, bajo un único
nombre.
Para acceder a esos valores podemos usar un índice númerico

"""
#pelicula = "Batman"

# Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
grupos = list(("Heroes","Zoe","Bunkers"))
years = list(range(2020,2050))
variada = ["Eric",45,1.67,True,"Texto"]

"""

print(peliculas)
print(grupos)
print(years)
print(variada)

"""
# Indices
# Modificar índices

peliculas[2] = "Yo robot"
peliculas[1] = "Transformers"
print(peliculas)
# Visualizar

print(peliculas[1])
print(peliculas[-2])
print(grupos[0:1])
print(peliculas[1:])

# Añadir elementos a listas

grupos.append("DLD")
grupos.append("La Maldita")
print(grupos)

# Recorrer lista
print("\n###### Listado de películas   ######")

for pelicula in peliculas:
    #print(pelicula)
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

"""
print("\n###### Listado de películas  agregar  ######")

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva película: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    #print(pelicula)
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

"""


# Ejercicio complementario

print("\n###### Listado de autos ######")

marcas_autos = ["volkswagen","chevrolet","suzuki","volvo","audi"]

print(marcas_autos)


# Listas MULTIDIMENSIONALES

print("\n###### Listado de contactos ######")

contactos = [
    [
    "Juan",
    "jrivera@gmail.com"
    ],    
    [
    "Ricardo",
    "rbuendia@gmail.com"
    ],
    [
    "Elmer",
    "emeza@gmail.com"
    ]

]

#print(contactos)
#print(contactos[1][1])


for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
#print(contacto[0])
#print(contacto[1])