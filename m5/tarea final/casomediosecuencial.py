"""
Mejor medio de busqueda secuencial: lista de 50,000 numeros 
"""
import timeit
def busquedaSecuencial(file, objetivo):
    with open(file, "r") as archivo:
        for linea in archivo:
            if int(linea.strip()) == objetivo:
                return True
    return False

buscar = int(input("Ingrese el número que desea buscar en la lista del archivo: "))

encontrado = busquedaSecuencial("casoMedio.dat", buscar)
tiempo = timeit.timeit(lambda: busquedaSecuencial("casoMedio.dat", buscar), number=1)

if encontrado:
    print(f"El valor {buscar} está presente en la lista del archivo.")
else:
    print(f"El valor {buscar} no está presente en la lista del archivo.")
print(f"El tiempo de ejecucion: {tiempo}")
