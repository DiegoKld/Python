#El encapsulamiento es aplicar sobre los atributos cierto alcance para que solo sea util dentro de la clase: siver para ahorrar memoria entre muchos otrs

class A():
    def __init__(self) -> None:
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador

a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())