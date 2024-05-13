import random
def listaOrdenada(cantidad, minimo, maximo):
    lista = [random. randint(minimo, maximo) for _ in range(cantidad) ] #creacion de la lista desordenada
    print("lista desordenada: ", lista)
    lista.sort() #organizando la lista

    return lista
def busquedaBinaria(lista, objetivo):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2 
        elementoMedio = lista[medio]

        if elementoMedio == objetivo: #busqueda binaria para ubicar el numero deseado
            return medio
        elif elementoMedio < objetivo:
            inicio = medio + 1
        else:
            final = medio - 1

    return inicio

cantidad = 20
minimo =int(input("Ingrese desde que numero minimo desea que empiece en la lista: "))
maximo = int(input("Ingrese el numero maximo que desea que sea el ultimo en la lista: "))

listaNumeros = listaOrdenada(cantidad, minimo, maximo)
print("Lista de números ordenada:", listaNumeros)
buscar = int(input("Ingrese el numero que quiere buscar: "))
posicion = busquedaBinaria(listaNumeros, buscar)

if posicion != len(listaNumeros) and listaNumeros [posicion] == buscar:
    print(f"El numero {buscar} fue encontrado en la posicion {posicion} de la lista.")
else:
    print(f"El numero {buscar} no fue encontrado en la lista. Debería insertarse en la posicion {posicion} para mantener la lista ordenada.")