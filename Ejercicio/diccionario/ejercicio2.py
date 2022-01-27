""" Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número

{

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

} """

diccionario = {

    1: "Casillas", 15: "Ramos",

    3: "Pique", 5: "Puyol",

    11: "Capdevila", 14: "Xabi Alonso",

    16: "Busquets", 8: "Xavi Hernandez",

    18: "Pedrito", 6: "Iniesta",

    7: "Villa"

}

NumeroJugador = int(input("Ingrese el numero del jugador a buscar: "))
""""
jugador = diccionario.get(NumeroJugador)

print("El jugador que busca se llama:\n{}".format(jugador))
"""

if NumeroJugador in diccionario:
    print("El jugador que busta es:\n{}".format(diccionario[NumeroJugador]))
else:
    print("No es un numero dentro del diccionario")
