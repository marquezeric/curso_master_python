"""
Variables Locales: Se definen dentro de la función y no se pueden usar
fuera de ella, solo están disponibles dentro.
A no se que hagamos un Return.

Variables Globales: Son las que se declaran fuera de una función
y están disponibles dentro y fuera de ellas.

"""

frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase = "Hola Mundo!!!"
    print("Dentro de la función: ")
    print(frase)

    year = 2021
    print(year)
    
    global website  #  Declaración de variable global dentro de una función
    website = "wordpress.emarquez.com"
    print("Dentro de la función", website)

    #return f"Dato devuelto es {year}"  #  Es lo mismo
    return "Dato devuelto  es " + str(year)

print(holaMundo())

print("Fuera de la función", website)
