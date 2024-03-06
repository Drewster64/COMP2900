# Encontrar el índice de la primera aparición de un elemento en una lista:
#●	Función: encontrar_indice(lista, elemento)
#●	Parámetros: lista (lista) y elemento (valor a buscar)
#●	Devuelve: El índice de la primera aparición del elemento en la lista, o -1 si no se encuentra

def buscar_indice(lista, elemento):
    return lista.index(elemento) if elemento in lista else -1 #método index para encontrar el indice en la lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
buscarElemento = int(input("Ingrese el elemento que desea buscar en la lista: "))

#Busca el índice del elemento en la lista utilizando la función
indice = buscar_indice(numeros, buscarElemento)
print("El indice de la primera aparición del elemento", buscarElemento, "en la lista es:", indice)
