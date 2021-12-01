miLista=["Juan","Ricardo",22,"Elmer",20,"Eric",9]	#	Lista Original puede almacenar números y caracteres o variables
													#	Recordar que las listas o arrays inician desde 0 has ... n

print(miLista[:])	#	Leer todos los elementos del arreglo
print(miLista[2])	#	Leer solo un elemento específico 
print(miLista[0:3])	# 	leer solo una porción de la lista, dejando al ultimo elemento excluido
print(miLista[-3])	# 	Lee desde el último, pero no cuenta desde cero
print(miLista[:2])	# 	Python entiende que debe tomar desde el elemento 0
print(miLista[1:])	# 	Lee a partir del elemento 2 hasta el final de la lista

		#	Agregar elementos a la lista
miLista.append("Jorge")	#	Agregará mi elemento nuevo , pero al final

print(miLista[:])

miLista.insert(4,"Ricardo")	#	Agregará mi elemento en el índice 4 

print(miLista[:])

miLista.extend(["Mario","Carlos","Jaime"])	#	Agregar elementos de una la lista a lista original

print(miLista[:])

print(miLista.index("Eric"))	#	Indica que posición dentro de la lista tiene el elemento indicado

print("Eric" in miLista)		#	Pregunta dentro de la lista si se encuentra el elemento solicitado

miLista.remove("Eric")			#	Remueve el elemento indicado de la lista "Texto" cuando el elemento
miLista.remove(9)				#	cuando es numerico el elemento se debe de poner solo el número
print(miLista[:])

miLista.pop()					#	Elimina de la lista al ultimo elemento


miLista2=["Antonio","Fernando","Felipe"]	#	Segunda Lista para unir a la lista original

miLista3=miLista+miLista2			#	Creamos miLista3 que va alojar la suma de miLista + miLista2

print(miLista3[:])					#	Imprimimos miLista3

milista4=["basketbol","futbol","beisbol","voleybol"] * 3 #	se triplica la milista4

print(milista4)