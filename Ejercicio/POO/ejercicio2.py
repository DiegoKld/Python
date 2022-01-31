""" Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora. """

class Calculadora():
    def __init__(self) -> None:
        self.num1 = int(input("Ingrese el primer numero: "))
        self.num2 = int(input("Ingrese el Segundo numero: "))
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multi(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2



calculadora = Calculadora()

print(calculadora.suma())