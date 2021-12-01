"""
EJERCICIO 5
Hacer un programa que muestre todos los números entre dos números 
que diga el usuario

"""

valor_1 = int(input("Introduce el primer número: "))
valor_2 = int(input("Introduce el segundo número: "))

if valor_1 < valor_2:

    for contador in range(valor_1, (valor_2 + 1)):

        print(contador)

else:
    print("El primer número de ser menor al segundo número")