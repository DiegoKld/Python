#Modificacion de metodos cuando se heredan de otra clase
 
class Animales():#Esta va a ser la clase padre, aca se crea el constructor y ademas se crea cada uno de los metodos que se van a pasar a las clases hijas como herencia, si vemos el init se envia un mensaje y ese mensaje se pasa por el metodo hablar y ese metodo hablar se puede heredar y modificar en cada una de las clases que lo necesiten
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

#Modificacion del metodo hablar
class Perro(Animales):
    def hablar(self):
        print("Yo hago guao!")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo soy un pez")

perro = Perro("Guaoee") #Esto no lo imprime por que es una clase Hija que se esta modificando en la clase Perro
perro.hablar()

gato = Animales("Yo hago miau!!!")#Este si imprime el mensaje por que se envia directamente a la clase padre
gato.hablar()

pez = Pez("Hola pez")#No se imprime el mensaje aca ya que es una clase hija de Animales y ddentro de la clase Pez se modifica el metodo hablar. Por eso se imprime lo que se indico en el metodo hablar dentro de la clse PEZ que a su vez depende de lo que le pidio a Animales
pez.hablar()




        
