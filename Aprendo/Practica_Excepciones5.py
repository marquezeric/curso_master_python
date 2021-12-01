def evaluaEdad(edad):
		
	if edad<0:
		raise TypeError("No se permiten edades negativas")	#Lanzamiento de excepción

	if edad<20:
		return "Eres muy Joven"
	elif edad<40:
		return "Eres Joven"
	elif edad<65:
		return "Eres maduro"
	elif edad<100:
		return "Cuídate..."

print(evaluaEdad(45))