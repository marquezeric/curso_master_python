
print("Programa de evaluación de notas de alumnos")			#Imprime mensaje de inicio

nota_alumno=input("Introduce la nota del Alumno: ")	#Entrada de dato **Muy importante** Pyton toma todo dato
															#introducido por input como string
def evaluacion(nota):
	calificacion="Aprobado"
	if nota<=5:
		calificacion="Reprobado"
	return calificacion


print(evaluacion (int(nota_alumno)))	#Se hace uso de la función "int" para convertir el dato introducido a numerico 