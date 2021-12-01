"""
EJERCICIO 9
Hacer un programa que pida números al usuario
indefinidamente hasta meter el número 111

"""
contador = 1
while contador < 111:
    valor = int(input("Introduce el valor que quieras:"))
    
    if valor == 111:
        break
    print(f"Has introducido el número {valor}")
