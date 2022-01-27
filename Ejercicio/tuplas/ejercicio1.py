"""" Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla """

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

mes = int(input("Ingrese el numero de mes a buscar:\n"))

print("El mes que ud busca es: {}".format(meses[mes-1]))
