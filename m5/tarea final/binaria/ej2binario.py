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

def Insercion(lista, valor): #esta funcion se encarga de iterar en la lista buscando un valor menor al insertado
    insercion = 0
    for i in range(len(lista)):
        if lista[i] < valor:
            insercion += 1 #al encontrar el valor menor, el numero insertado toma la posicion despues de este, incrementando en 1
    return insercion

lista = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 36]
objetivo = int(input("Escoja el valor de la lista que desea buscar: "))
resultado = busquedaBinaria(lista, objetivo)

if resultado != -1:
    print(f"El valor {objetivo} se encuentra en la posicion {resultado}.")
else:
    posicionNueva = Insercion(lista, objetivo)
    print(f"El valor {objetivo} debería insertarse en la posicion {posicionNueva} para mantener la lista ordenada.")
