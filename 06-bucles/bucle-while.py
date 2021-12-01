"""
BUCLE WHILE
Estructura de control que itera o repite la ejecución de una
serie de instrucciones tantas veces como sea necesario, 
hasta que deje de cumplirse la condición

while condición:
    
    bloque de instrucciones
    
    actualización de contador

"""
contador = 1

while contador <= 100:
    print(f"Estoy en el número {contador}")
    contador += 1

print("---------------------------------------------------------")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)


print("\n##########  Ejemplo  #############")

numero_usuario = int(input("\n¿De que número quieres la tabla? "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n#### Tabla del número {numero_usuario}")

contador = 1
while contador <=10:
    print(f"{numero_usuario} X {contador} = {numero_usuario * contador}")

    contador += 1
else:
    print(f"Tabla del {numero_usuario} terminanda")


