"""9. Generar una lista de números aleatorios:
●	Función: generar_numeros_aleatorios(cantidad, minimo, maximo)
●	Parámetros: cantidad (de numeros), minimo y maximo (valores)
●	Devuelve"""

import random 
#La utilizacion de randint del modulo random nos permitirá obtener numeros aleatorios en el output

def generar_numeros_aleatorios(cantidad, minimo, maximo): #Definiendo función para generar una lista de números aleatorios

    randomNum = [random.randint(minimo, maximo) for _ in range(cantidad)]
    
    return randomNum

cantidad = int(input("Ingrese la cantidad de numeros aleatorios que desea generar: "))
minimo = int(input("Ingrese el valor mínimo: "))
maximo = int(input("Ingrese el valor máximo: "))

randomNumPr = generar_numeros_aleatorios(cantidad, minimo, maximo)
print("Lista de numeros aleatorios:", randomNumPr)
