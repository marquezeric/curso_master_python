from coche import Coche

carro = Coche("Amarillo","Renault","Clio", 150, 200, 4)
carro1 = Coche("Azul","VolksWagen","Caribe", 155, 66, 4)
carro2 = Coche("Gris Plata","Chevrolet","Chevy", 155, 60, 5)
carro3 = Coche("Negro","Suzuki","SX4", 150, 120, 5)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

#  Detectar tipado

if type(carro) == Coche:
    print("Es un objeto correcto!!")
else:
    print("No es un objeto")

#  Visibilidad  Publico  o  Privado

print(carro.soy_publico)

#print(carro.__soy_privado)

print(carro.getPrivado())