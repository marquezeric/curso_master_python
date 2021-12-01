"""
EJERCICIO 6
Mostrar todas las tablas de multiplicar del 1 al 10
Mostrando el título de la tabla y luego las multiplicaciones del 1 al 10

"""

for tabla in range (1, 11):
    print("##############################")

    print(f"###### Tabla {tabla} #######")
  
    print("##############################")
        
    for numero in range(1, 11):
        print(f"\n{tabla} x {numero} = {tabla * numero}")