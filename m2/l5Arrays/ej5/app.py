"""
5. Eliminar un elemento de un arreglo:
●	Crea un arreglo con números.
●	Elimina un elemento específico del arreglo.
●	Imprime el arreglo con el elemento eliminado.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Lista de elementos:", numeros)
deleteNum = int(input("Ingrese el elemento que desea eliminar del arreglo: "))

posicion = -1
counter = 0
for numero in numeros:
    if numero == deleteNum:
        posicion = counter
    counter += 1

if posicion != -1: # Verifica si el elemento a eliminar esta en la lista
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

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Lista de elementos:", numeros)
deleteNum = int(input("Ingrese el elemento que desea eliminar del arreglo: "))

if deleteNum in numeros:
    numeros.remove(deleteNum) #funcion remove permite eliminar el numero escogido por el usuario del arreglo
    print("El elemento", deleteNum, "fue eliminado del arreglo.")
    print("Lista de elementos actualizada:", numeros)
else:
    print("El elemento", deleteNum, "no se encuentra en la lista de elementos")
"""
