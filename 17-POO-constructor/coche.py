class Coche:
    #  Atributos o propiedades (variables)
    #  Caracteristicas del coche
    color = "rojo"
    marca = "ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 4

    soy_publico = "Hola soy un atributo publico"

    __soy_privado = "Hola Soy un atributo privado"  #  Cuando un atributo se inicia con doble guión bajo, este será privado

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


#  Métodos, son acciones que hace el objeto (coche) (funciones)
    def getPrivado(self):  #  Cuando se desea obtener un atributo privado
        return self.__soy_privado

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca   

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):

        Info = "----------- Información del coche ------------------"

        Info += "\n Color: " + self.getColor()
        Info += "\n Marca: " + self.getMarca()
        Info += "\n Modelo: " + self.getModelo()
        Info += "\n Velocidad: " + str(self.getVelocidad())

        return Info
        


#  fin definición clase
