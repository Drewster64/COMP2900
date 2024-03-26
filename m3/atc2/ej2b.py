# Enfoque 2: fórmula matemática para calcular la suma de  
# una serie aritmética 
import timeit
def suma_formula(n): 
    return (n * (n+1)) // 2 

result = suma_formula(10)
time = timeit.timeit(lambda: suma_formula(10), number=1)
print("La suma de los números del 1 al 10 es:", result) 
print('-----------------------------------------------------')
print("Tiempo tomado:", time, "segundos.")

