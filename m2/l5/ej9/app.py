"""9. Generar una lista de números aleatorios:
●	Función: generar_numeros_aleatorios(cantidad, minimo, maximo)
●	Parámetros: cantidad (de numeros), minimo y maximo (valores)
●	Devuelve"""

import random

def generar_numeros_aleatorios(cantidad, minimo, maximo):
    randomNum = []
    for _ in range(cantidad):
        numero_aleatorio = random.random() * (maximo - minimo) + minimo
        randomNum.append(int(numero_aleatorio))
    return randomNum

cantidad = int(input("Ingrese la cantidad de números aleatorios que desea generar: "))
minimo = int(input("Ingrese el valor mínimo: "))
maximo = int(input("Ingrese el valor máximo: "))

randomNumPr = generar_numeros_aleatorios(cantidad, minimo, maximo)
print("Lista de números aleatorios:", randomNumPr)

