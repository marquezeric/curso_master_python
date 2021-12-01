# La herencia es la posibilidad de compartir atributos y métodos
# entre clases. Y que diferentes clases hereden de otras

class Persona:
    """
    nombre =
    apellidos =
    edad =

    """

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminado"

    def dormir(self):
        return "Estoy durmiendo"

#  Fin de la definición de mi clase

class Informatico(Persona):
    """
    lenguajes
    experiencia

    """
    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def reparar(self):
        return "He reparado tu PC"


class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__()  # Para heredar otro constructor
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15
    
    def auditorio(self):
        return "Estoy auditando una red"