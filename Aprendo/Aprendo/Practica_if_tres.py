#	Eric Márquez Salas
#	Desarrollo de Aplicaciones
#	Octubre 2020
#	Programa utilizando If
print("Comparación de dos números")
num1=int(input("Introduce el primer número "))	# Solicitud del primer número y lo registrará en la variable num1
num2=int(input("Ahora introduce el segundo número "))	# Solicitud del primer número y lo registrará en la variable num2

def DevuelveMax(v1,v2):					#	Se declara la función "DevuelveMax" y se define que solicitará parámetros v1 y v2
										#	Observemos que los parámetros no son igual a las variables
	if v1<v2:
		print(v2)
	elif v2<v1:
		print(v1)
	else:
		print("Ambos números son iguales")

print("El número mayor es " )

DevuelveMax(num1,num2)
	
#	if num1>num2:
#		print("El número " + num1 " es mayor")
#	elif:
#		print("El número " + num2 " es mayor")
