# Enfoque 2: usando la función index() 
import timeit
def search_index(number, numbers):
    try:
        return numbers.index(number)
    except ValueError:
        return -1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

buscarNumero = int(input("Ingrese el número del 1-10 que desea buscar: "))
result = search_index(buscarNumero , numbers)
tiempo = timeit.timeit(lambda: search_index(buscarNumero, numbers), number=1)

if result != -1:
    print(f"El número {buscarNumero} ha sido encontrado en la lista.")
else:
    print(f"El número {buscarNumero} no ha sido encontrado en la lista.")

print('-----------------------------------------------------')
print("Tiempo tomado:", tiempo, "segundos.")
