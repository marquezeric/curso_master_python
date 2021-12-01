"""
# Condicional IF

SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecuta otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones

Operadores de comparación

== es igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

Operadores lógicos

and Y
or  O
!   negación
not NO

"""

# Ejemplo 1

print("##############  EJEMPLO 1  ######################")

#color = input("Adivina cual es mi color favorito: ")
color = "rojo"

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("Color equivocado")


# Ejemplo 2

print("\n##############  EJEMPLO 2  ######################")


year =2020

#year = int(input("¿En que año estamos? "))

if year < 2021:
    print("Estamos antes de 2021 !!")
else:
    print("Es un año posterior a 2021")

# Ejemplo 3

print("\n##############  EJEMPLO 3  ######################")

nombre = "Eric Marquez"
ciudad = "México"
continente = "Oceanía"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad ")

    if continente != "Americano":
        print("El usuario no es Americano")
    else:
        print(f"es Americano y de {ciudad}")

else:
    print(f"{nombre} NO es Mayor de edad")

# Ejemplo 4

print("\n##############  EJEMPLO 4  ######################")
dia = 2
#dia = int(input("Introduce el día de la semana: "))
"""
if dia == 1:
    print("Es Lunes")
else:
    if dia == 2:
        print("Es Mártes")
    else:
        if dia == 3:
            print("Es Miércoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
                else:
                    if dia == 6:
                        print("Es Sábado")
                    else:
                        if dia == 7:
                            print("Es Domingo")
"""
if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Mártes")
elif dia == 3:
    print("Es Miércoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
elif dia == 6:
    print("Es Sábado")
elif dia == 7:
    print("Es Domingo")
else:
    print("Fin de semana")


# Ejemplo 5

print("\n##############  EJEMPLO 5  ######################")

edad_minima = 18
edad_maxima = 65
edad_oficial = 17
 
#edad_oficial = int(input("Introduce tu edad: "))
if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")

# Ejemplo 6

print("\n##############  EJEMPLO 6  ######################")

pais = "España"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana!!")
else:
    print(f"{pais} no es un país de habla hispana")


# Ejemplo 7

print("\n##############  EJEMPLO 7  ######################")

pais = "Mexico"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un país de habla hispana!!")
else:
    print(f"{pais} SI es un país de habla hispana")


    # Ejemplo 8

print("\n##############  EJEMPLO 8  ######################")

pais = "Rusia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un país de habla hispana!!")
else:
    print(f"{pais} SI es un país de habla hispana")