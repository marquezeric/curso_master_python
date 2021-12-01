valido=False

email=input("Intrduce tu email: ")
for i in range(len(email)):

	if email[i]=="@":
		valido=True

if valido:
	print("Email correcto")

else:
	print("Email no incorrecto")