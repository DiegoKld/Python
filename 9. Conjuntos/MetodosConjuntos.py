conjunto = {1, 2, 3, 4, 5}

print(conjunto)
conjunto.add(20)
print(conjunto)

conjunto.remove(4)
print(conjunto)

# pop toma un elemento al azar del conjunto y lo elimina
conjunto.pop()
print(conjunto)

# añade elementos iterables
conjunto.update([1, 2, 3])
print(conjunto)

# deja el conjunto vacio
conjunto.clear()
print(conjunto)
