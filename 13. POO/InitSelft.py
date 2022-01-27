"""class FrabricaTelefonos():
    marca = "Samsung"

    def ElaborarHuawei(self):#Nos permite engoblar atributos a toda la clase
        self.marca = "Huawei"

telefono = FrabricaTelefonos()

telefono.ElaborarHuawei()
print(telefono.marca)
"""

class FabricaTelefonos():
    def __init__(self, marca, color):#Constructor, sirve para iniciarse al construir un objeto
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos('Huawei',"Negro")

print(telefono.marca)
print(telefono.color)

