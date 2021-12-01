#	Inicio de Programación Orientada a Objetos POO
#	En este ejemplo se define un CONSTRUCTOR, el cual definira el estado inicial
#	 de los objetos que perteneceran a una clase
#	CONSTRUCTOR ES UN MÉTODO ESPECIAL QUE LE DA ESTADO INICIAL A LOS OBJETOS
#	También usamos la encapsulación __ con doble sublínea

class Coche():

	def __init__(self):				#	Declaración de nuestro Constructor
		#Propiedades
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4				#ENCAPSULACIÓN de propiedades __ Indica que a variable no sea accesible desde el exterior de la CLASE pero si desde dentro de la propia CLASE
		self.__enmarcha=False
		
	def arrancar(self,arrancamos):	#Comportamiento - Método
		self.__enmarcha=arrancamos
		
		if (self.__enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo):
			return "El coche esta en marcha"

		elif(self.__enmarcha and chequeo==False):
			return"Algo a ido mal en el chequeo. No podemos arrancar"

		else:
			return "El coche esta parado"

	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " Y un largo de ",	
		 self.__largoChasis)



	def __chequeo_interno(self):
		print("Realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"
		self.refrigerante="ok"

		if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas" and self.refrigerante=="ok"):
			
			return True

		else:
			return False



misuzuki=Coche()	#Instancia de Clase		- 	Creación de primer Objeto

print(misuzuki.arrancar(True))	#	aquí se inserta el parámetro que necesita el método arrancar y también se imprime ya que el método arrancar trae string

misuzuki.estado()

#print(misuzuki.__chequeo_interno())	# Si no está encapsulado el método chequeo_interno se podrá acceder desde fuera de la clase al método chequeo_interno

print("-------------------A continuación creamos el segundo objeto-----------------")

michevy=Coche()		#Instancia de Clase		-	Creación de segundo objeto

print(michevy.arrancar(True))

michevy.estado()

#print(michevy.__chequeo_interno())	# Si no está encapsulado el método chequeo_interno se podrá acceder desde fuera de la clase al método chequeo_interno