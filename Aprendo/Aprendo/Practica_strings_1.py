#	Uso de la función isdigit, insertando un while
#	después de que el usuario inserta la edad

edad=input("Introduce la edad: ")

while edad.isdigit()==False:

	print("Por favor, introduce un valor númerico")

	edad=input("Introduce la edad: ")	
	pass

if (int(edad)<18):
	print("No puedes pasar")
else:
	print("Puedes pasar")