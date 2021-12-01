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
		self.__ruedas=4				#ENCAPSULACIÓN __ Indica que a variable no sea accesible desde el exterior de la CLASE pero si desde dentro de la propia CLASE
		self.__enmarcha=False
		
	def arrancar(self,arrancamos):	#Comportamiento - Método
		self.__enmarcha=arrancamos
		
		if(self.__enmarcha):
			return "El coche esta en marcha"

		else:
			return "El coche esta parado"

	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " Y un largo de ",	
		 self.__largoChasis)


misuzuki=Coche()	#Instancia de Clase		- 	Creación de primer Objeto

print(misuzuki.arrancar(True))	#	aquí se inserta el parámetro que necesita el método arrancar y también se imprime ya que el método arrancar trae string

misuzuki.estado()

print("-------------------A continuación creamos el segundo objeto-----------------")

michevy=Coche()		#Instancia de Clase		-	Creación de segundo objeto

print(michevy.arrancar(False))

michevy.ruedas=2	#	en caso de que no se especifique encapsulación esta linea cambiara la variable ruedas

michevy.estado()