# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

frase1 = input("Ingrese la frase 1: ")
frase2 = input("Ingrese la frase 2: ")

if len(frase1) < 3 or len(frase2) < 3:
    print("La palabra NO rima, tiene menos de 3 letras")

elif frase1[-3:] == frase2[-3:]:
    print("Las frases riman")

elif frase1[-2:] == frase2[-2:]:
    print("Las frases riman un poco")
else:
    print("Nada rima")
