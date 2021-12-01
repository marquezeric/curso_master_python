cantantes = ["2pac","Drake","Bad Buny","Julio Iglesias"]
numeros = [1,2,5,8,3,4]

# Ordenar Lista

print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos a Lista

cantantes.append("Natos y Waor")  #  Lo agrega al final de la lista
cantantes.insert(1, "David Bisbal")  #  Lo agrega en la posición exacta que defino de la lista

print(cantantes)

# Eliminar elementos a Lista

cantantes.pop(1)
cantantes.remove("Bad Buny")
print(cantantes)

# Dar la vuelta a elementos de Lista

print(numeros)
numeros.reverse()
print(numeros)

# buscar elementos dentro de una Lista

print("Eric" in cantantes)  # Solo busca, y si lo encuentra mostrara True o False

# Contar elementos de una Lista
print(cantantes)
print(len(cantantes))

# Cuantas veces aparece elementos en una Lista
numeros.append(8)
print(numeros.count(8))

# Conseguir un indice de una Lista

print(cantantes.index("Drake"))

# Unir Listas

cantantes.extend(numeros)
print(cantantes)