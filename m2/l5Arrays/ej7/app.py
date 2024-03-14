"""
7. Calcular el promedio de los elementos de un arreglo:
●	Crea un arreglo con números.
●	Calcula el promedio de los elementos del arreglo.
●	Imprime el promedio.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Lista de elementos:", numeros)
deleteNum = int(input("Ingrese el elemento que desea eliminar del arreglo: "))

posicion = -1 #Almacena el elemento escogido

counter = 0
for numero in numeros:
    if numero == deleteNum:
        posicion = counter 
    counter  += 1

if posicion != -1:
    nuevos_numeros = []
    counter = 0
    for numero in numeros:
        if counter != posicion:
            nuevos_numeros.append(numero)
        counter += 1
    numeros = nuevos_numeros

    print("El elemento", deleteNum, "fue eliminado del arreglo.")
    print("Lista de elementos actualizada:", numeros)
else:
    print("El elemento", deleteNum, "no se encuentra en la lista de elementos")

"""
******************************Con funciones especiales**********************************

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

promedio = sum(numeros) / len(numeros)
#Sum suma los elementos y len cuenta la cantidad de elementos que hay, se divide entre ambos para sacar el promedio

print("Lista de elementos:", numeros)
print("El promedio de los elementos del arreglo es:", promedio)
"""
