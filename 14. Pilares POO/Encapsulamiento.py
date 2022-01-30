#El encapsulamiento es aplicar sobre los atributos cierto alcance para que solo sea util dentro de la clase: siver para ahorrar memoria entre muchos otrs

class A():
    def __init__(self) -> None:
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador

class B():
    def __init__(self) -> None:
        self.__contador = 0 #Con el guion bajo "_" se esta encapsulando el atributo para que solo pueda ser usado dentro de la clase

    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador

print("Objeto1 ")
a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)#se puede usar el atributo por que no esta encapsulado

print("Objeto2 ")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador)#Me tira error debido a  que el atributo esta encapsulado
