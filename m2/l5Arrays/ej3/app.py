"""
Invertir el orden de los elementos de un arreglo:
●	Crea un arreglo con números.
●	Invierte el orden de los elementos del arreglo.
●	Imprime el arreglo con el orden invertido.
"""

numeros = [355, 37, 2895, 916, 20015]

numeros_invertidos = []

longitud = 0
for _ in numeros: # Obtiene la longitud de la lista
    longitud += 1

for i in range(longitud - 1, -1, -1):
    numeros_invertidos.append(numeros[i]) #los -1 permiten reorganizar los valores en orden

print("Lista de numeros original:", numeros)
print("Lista de numeros con el orden invertido:", numeros_invertidos)

