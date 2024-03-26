# Suma de todos los números enteros de 1 a un número determinado n.
# Enfoque 1: usando un ciclo for para recorrer todos los números
# de 1 a n y sumarlos
import timeit
def suma_for(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

result = suma_for(10)
time = timeit.timeit(lambda: suma_for(10), number=1)
print("La suma de los números del 1 al 10 es:", result) 
print('-----------------------------------------------------')
print("Tiempo tomado:", time, "segundos.")
