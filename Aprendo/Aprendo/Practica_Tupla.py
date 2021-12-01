miTupla=("Juan",13,1,1995,9)	#	La tupla es similar a una lista, solo que la tupla no es modificable y se realiza con () o sin paréntesis
								#	de igual manera comienza con el indice 0
								#	También se puede definir sin paréntesis, aunque no es reconmedable y se denomina empaquetado de tupla
miLista=list(miTupla)		#	Con la instrucción list convertimos a nuestra tupla en una lista
miTupla=tuple(miLista) 		#	Con la intrucción "tuple" se hace una conversión, ya sea de Tupla a Lista o  Lista a Tupla

print(miTupla[0])
print(miTupla)
print(miLista)
print("Eric" in miTupla)	#	la instrucción "in" le preguntamos a la Tupla si es que contiene un elemento indicado
print(miTupla.count(9))		# 	La instrución "count"  nos permite saber cuantas veces se encuentra un elemento indicado
print(len(miTupla))			#	La instrucción "len" muestra la longitud de nuestra tupla (Cuantos elementos contiene)
							#	, iniciando con 1 y no con 0
miTupla2=("Eric",)			#	Tupla unitaria

print(miTupla2)

							#	Desempaquetado de Tupla
							#	Cuando queremos asignar los valores de nuestra tupla a unas variables dadas
miTupla3=("Eric",9,"Agosto",1975)	#	Nuestra Tupla
nombre,dia,mes,agno=miTupla3
print(nombre)
print(dia)
print(mes)
print(agno)
print(miTupla3.index("Eric"))	#	En versiones anteriores no se permite preguntar por indice, como en las listas

print(miTupla3.index("Agosto"))	#	También se puede resalizar búsqueda por índice, al igual que las listas