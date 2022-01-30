#Metodo para modificar y colocar valores

class A():
    def __init__(self) -> None:
        self._cuenta = 0
        self._contador = 0

    @property   #Si pongo esta instancia o decorador el metodo lo voy a poder llamar como un atributo; es decir, sin los parentisis al final
    def cuenta(self):
        return self._cuenta

    @cuenta.setter # Este decorador me permite llamar al metodo como atributo; pero para modificar los valores que hay dentro
    def cuenta(self, cuenta):
        self._cuenta = cuenta

    @property
    def contador(self):
        return self._contador

    @contador.setter
    def contador(self, contador):
        self._contador = contador

a = A() #Creo el objeto " a " a partir de la clase " A() "

print(a.cuenta)
a.cuenta = 20
print(a.cuenta)
print(a.contador)

a.contador = 10

print(a.contador)

#En cada codigo se puede tener el metodo GET y SET, puede faltar el metodo SET y ser un codigo de solo lectura, pero el que nunca puede faltar, es el metodo GET