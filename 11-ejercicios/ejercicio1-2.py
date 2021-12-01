"""
Ejercicio 1. Hacer un programa que tenga una lista 
de 8 números enteros y haga lo siguiente:
- Recorrer la lista y mostrarla 
- Hacer función que recorra listas de números y devuelva un string 1-1
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algún elemento (que el usuario pida por teclado)

"""

# Recorrer y mostrar
print("\n###### Ordenar y Mostrar una lista #########")

numeros = [4,9,8,1,10,7,5,2,3,6]

print(numeros)
numeros.sort()
print(numeros)
print(len(numeros))

# Búsqueda en una lista
print("\n###### Búsqueda en una lista #########")

busqueda = int(input("Introduce un número: "))

comprobar = isinstance (busqueda, int)
while not comprobar or busqueda <= 0:  #  Mientras comprobar NO se cumpla o búsqueda sea menor o igual a cero
    busqueda = int(input("Introduce un número: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"Buscar en el lista el número {busqueda}")
search = numeros.index(busqueda)

print(f"El número búscado exite en la lista, es el índice {search}")