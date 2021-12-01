#	Trabajo con paquetes
#	Carpeta calculo ------>Nombre del paquete
#	Archivo calculos_generales.py ------->Nombre del módulo
#	import dividir --------->Nombre de la función que queremos importar

#	Este archivo uso_modulos	se encuentra fuera de la carpeta calculo

#from calculos.calculos_generales import dividir
#	nombre del paquete, nombre del módulo 	nombre de la función

#from calculos.calculos_generales import potencia

# para importar todas las fuciones que contenga
from calculos.calculos_generales import *

from calculos.basicos.operaciones_basicas import *

from calculos.redondeo_potencia.redondeaYpotencia import *

sumar(5, 7)

dividir(4, 6)

potencia(5, 7)

redondear(4.8)
