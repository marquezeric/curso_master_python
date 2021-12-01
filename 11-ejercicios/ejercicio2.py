"""
Realizar un programa que añada valores a una lista 
mientras que su longitud sea menor a 120 y luego mostrar la lista
Usar While y for

"""
"""
coleccion = []

for contador in range(120):
    coleccion.append(f"{contador}")
    print(f"Mostrando el :" + coleccion[contador])

print(coleccion)  #  Imprime todos los elementos agregadodos
print(coleccion[23])  #  Si deseamos visualizar algún índice en especial

"""

#####################    Con while    #####################

coleccion = []
x = 0

while x <= 120:
    coleccion.append(f"{x}")
    print(f"Mostrando el :" + coleccion[x])

    x += 1

print(coleccion)
