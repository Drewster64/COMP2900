"""
. Ordenar los elementos de un arreglo de menor a mayor:
●	Crea un arreglo con números.
●	Ordena los elementos del arreglo de menor a mayor.
●	Imprime el arreglo ordenado.
"""
numeros = [355, 37, 2895, 916, 20015]
print("Lista de elementos:", numeros)

n = 0 
for b in numeros:
    n += 1

i = 0
while i < n:
    O = i + 1 #evita que los elementos se comparen con ellos mismos
    while O < n:
        if numeros[i] > numeros[O]: #si los numeros de i son mayor a O, se intercambian
            numeros[i], numeros[O] = numeros[O], numeros[i]
        O += 1
    i += 1

print("Lista ordenada de menor a mayor:", numeros)


"""
numeros = [355, 37, 2895, 916, 20015]
print("Lista de elementos:", numeros)
numeros.sort() #Funcion sort permite organizarlas de menor a mayor
print("Lista ordenada:", numeros)
"""

