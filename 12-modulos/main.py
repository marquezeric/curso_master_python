"""
Modulos: Son funcionalidades ya hechas para reutilizar.
En Python hay muchos módulos, que los puedes consultar aquí:
https://docs.python.org/3/py-modindex.html

Podemos consegui modulos que ya vienen en el lenguaje,
módulos enn internet y también podemos crear nuestros módulos

"""

#import mimodulo  #  Se importan todas las funciones que contiene mi archivo
#from mimodulo import holaMundo  #  Se importa exlcusivamente la función deseada
from mimodulo import *

#print(mimodulo.holaMundo("Eric Márquez"))
print(holaMundo("Eric Márquez"))  #  Y solo se hace el llamado a 

#print(mimodulo.calculadora(9,7,True))
print(calculadora(9,7,True))

# Módulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)

print(fecha_completa.year)

print(fecha_completa.month)

print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S ")

print("Mi fecha personalizada",fecha_personalizada)

print(datetime.datetime.now().timestamp())

print(datetime.datetime.now().time())



# Módulo Matemáticas

import math

print("La raíz cuadrada de 10", math.sqrt(10))

print("Número Pi: ", float(math.pi))

print("Redondear a la alza: ", math.ceil(6.67854))

print("Redondear a la baja: ", math.floor(6.67854))

# Módulo Random

import random

print("Número aleatorio", random.randint(15,67))

