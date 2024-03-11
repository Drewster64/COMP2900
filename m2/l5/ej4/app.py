def promedio(lista_numeros):
    suma = 0
    cantidadNumeros = 0
    for numero in lista_numeros:
        suma += numero
        cantidadNumeros += 1
    return suma / cantidadNumeros

numeros = [3, 7, 10, 16, 22] 
resultado = promedio(numeros) 
print("Lista de numeros:", numeros)
print("El promedio de la lista de números es:", resultado)
