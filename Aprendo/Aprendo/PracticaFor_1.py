email=False

miemail=input("Introduce tu dirección de email: ")

for i in miemail:
	
	if (i=="@"):

		email=True

if email==True:
	print("Email es correcto")
else:
	print("Email no es correcto")