class A():
    def __init__(self) -> None:
        self._contador
        self._uenta = 0

    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador
        
a = A()

#Si miran un guion bajo no llamar a modificar el atributo; esto como buena practica de programacion