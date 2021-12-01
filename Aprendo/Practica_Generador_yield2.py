#	Eric Márquez
#	Desarrollo de Aplicaciones
#	Programa que genera numeros
#	pares pero ahora utilizando yield
def generapares(limite):

	num=1

	while num<limite:

		yield num*2

		num=num+1


devuelvepares=generapares(10)

print(next(devuelvepares))

print(next(devuelvepares))

print(next(devuelvepares))