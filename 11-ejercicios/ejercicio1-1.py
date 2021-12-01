"""
Ejercicio 1. Hacer un programa que tenga una lista 
de 8 números enteros y haga lo siguiente:
- Recorrer la lista y mostrarla 
- Hacer función que recorra listas de números y devuelva un string 1-1
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algún elemento (que el usuario pida por teclado)

"""
#######  Función que recorre lista de números y devuelve un string  #####

# Recorrer y mostrar
print("###### Función que recorre y muestra una lista #########")
numeros = [9,8,1,9,7,5,2,0]  #  Definición de la lista

def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    
    return resultado

print(mostrarLista(numeros))  #  En este caso le pasamos el parámetro numeros, arreglo
print(mostrarLista(["Juan","Ricardo","Elmer","Ricardo","Eric"]))  #  Definimos nuevos parámetros en lista
numeros.sort()
print(mostrarLista(numeros))