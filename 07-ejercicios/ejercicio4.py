"""
EJERCICIO 4
Pedir dos números al usuario y hacer todas las operaciones 
básicas de una calculadora y mostrarlo en pantalla

"""
numero_1 = int(input("Ingresa el primer número "))
numero_2 = int(input("Ingresa el segundo número "))

print(f"\nLa suma de estos dos números es: {numero_1 + numero_2}")
print(f"\nLa resta de estos dos números es: {numero_1 - numero_2}")
print(f"\nLa multiplicación de estos dos números es: {numero_1 * numero_2}")
print(f"\nLa división de estos dos números es: {numero_1 / numero_2}")

print("############  Otra solución  ################")

print("\nLa suma: " + str(numero_1 + numero_2))
print("\nLa resta: " + str(numero_1 - numero_2))
print("\nLa multiplicación: " + str(numero_1 * numero_2))
print("\nLa división: " + str(numero_1 / numero_2))