#	Eric Márquez
#	Desarrollo de Aplicaciones
#	Programa que genera numeros
#	pares pero ahora utilizando yield
def devuelve_ciudades(*ciudades):	#El asterisco  significa que recibira un determimnado número de argumentos y en forma de tupla
	for elemento in ciudades:		#Bucle padre
		#for subElemento in elemento:
			yield from elemento



ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
