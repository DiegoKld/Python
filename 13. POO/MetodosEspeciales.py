from email.errors import MalformedHeaderDefect


class FabricaTelefonos():
    def __init__(self, marca, color):#Constructor, carga todo al iniciar un objeto
        self.marca = marca 
        self.color = color
        print("el objeto {} ha sido creado".format(self.marca))

    #Este metodo genera una descripcion general de lo que se desee y asi al usar el metodo __del__ no se va a mostrar el espacio en memoria si no la anotacion que se deje ahi dentro
    def __str__(self):
        return "el objeto es {}".format(self.marca)

    #DESTRUCTOR
    def __del__(self):
        print("el objeto {} ha sido destruido".format(self.marca))

telefono = FabricaTelefonos("Nokia", "Negro")

print(telefono.marca)
print(telefono)