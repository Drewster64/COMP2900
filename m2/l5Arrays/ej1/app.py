"""
1. Sumar los elementos de un arreglo:
●	Crea un arreglo con números.
●	Recorre el arreglo y suma cada elemento.
●	Imprime la suma total.
"""

numeros = [6, 7, 8, 9, 10,32,55,89] # Definimos un arreglo con numeros

sumaTotal = 0 #Variable para almacenar la suma

for elemento in numeros: #Sumar los elementos del arreglo
    sumaTotal += elemento

print("La suma total de los elementos del arreglo es:", sumaTotal, ":)")
