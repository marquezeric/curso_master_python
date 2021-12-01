"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto
"""

texto="Master en Python"
texto2="Con Víctor Robles"
numero=45
decimal=6.7

print("----------------------------------------------------------")

# Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

# Sustituir el valor de algunas variables / reasignando valores
numero=77
decimal=8.9
print(numero)
print(decimal)

print("-----------------------------------------------------------")

# Concatenación
nombre="Eric"
apellido="Márquez"
web="wordpress.emarquez.com"

print(nombre, apellido, web)    # En esta línea no concatena solo esta recibiendo las variables

print(nombre + " " + apellido + " - " + web)

print(f"{nombre} {apellido} - {web}")

print("Hola mi nombre es: {} {} y mi web es: {}".format(nombre,apellido,web))