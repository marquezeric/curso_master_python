print("Asignaturas optativas año 2020")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()	#	funcion Lower convierte el texto introducido a minúculas 

if asignatura in("informatica gráfica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida " + asignatura)
else:
	print("La asignatura escogida no esta contemplada")