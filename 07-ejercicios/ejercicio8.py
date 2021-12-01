"""
EJERCICIO 8
¿Cuanto es el N por ciento de X número?
                20 %  de  150


"""
numero = int(input("Introduce el número: "))
porcentaje = int(input(f"introduce el porcentaje que quieres sacar a {numero} "))
resultado = (numero * (porcentaje / 100))
print(f"El %{porcentaje} de {numero} es {resultado} ")