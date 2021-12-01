#	Inicio de Programación Orientada a Objetos POO
#	En este ejemplo se definirá con un solo método arrancar y estado
#	Solo se debera pasar un parámetro

class Coche():
	#Propiedades
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enmarcha=False
	
	def arrancar(self,arrancamos):	#Comportamiento - Método
		self.enmarcha=arrancamos
		
		if(self.enmarcha):
			return "El coche esta en marcha"

		else:
			return "El coche esta parado"

	def estado(self):
		print("El coche tiene ", self.ruedas, " ruedas. Un ancho de ", self.anchoChasis, " Y un largo de ",	
		 self.largoChasis)
			

misuzuki=Coche()	#Instancia de Clase		- 	Creación de primer Objeto

print("El largo del coche es :", misuzuki.largoChasis)
print("El coche tiene :", misuzuki.ruedas, " ruedas")
print(misuzuki.arrancar(False))	#	aquí se inserta el parámetro que necesita el método arrancar y también se imprime ya que el método arrancar trae string

misuzuki.estado()


michevy=Coche()		#Instancia de Clase		-	Creación de segundo objeto

print("El largo del coche es :", michevy.largoChasis)
print("El coche tiene :", michevy.ruedas, " ruedas")
print(michevy.arrancar(False))

michevy.estado()