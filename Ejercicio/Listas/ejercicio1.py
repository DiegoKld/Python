lista = [20, 50, "Curso", 'Python', 3.14]

print("La lista inicial inicial es: ", lista[0:])

P1 = input("Ingrese la palabra a remplazar en el campo 0")
P2 = input("Ingrese la palabra a remplazar en el campo 1")

lista[0] = P1
lista[1] = P2

print(lista)
