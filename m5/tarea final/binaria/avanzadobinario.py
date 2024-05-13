import random
def lista20(file, cantidad):
    with open(file, "w") as f:
        numeros_unicos = random.sample(range(1, 21), cantidad)  #primera funcion se encarga de crear un archivo con una lista aleatoria de 20 numeros
        for numero in numeros_unicos:
            f.write(f"{numero}\n")

def selection_sort(lista):
    n = len(lista)
    for i in range(n):#el algoritmo de ordenamiento selection sort se encarga de ordenarlos en orden ascendente
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

def busquedaBinaria(lista, valor):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2 #funcion de busqueda binaria para encontrar el numero deseado por el usuario

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


file = "20Num.dat"
cantidad = 20 #cantidad de numeros agregados a la lista
lista20(file, cantidad)

with open(file, "r") as file:
    lista = [int(linea) for linea in file]

print("Lista original:")
print(lista)
selection_sort(lista)
print("Lista ordenada por el algoritmo de Selection Sort:")
print(lista)

buscar = int(input("Ingrese el número que desea buscar en la lista: "))
resultado = busquedaBinaria(lista, buscar)

if resultado < len(lista) and lista[resultado] == buscar:
    print(f"El valor {buscar} esta en la lista.")
else:
    posicionNueva = Insercion(lista, buscar)
    print(f"El valor {buscar} debería insertarse en la posicion {posicionNueva} para mantener la lista ordenada.")
