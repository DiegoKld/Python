class A():
    def __init__(self) -> None:
        self._cuenta = 0
        self._contador = 0

    @property   #Si pongo esta instancia el metodo lo voy a poder llamar como un atributo; es decir, sin los parentisis al final
    def cuenta(self):
        return self._cuenta

    @property
    def contador(self):
        return self._contador

a = A() #Creo el objeto " a " a partir de la clase " A() "

print(a.cuenta)
print(a.contador)
