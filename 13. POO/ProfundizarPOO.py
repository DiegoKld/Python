class FabricaTelefonos():
    def __init__(self, marca, *colores, **modelos) -> None:#marca = atributo, colores= tupla, modelos=diccionario
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Alcatel", "Negro", "azul", m1 = 590, m2 = 300)

print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)

#atributos temporales, solo se atribuye al objeto. Si se crea otro objeto y se le pide memoria no va a pasar nada por que es algo local que se creo para ese objeto
telefono.memoria = 512

print(telefono.memoria)