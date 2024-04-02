"""
•	Ejercicio 3: Máximo común divisor (MCD)
Escribe una función recursiva que encuentre el máximo común divisor de dos números enteros utilizando el algoritmo de Euclides.
Luego, prueba tu función con diferentes pares de números.
"""

def mcd(a, b):
    if b == 0:
        return a #la funcion mcd primero se encarga de verificar si uno de los valores es 0, de ser asi, devolvera el otro valor"
    else:
        return mcd(b, a % b)
"""
de ningun valor ser 0, entra la funcion recursiva que toma b como su primer argumento y le resta la division entre A y B
repitiendo el proceso hasta que b = 0, cumpliendo con lo establecido en el algoritmo de Euclides
"""
num1 = 6
num2 = 0
print(f"El MCD de {num1} y {num2} es:", mcd(num1, num2))