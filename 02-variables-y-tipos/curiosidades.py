mi_texto="'Master'"       # También se puede poner comilla simple
#mi_texto=' "Master" '     #Así tambien puede ser
mi_texto2="en \"Python\" "   #si quieres poner comillas a tu string se usa diagonal invertida
#mi-texto3="Prueba de variable" #No se permite el guion como parte del nombre de variable
texto_unido=mi_texto+ " " +mi_texto2
print(texto_unido)

# Carácteres especiales

texto_unido=mi_texto+ " \n " +mi_texto2
print(texto_unido)

texto_unido=mi_texto+ " \t " +mi_texto2
print(texto_unido)

texto_unido=mi_texto+ " \r " +mi_texto2
print(texto_unido)