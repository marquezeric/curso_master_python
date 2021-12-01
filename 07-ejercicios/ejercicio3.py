"""
EJERCICIO 3
    Escribir dos programas que muestren los cuadrados
    (Números multiplicados por si mismo) de los 60 primeros
    números naturales. Resolverlo con los bucles for y while

"""
"""
print("\n########## Ejercicio con FOR ##########")

for contador in range(61):  # 61 por que nuestro rango lo comienza a leer desde 0
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")


"""
"""
print("\n########## Ejercicio con WHILE ##########")

contador = 0

while contador <= 60:
    cuadrado = contador * contador
    
    print(f"El cuadrado de {contador} es {cuadrado}")
    
    contador += 1
"""
print("\n########## Ejercicio extra con WHILE ##########")
kilometraje = 5000

while kilometraje <= 45000:
    print(f"print {kilometraje}")
    kilometraje += 1000
    if kilometraje == 30000:
        print("Mantenimiento mayor")