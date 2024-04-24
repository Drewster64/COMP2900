"""
•	Ejercicio 1: Suma de números naturales
Escribe una función recursiva que calcule la suma de los primeros n números naturales.
 Luego, prueba tu función con diferentes valores de n.
"""
def sumaNaturales(n):
    if n <= 0:
        return 0 #Ciclo busca si n es menor o igual a 0 para devolver el mismo. Este ciclo se utiliza posteriormente para devolver los valores obtenidos por la funcion recursiva y obtener la suma de todos
    else:
        return n + sumaNaturales(n-1) #Funcion recursiva que se encarga de sumar los numeros naturales, repitiendo el ciclo hasta llegar a 0
    
n = 12
print(f"La suma de los primeros {n} números naturales es: {sumaNaturales(n)}")
