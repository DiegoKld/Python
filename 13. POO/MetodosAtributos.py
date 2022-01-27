#un metodo no es mas que una funcion dentro de una clase
#Un metodo va a realizar una accion

class FabricaTelefonos():#clase
    #atributos
    marca = "Huawei"
    color = "Negro"
    ram = 32
    almacenamiento = 128

    #asi se declara un metodo de instancia
    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando musicas")




telefono = FabricaTelefonos() #objeto
#Este objeto puede tener acceso a distintos atributos
telefono.marca#atributo
print(telefono.marca)

print(telefono.llamar("Hola, donde esta el mundo"))
telefono.escucharMusica()