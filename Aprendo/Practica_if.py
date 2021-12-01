def evaluacion(nota):	#	Definición de la función evaluar con aceptación de un parametro llamado "estado"
	valoracion="Aprobado"
	if nota<=5:		#	Si el parametro es menor o igual a 5
		valoracion="Suspenso"
	return valoracion
print(evaluacion(5))	#Llamado a ejecutar la función evaluar