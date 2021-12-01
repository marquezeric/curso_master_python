"""
EJERCICIO 7
Hacer un programa que muestre todos los números impares
entre dos número que decida el usuario

"""

valor_1 = int(input("Introduce el primer valor "))
valor_2 = int(input("Introduce el segundo valor valor "))

if valor_1 < valor_2:
    
    for contador in range(valor_1, valor_2 + 1):
        if contador % 2 == 0:
            print(f"{contador} es par")
        else:
            print(f"{contador} es impar")




else:
    print("El primer valor debe ser mayor al segundo valor")