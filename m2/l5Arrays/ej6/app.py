"""
6. Contar la cantidad de apariciones de un elemento en un arreglo:
●	Crea un arreglo con números.
●	Cuenta la cantidad de veces que aparece un elemento específico en el arreglo.
●	Imprime la cantidad de apariciones del elemento.
"""
numeros = [2, 22, 59, 33, 33, 66, 156, 33]

print("Arreglo de Numeros:", numeros)
countNum = int(input("Ingrese el elemento que desea contar en el arreglo de numeros: "))

counter = 0 

for numero in numeros:
    if numero == countNum:
        counter+= 1

if counter == 1:
    print("El elemento", countNum, "aparece una vez en el arreglo de numeros.")
else:
    print("El elemento", countNum, "aparece", counter, "veces en el arreglo de numeros.")

