# Encontrar el número más grande en una lista de números.  
# Enfoque 1: Utilizando la función max() de Python para encontrar el  
# número más grande en una lista. 
import timeit
def max_lista(lista):
    return max(lista)

lista = [1, 2, 33, 48964, 55, 666, 7777, 8000, 900, 100]
maximo = max_lista(lista)
time = timeit.timeit(lambda: max_lista(lista), number=1)

print("Lista: ", lista)
print("El número más grande en la lista es:", maximo)
print('-----------------------------------------------------')
print("Tiempo tomado:", time, "segundos.")

