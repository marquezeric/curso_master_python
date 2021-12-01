#	Los Diccionarios se insertaran dentro de llave {} pero tomando en cuenta que los datos se almacenan asociados a una clave
#	de tal forma que se crea una asociación de tipo "clave:valor" para cada elemento almacenado
#	El orden en que se ingresen los elemtos no importa
miDiccionario={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","España":"Madrid"}

print(miDiccionario["Francia"])		#	Para imprimir el valor de una clave se pondrá la clave entre []

print(miDiccionario)				# Imprimir todo mi diccionario

miDiccionario["Italia"]="Lisboa"	#	Agregar un elemento nuevo a nuestro diccionario (el error de la capital es a proposito)

print(miDiccionario)

miDiccionario["Italia"]="Roma"		#	Para corregir un valor que esta mal solo se sobreescribe

print(miDiccionario)

del miDiccionario["Reino Unido"]

print(miDiccionario)


miDiccionario2={"Alemania":"Berlín",23:"Jordan","Mosqueteros":3}

print(miDiccionario2)

miTupla=["España","Francia","Reino Unido","Alemania"]	#	Creamos una Tupla para la asignación de los valores al diccionario

miDiccionario3={miTupla[0]:"Madrid", miTupla[1]:"París", miTupla[2]:"Londres", miTupla[3]:"Berlín"} # asignar valores por medio de un diccionario a una tupla

print(miDiccionario3)

miDiccionario4={23:"Jordan","Nombre":"Micheal","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}	#	Para que un diccionario almacene una tupla

print(miDiccionario4)

print(miDiccionario4["anillos"]) #	Acceder a alguno de los valores del diccionario, tomamos el valor de la clave, mas no del valor {Clave:Valor}


miDiccionario5={23:"Jordan","Nombre":"Micheal","Equipo":"Chicago","anillos":{"temporada":[1991,1992,1993,1996,1997,1998]}}	#	Un Diccionario dentro de otro diccionario


print(miDiccionario5)

print(miDiccionario5.keys())	#	Uso de método keys, imprime los keys (claves)

print(miDiccionario5.values())	#	Uso del método values, imprime los valores

print(len(miDiccionario5))