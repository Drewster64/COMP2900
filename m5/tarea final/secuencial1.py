"""	Ejercicio Básico: Implementa una función de búsqueda secuencial 
que tome una lista y un valor objetivo, y devuelva la posición del objetivo en la lista o -1 si no se encuentra.
def busqueda_secuencial(lista, objetivo): 
# Tu código aquí
"""
def busquedaSecuencial(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1

lista = [1, 2, 500, 2665, 55, 785, 552, 60]

buscar = int(input("Ingrese el número cuya posicion desea buscar en la lista: "))
resultado = busquedaSecuencial(lista, buscar)

if resultado != -1:
    print(f"El valor objetivo {buscar} se encuentra en la posicion {resultado} de la lista.")
else:
    print(f"El valor objetivo {buscar} no se encuentra en la lista.")
