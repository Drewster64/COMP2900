import timeit

def busquedaBinaria(file, objetivo):
    with open(file, "r") as f:
        file = [int(line.strip()) for line in f]  #esta parte del codigo ayuda a ir linea por linea para traer la lista del archivo y guardarla como "file" para que la busqueda binaria pueda procesarla

    inicio = 0
    final = len(file) - 1
    while inicio <= final:
        medio = (inicio + final) // 2 
        elementoMedio = file[medio]

        if elementoMedio == objetivo: 
            return medio
        elif elementoMedio < objetivo:
            inicio = medio + 1
        else:
            final = medio - 1

    return -1

buscar = int(input("Ingrese el número que desea buscar en la lista del archivo: "))

encontrado = busquedaBinaria("casoMedio.dat", buscar)
tiempo = timeit.timeit(lambda: busquedaBinaria("casoMedio.dat", buscar), number=1)

if encontrado != -1:
    print(f"El valor {buscar} está presente en la lista del archivo.")
else:
    print(f"El valor {buscar} no está presente en la lista del archivo.")
print(f"El tiempo de ejecucion: {tiempo}")
