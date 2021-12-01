"""
Una función es un conjunto de instrucciones agrupadas bajo 
un nombre concreto, que pueden reutilizarse invocando a
la función tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES


¿Como se invocan las funciones?
    R= Solamente se hace el llamado de la función

nombreDeMiFuncion(parametros):

"""

# Ejemplo 1

print("###############  Ejemplo 1  #################")

def muestraNombre():
    print("Eric Márquez")
    print("Juan Rivera")
    print("Ricardo Buendia")
    print("Elmer Meza")
    print("Ricardo Torres")
    print("Jorge Zamudio")

# Invocar función tantas veces como sea necesario
muestraNombre()
#muestraNombre()
#muestraNombre()

"""
# Ejemplo 2 Parámetros

print("###############  Ejemplo 2  #################")

def mostrarTuNombre(nombre,edad):

    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Ya eres Mayor de edad")
    else:
        print("No eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

mostrarTuNombre(nombre, edad)

"""
# Ejemplo 3 Parámetros

print("###############  Ejemplo 3  #################")

def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")

    for contador in range(11):
        operacion = numero * contador

        print(f"{numero} X {contador} = {operacion}")

tabla(4)

# Ejemplo 3.1  solamente realizamos otro for pero ahora para que intere sobre lo 

print("\n###############  Ejemplo 3.1  #################")

for numero_tabla in range(1,11):
    tabla(numero_tabla)



# Ejemplo 4

print("\n###############  Ejemplo 4 #################")

# Parametros opcionales

def getEmpleado(nombre, dni = None):  #  para asignar un parámetro opcional este debe tener valor None o False
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    
    if dni != None:
        print(F"DNI: {dni}")

getEmpleado("Eric Márquez Salas", "MASE7508091Y8")


# Ejemplo 5

print("\n###############  Ejemplo 5 #################")

# Ejemplo Return o devolver datos

def saludame(nombre):
    saludo = f"Hola, saludos !!! {nombre}"

    return saludo

saludame("Eric Márquez Salas")  #  Llamado a la función introduciendo el parametro de nombre

print(saludame("Eric Márquez Salas"))  #  Para imprimir la función introduciendo el parametro


# Ejemplo 6

print("\n###############  Ejemplo 6 #################")

# Ejemplo de calculadora básica

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2


    cadena = ""
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena

print(calculadora(5,5, True))



#  Ejemplo 7

print("\n###############  Ejemplo 7 #################")

# Funciones dentro de otras funciones

def getNombre(nombre):
    texto = f"El nombre es: {nombre} "
    return texto

def getApellidos(apellidos):
    texto = F"Los apellidos son: {apellidos} "
    return texto

def devuelveTodo(nombre,apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Eric", "Marquez Salas"))


#  Ejemplo 8

print("\n###############  Ejemplo 8 #################")

# Funciones Lambda funcón anonima, no tiene nombre, no hace falta definirla, pequeñas

dime_el_year = lambda year: f"El año es {year * 20}"

print(dime_el_year(2034))
