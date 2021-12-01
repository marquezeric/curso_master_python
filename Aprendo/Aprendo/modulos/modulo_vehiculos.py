#	Manejo de herencia Simple	
#
class Vehiculos():
	
	def __init__(self,marca,modelo):	#Definimos el constructor
		
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ",self.modelo, "\nEn marcha: ",self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ",self.frena)

	#	Aplicación de la Herencia


class Furgoneta(Vehiculos):
	def carga(self,cargar):
		self.cargado=cargar
		if (self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"



class Moto(Vehiculos):	#Ahora tiene 6 métodos los que hereda de arriba mas el propio
	hcaballito=""	#Generamos un método
	def caballito (self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ",self.modelo, "\nEn marcha: ",self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ",self.frena, "\n", self.hcaballito)


class VElectricos():
	def __init__(self):
		self.autonomia=100
	def cargarEnergia(self):
		self.cargando=True 
