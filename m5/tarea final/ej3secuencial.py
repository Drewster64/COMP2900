"""	
Crea un programa que genere una lista de números aleatorios y luego utilice la búsqueda secuencial
 para encontrar un número ingresado por el usuario.
"""   
import random

def lista100():
    with open("100.dat", "w") as f:
        for _ in range(100):
            numero = random.randint(1, 100)
            f.write(f"{numero}\n")

def busquedaSecuencial(file, objetivo):
    with open(file, "r") as archive:
        for linea in archive:
            if int(linea) == objetivo:
                return True
    return False

lista100()
buscar = int(input("Ingrese el número que desea buscar en la lista: "))
encontrado = busquedaSecuencial("100.dat", buscar)

if encontrado:
    print(f"El valor {buscar} está presente en la lista.")
else:
    print(f"El valor {buscar} no está presente en la lista.")

