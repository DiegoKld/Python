"""Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final"""

P1 = float(input("Ingrese el valor de la practica: \n1. "))
P2 = float(input("Ingrese el valor de la practica: \n2. "))
P3 = float(input("Ingrese el valor de la practica: \n3. "))

EP = float(input("Ingrese el valor del examen parcial: "))
EF = float(input("Ingrese el valor del examen final: "))

PP = (P1 + P2 + P3) / 3

PROM = (PP + (2*EP) + (3*EF)) / 6

print("El promedio parcial del estudiante es de:\n", PP,
      "\n Y el promedio final del estudiante es de:\n", PROM)
