""" Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno """

class Fabrica():
    def __init__(self,llanta, color, precio) -> None:
        self.llanta = llanta
        self.color = color
        self.precio = precio

class Carro(Fabrica):
    def datos(self):
        print("La cantidad de llanatas del carro es: {}".format(self.llanta))
        print("El color del carro es: {}".format(self.color))
        print("El precio del carro es: {}".format(self.precio))

class Moto(Fabrica):
    def datos(self):
        print("La cantidad de llantas de la moto es: {}".format(self.llanta))
        print("El color de la moto es: {}".format(self.color))
        print("El precio de la moto es: {}".format(self.precio))

moto = Moto(2, "Negro", 5000000)
carro = Carro(4, "Gris plata", 40000000)

moto.datos()
carro.datos()


