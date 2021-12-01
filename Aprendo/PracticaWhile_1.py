edad=int(input("Introduce tu edad por favor: "))

while edad<=0 or edad >=100:
	print("Has introducido una edad incorrecta. Vuelve a intentarlo")
	edad=int(input("Introduce tu eadad por favor: "))

print("Gracias por colaborar. Puedes pasar")
print("edad del aspirante " + str(edad))
