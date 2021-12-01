class Persona():
	def __init__(self, nombre, edad, lugar_residencia):		#	Definir Constructor
	
		self.nombre=nombre
	
		self.edad=edad
	
		self.lugar_residencia=lugar_residencia

	def descripcion(self):
		
		print("Nombre: ", self.nombre, "Edad: ", self.edad,"Residencia: ", self.lugar_residencia)

class Empleado(Persona):	#	Hereda de Persona  PRINCIPIO DE SUSTITUCIÓN

	def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):	#	Definir Constructor de la clase empleado

		super().__init__(nombre_empleado,edad_empleado,residencia_empleado)

		self.salario=salario

		self.antigüedad=antigüedad

	def descripcion(self):
		super().descripcion()
		print("salario: ", self.salario, "Antiguedad: ", self.antigüedad)



#Eric=Persona("Eric",45,"Ciudad de México")		#	Creación de un objeto tipo Persona pasandole los tres parámetros

Eric=Empleado(1500,20,"Eric",45,"CD-MX")		#	Uso de la instrucción super()Creación de un objeto tipo Persona pasandole los tres parámetros

Eric.descripcion()	#	Se manda llamar al método descripción para que imprima

print(isinstance(Eric,Empleado))		#	isinstance nos indica si el objeto es una instancia