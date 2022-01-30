class Animales():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
#Resulta que en algunas ocaciones no se hereda completamente los atributos de una clase; es por eso que se debe usar la sentencia super(). y seguidamente lo que se desea heredar como en el caso que se muestra aca. No se debe olvidar que se hereda pero tambien se inicial el nombre nuevo que en este caso seria sonido
class Perro(Animales):
    def __init__(self, nombre, sonido) -> None:
        super().__init__(nombre)
        self.sonido = sonido

perro = Perro("Matias", "Dice guao guao")

print(perro.nombre)
print(perro.sonido)