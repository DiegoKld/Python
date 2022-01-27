NumInt = int(input("Ingrese un numero entero: \n"))

if(NumInt < 0):
    NumIntAux = NumInt*-1
    print("El valor absoluto de {} es {}".format(NumInt, NumIntAux))
else:
    print("El numero no tiene valor absoluto ya que es positivo")
