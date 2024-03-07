"""
Buscar un elemento en un arreglo:
●	Crea un arreglo con números.
●	Busca un elemento específico en el arreglo.
●	Imprime la posición del elemento encontrado o un mensaje si no se encuentra.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#El usuario ingresa el numero que desea buscar
elemento = float(input("Ingrese el número del 1-15 cuya posicion desea buscar: "))

posicion = -1
for i in range(len(numeros)):
    if numeros[i] == elemento:
        posicion = i
        break

if posicion != -1:
    print("Lista de elementos:", numeros)
    print("El elemento", elemento, "se encuentra en la posición", posicion)
else:
    print("Lista de elementos:", numeros)
    print("El elemento", elemento, "no se encuentra en la lista.")

