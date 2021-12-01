"""
try:

    nombre = input("Introduce tu nombre: ")
    #print(nombre)

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, introduce bien el nombre")

else:
    print("Todo ha funcionado correctamente")

finally:
    print("Fin de la iteración")

"""
#  Multiples excepciones

"""
try:

    numero = int(input("Introduce un número para elevarlo al cuadrado "))
    print("El cuandrado es: " + str(numero * numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros en el código")
#except ValueError:
#   print("Introduce un número correcto")
except Exception as error:
    print(type(error))
    print("Ha ocurrido un error: ", type (error).__name__)

"""

#  Excepciones personalizadas o lanzar excepción

try:
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <=1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al Master en Python {nombre} !!")
except ValueError:
    print("Introduce los datos correctamente!!")
except Exception as e:
    print("Existe un error: ", e)