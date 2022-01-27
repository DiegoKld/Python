# Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son:
# candidato A por el partido rojo,
# candidato B por el partido verde,
# candidato C por el partido azul.
# Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

# Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula


print("Elija su candidato favorito\n")
opcion = input(
    "OPRIMA:\nA) Partido rojo: \nB) Partido verde: \nC) Partido azul:\n")

opcion1 = opcion.upper()

if opcion1 != "A":
    print("No ingreso una opcion valida")

elif opcion1 == "A":
    print("Eligio partido rojo")

elif opcion1 == "B":
    print("Eligio partido Verde")

elif opcion1 == "C":
    print("Eligio partido Azul")

else:
    print("Esta opcion NO existe")
