for letra in "Python":
	
	if letra == "h":
		continue				#	La instrucción continue omite la h y la función print no la imprimira	
		
	print("Viendo la letra: " + letra)


#####	Contar el número de caracteres que tiene una variables

nombre= "Pildoras Informaticas"	#	Se asigna valor a la variable nombre

contador=0				#	Se inicializa la variable contador en cero

for i in nombre:		#	Inicio del ciclo for
	
	if i==" ":			#	Condición
		continue
	contador+=1					#	Incrementa la variable contador de 1 en 1
	# contador=contador=1
print(contador)				#	La función len lee cuantos caracteres tiene la variable nombre, recordar que toma en cuenta los espacios

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ut suscipit ex. Fusce nec nunc condimentum, faucibus ligula sed, interdum tortor. Proin et lobortis tortor, eu finibus justo. Sed dapibus volutpat neque, quis convallis enim ultrices id. Pellentesque ac odio congue, tempus massa vel, tempus nunc. Donec et ex ultrices, placerat lectus tincidunt, varius diam. Sed mattis nulla efficitur mi vehicula, in gravida tellus viverra. Aliquam dignissim porttitor facilisis. Mauris id elementum purus. Donec vulputate lacinia velit vitae consequat. Mauris tincidunt tortor a ligula imperdiet, a porta arcu elementum. Nunc et nunc ac enim lacinia laoreet quis nec felis. Suspendisse potenti. "
cuenta=0
for i in texto:
	if i ==" ":
		continue
	cuenta+=1
	pass
print(cuenta)

parrafo=("Suspendisse vulputate accumsan magna sed iaculis. Aliquam non quam ipsum. Vivamus vitae magna enim. Nulla finibus, est sit amet aliquet imperdiet, enim justo mollis metus, a dictum lacus ipsum et orci. Suspendisse lobortis enim sit amet nulla scelerisque, sit amet commodo erat feugiat. Donec ultrices venenatis tellus ac tincidunt. Proin rhoncus lectus in tellus varius fermentum nec quis nibh. Maecenas sapien nulla, dignissim pretium sagittis in, volutpat a dolor. Phasellus accumsan sollicitudin condimentum. Donec a velit sed mauris tincidunt fringilla. Phasellus iaculis convallis purus et placerat. Nam et euismod urna, nec posuere ex. Aenean ac leo euismod, tristique tortor sit amet, aliquam libero. Aliquam erat volutpat. In in nisi a est molestie feugiat.")
contar=0
for i in parrafo:
	if i ==" ":
		continue
	contar+=1
print("El parrafo siguiente: " + parrafo)
print("Contiene " + str(contar) + " caracteres")