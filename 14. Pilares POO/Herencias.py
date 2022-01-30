#Crear dos clases y heredar de una a otra, pasar un atributo entre clases sin necesidad de volverlo a crear

class Animales(): #Clase padre
    def habla(self):
        print("Yo soy un animal como ud ")
    
    def descripcion(self):
        print("Yo soy un {} ".format(self.animal))

class Perro(Animales):#clase hija
    def Perro(self):
        pass

class Abeja(Animales):#clase hija
    
    def __init__(self, animal) -> None:
        self.animal = animal

animal = Animales()
animal.habla()

perro = Perro()
perro.habla()

abeja = Abeja("Abeja")
abeja.descripcion()