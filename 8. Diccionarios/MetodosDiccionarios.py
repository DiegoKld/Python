diccionario = {1: 2, 2: 3, 3: 4}
# Para eliminar el parametro de la llave que queramos
print(diccionario)
diccionario.pop(3)
print(diccionario)

# limpiar el diccionario completo
diccionario.clear()
print(diccionario)

# buscar un valor especifico
diccionario = {1: 2, 2: 3, 3: 4}
diccionario2 = {4: 5, 6: 7}
print(diccionario.get(2))

# recibe el valor de la llave y su valor y lo agrega

diccionario.setdefault(4, 5)
print(diccionario)

# actualizar valores recibe otro diccionario

diccionario.update(diccionario2)
print(diccionario)
