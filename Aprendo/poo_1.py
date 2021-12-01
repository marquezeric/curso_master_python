#Inicio de Programación Orientada a Objetos POO

class Coche():
	#Propiedades
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enmarcha=False
	
	def arrancar(self):	#Comportamiento - Método
		self.enmarcha=True


	def estado(self):
		if (self.enmarcha):
			return "El coche esta en marcha"

		else:
			return "El coche esta parado"

misuzuki=Coche()	#Instancia de Clase		- 	Creación de primer Objeto

print("El largo del coche es :", misuzuki.largoChasis)
print("El coche tiene :", misuzuki.ruedas, " ruedas")
misuzuki.arrancar()

print(misuzuki.estado())


michevy=Coche()		#Instancia de Clase		-	Creación de segundo objeto

print("El largo del coche es :", michevy.largoChasis)
print("El coche tiene :", michevy.ruedas, " ruedas")

print(michevy.estado())