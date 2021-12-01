print("Verificación de acceso")

nota_alumno=int(input("Introduce tu nota, por favor: "))

if nota_alumno<=5:
	print("Insuficiente")

elif nota_alumno<6:
	print("Suficiente")
							#	Funcionará como un solo bloque condicional
elif nota_alumno<7:
	print("Bien")

elif nota_alumno<9:
	print("Notable")

else:
	print("Sobresaliente")	#	Este else se ejecutará cuando ninguna de las condiciones anteriores se cumplan"

#	Recordar que no debe haber un else sin su correspondiente if
#	También un else le hace caso al if que tenga arriba de este
#	Cuando se desea utilizar Varios else, se debe utilizar elif
