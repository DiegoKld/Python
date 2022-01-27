vocal = input("Ingrese una vocal: \n")

"""if vocal == "a":
    print("Esto es una vocal")
elif vocal == "e":
    print("Esto es una vocal")
elif vocal == "i":
    print("Esto es una vocal")
elif vocal == "o":
    print("Esto es una vocal")
elif vocal == "u":
    print("Esto es una vocal")
else:
    print("Esto no es una vocal")"""

if vocal.lower() in "aeiou":
    print("Esto es una vocal")
else:
    print("Esto NO es una vocal")
