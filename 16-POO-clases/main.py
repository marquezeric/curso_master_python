#  Programación orientada a objetos (POO o OOP)

#  Definir una clase (Molde para crear mas objetos de este tipo)
#  (Coche) con caracteristicas similares

class Coche:
    #  Atributos o propiedades (variables)
    #  Caracteristicas del coche
    color = "rojo"
    marca = "ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

#  Métodos, son acciones que hace el objeto (coche) (funciones)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

#  fin definición clase

print("-----------Coche 1---------------------------------------------")

coche = Coche()

coche.setColor("amarillo")  #  Cambiar mediante la asignación por parametro
coche.setModelo("Murcielago")  #  Cambiar mediante la asignación por parametro

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print("Velocidad final", coche.getVelocidad())

print("------------Coche 2------------------------------------------")

#  Crear mas objetos

coche2 = Coche()
coche2.setColor("Azul")
coche2.setModelo("Gallardo")
print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))
