# Enfoque 1: usando un ciclo for 
import timeit
def search_for(number, numbers):
    for i in range(len(numbers)):
        if numbers[i] == number:
            return 1
    return -1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

buscarNumero = int(input("Ingrese el número del 1-10 que desea buscar: "))
result = search_for(buscarNumero , numbers)
tiempo = timeit.timeit(lambda: search_for(buscarNumero, numbers), number=1)

if result == 1:
    print(f"El número {buscarNumero} ha sido encontrado en la lista.")
elif result == -1:
    print(f"El número {buscarNumero} no ha sido encontrado en la lista.")

print('-----------------------------------------------------')
print("Tiempo tomado:", tiempo, "segundos.")