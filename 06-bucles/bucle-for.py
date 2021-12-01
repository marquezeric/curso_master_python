"""
for variable in elemento_iterable: (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""
contador = 0
resultado = 0
for contador in range (0, 10):
    print("Voy por el " + str(contador))

    #resultado = resultado + contador
    resultado += contador
print(f"El resultado es {resultado}")

# Ejemplo con tablas de multiplicar

print("\n###############  Ejemplo ##################")

numero_usuario = int(input("De que número quieres la tabla de multiplicar?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n#### Tabla de multiplicar del número {numero_usuario} ####")

for numero_tabla in range(0, 11):

    if numero_usuario == 45:
        print("No se pueden multiplicar números prohibidos !!")
        break

    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario * numero_tabla}")

else:
    print("Tabla finalizada")

for numero_tabla in range(0, 11):
    print(f"{numero_tabla}")