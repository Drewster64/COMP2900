# Enfoque 2: Recorriendo la lista y comparando cada número con un valor 
# de referencia para encontrar el número más grande 
import timeit
def max_iterativo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

lista = [1, 2, 33, 48964, 55, 666, 7777, 8000, 900, 100]
maximo = max_iterativo(lista)
time = timeit.timeit(lambda: max_iterativo(lista), number=1)

print("Lista: ", lista)
print("El número más grande en la lista es:", maximo)
print('-----------------------------------------------------')
print("Tiempo tomado:", time, "segundos.")
