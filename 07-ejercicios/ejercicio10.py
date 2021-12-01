"""
EJERCICIO 10
El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuantos han reprobado

"""
""" 
----------------------------Solución Emarquez--------------------
contador = 0

while contador < 16:

    calificacion = int(input("Introduce la primera calificacion"))
        
    if calificacion <= 5:
        print("Reprobrado")
    else:
            print("Aprobado")
    contador += 1
--------------------------------------------------------------------
"""
"""
----------------------------Solución Víctor Robles------------------

"""

"""
contador = 1
aprobados = 0
reprobados = 0

numero_alumnos = int(input("¿Cuántos alumnos tienes?: "))

while contador <= numero_alumnos:
    calificación = int(input(f"Que calificación pondrás al \"alumno {contador}\"? "))
    if calificación >= 6:
        aprobados += 1
    else:
        reprobados += 1
    contador += 1
print(f"\nTotal de alumnos aprobados {aprobados}")
print(f"Total de alumnos aprobados {reprobados}")


"""

"""

---------------------------------EJERCICIO COMPLEMENTARIO----------------------------------------------

REALIZAR UN PROGRAMA QUE CAPTURE el ARTÍCULO DE LA DESPENSA A COMPRAR Y SUME 
CADA UNO DE LOS PRODUCTOS, PARA QUE AL FINAL MUESTRE EL TOTAL GENERAL

"""
articulo = 0
caltot = 0
precio_total = 0

while articulo < 5:
    
    caltot = int(input("Ingresa el precio del articulo comprado: "))
    
    articulo += 1
    
    precio_total += caltot

    print(f"Total por pagar es: {precio_total}")