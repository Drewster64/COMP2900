def busquedaBinaria(lista, valor):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2

        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            final = medio - 1

    return -1  

lista = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
objetivo = int(input("Escoja el valor de la lista que desea buscar: "))
resultado = busquedaBinaria(lista, objetivo)
if resultado != -1:
    print(f"El valor {objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El valor {objetivo} no se encuentra en la lista.")
