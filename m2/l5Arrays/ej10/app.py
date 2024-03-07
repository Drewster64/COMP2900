"""
10. Rotar los elementos de un arreglo:
●	Crea un arreglo con números.
●	Rota los elementos del arreglo una posición a la derecha.
●	Imprime el arreglo con los elementos rotados.
"""
numeros =  [1, 2, 3, 4, 5, 6, 355, 37, 2895, 916, 20015]
print("Lista original de elementos del arreglo:", numeros)

numeros = numeros[-1:] + numeros[:-1]

"""
-1: hace que el ultimo elemento del arreglo se archive en una lista 
:-1 hace que el resto de los elementos del arreglo se archiven en otra lista 
al sumarlos se invierten en orden, dando como resultado que se hayan visto rotados hacia la derecha
"""

print("Lista del arreglo con los elementos rotados:", numeros)
