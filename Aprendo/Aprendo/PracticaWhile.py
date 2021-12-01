i=1

while i<=10:					#	Esta condición siempre se cumple por consiguiente el bucle se puede volver infinito
	print("Ejecución" + str(i))

	i=i+1						#	Sin este contador nuestro bucle se volverá infinito
								#	La primera vez que lo lee, a i le sumará 1 de tal manera que i será 2 y 
								#	así sucesivamente.

print("Terminó la ejecución")