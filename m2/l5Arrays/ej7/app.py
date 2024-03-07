"""
7. Calcular el promedio de los elementos de un arreglo:
●	Crea un arreglo con números.
●	Calcula el promedio de los elementos del arreglo.
●	Imprime el promedio.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

promedio = sum(numeros) / len(numeros)
#Sum suma los elementos y len cuenta la cantidad de elementos que hay, se divide entre ambos para sacar el promedio

print("Lista de elementos:", numeros)
print("El promedio de los elementos del arreglo es:", promedio)
