"""
6. Contar la cantidad de apariciones de un elemento en un arreglo:
●	Crea un arreglo con números.
●	Cuenta la cantidad de veces que aparece un elemento específico en el arreglo.
●	Imprime la cantidad de apariciones del elemento.
"""
numeros = [2, 22, 59, 33, 33, 66, 156, 33]

# Pedimos al usuario que ingrese el elemento que desea contar
print("Arreglo de Numeros:", numeros)
countNum = int(input("Ingrese el elemento que desea contar en el arreglo de numeros: "))

veces = numeros.count(countNum) #Funcion count permite contar el elemento en la cadena del arreglo
if (veces == 1): 
    print("El elemento", countNum, "aparece", veces, "vez en el arreglo de numeros.")
else:
    print("El elemento", countNum, "aparece", veces, "veces en el arreglo de numeros.")

