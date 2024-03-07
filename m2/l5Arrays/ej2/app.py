"""
Encontrar el máximo elemento de un arreglo: 
●	Crea un arreglo con números.
●	Recorre el arreglo y guarda el máximo elemento encontrado.
●	Imprime el máximo elemento.
"""

numeros = [355, 37, 2895, 916, 20015]

maximo = numeros[0] #variable para almacenar el maximo elemento

for elemento in numeros:
    if elemento > maximo:
        maximo = elemento

print("El máximo elemento del arreglo es:", maximo)
