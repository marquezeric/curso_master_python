#----Función sin return la operación se realiza
#----pero al no tener "return" no se muestra el resultado
def sumar(num1,num2):
	
	print(num1+num2)

sumar(10,1)
#----Función Suma
print('Función suma')
def suma(num1, num2):
	
	resultado=num1+num2

	return resultado
#Lleva doble parentesis por que llamamos a la función propia de Python print() y llamamos a nuestra función suma() creada por nosotros
print(suma(5,7))
	
print(suma(2,3))


print(suma(35,358))


#----Función Resta
print('Función Resta')
def resta(num1,num2):

	resultado=num1-num2

	return resultado
print(resta(25,5))


#----Función Multiplicación
print('Función Multiplicación')
def multiplicacion(num1, num2):
	
	resultado=num1*num2

	return resultado

print(multiplicacion(2,2))


palabra="Python"
print(palabra[0:2])
