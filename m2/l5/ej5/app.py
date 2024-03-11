# Encontrar el índice de la primera aparición de un elemento en una lista:
#●	Función: encontrar_indice(lista, elemento)
#●	Parámetros: lista (lista) y elemento (valor a buscar)
#●	Devuelve: El índice de la primera aparición del elemento en la lista, o -1 si no se encuentra

def buscar_indice(lista, elemento):
    indice = 0
    for item in lista:
        if item == elemento:
            return indice
        indice += 1
    return -1

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
buscarElemento = int(input("Ingrese el elemento que desea buscar en la lista 1-15: "))

indice = buscar_indice(numeros, buscarElemento)
if indice != -1:
    print("El índice de la primera aparición del elemento", buscarElemento, "en la lista es:", indice)
else:
    print("El elemento", buscarElemento, "no se encuentra en la lista.")
