"""
Proyecto Python
- Abrir asitente
- Login o registro
- Si elegimos registro, creará un usuario en la BD
- Si elegimos login, identificará al usuario y nos preguntará
- Crear notas, mostrar notas, borrarlas
"""
from usuarios import acciones

print("""
Acciones disponibles:
    -registro
    -login

""")
#  Primeras preguntas del asistente 105
hazEl = acciones.Acciones()

accion = input("Que quieres hacer?: ")


if accion == "registro":
    hazEl.registro()
   
elif accion == "login":
    hazEl.login()    

#  Primeras preguntas del asistente 106
