"""
Invertir el orden de los elementos de un arreglo:
●	Crea un arreglo con números.
●	Invierte el orden de los elementos del arreglo.
●	Imprime el arreglo con el orden invertido.
"""

numeros = [355, 37, 2895, 916, 20015]

numeros_invertidos = list(reversed(numeros)) #metodo reversed permite invertir los valores

print("Lista de numeros original:", numeros)
print("Lista de numeros con el orden invertido:", numeros_invertidos)
