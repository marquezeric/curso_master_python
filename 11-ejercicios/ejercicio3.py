"""
Ejercicio 3
Programa que compruebe si una variable esta vacía 
y se está vacía rellenarla con texto en minúsculas y mostrarlo
en mayúsculas.

"""
texto = ""

if len(texto.strip()) <= 0:

    texto = "Hola soy un texto en minúsculas"
    # mostrar el texto
    print(texto.upper() + " y la variable esta vacía")

else:
    print(f"La variable tiene texto  {texto}")
    