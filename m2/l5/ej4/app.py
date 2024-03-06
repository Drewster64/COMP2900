# Promediar una lista de números:
#●	Función: promedio(lista_numeros)
#●	Parámetro: lista_numeros (lista de números)
#●	Devuelve: El promedio de la lista de números

def promedio(lista_numeros):
    # Suma de todos los números en la lista / Calcula la cantidad de números en la lista
    #divide entre ambos para dar el promedio
    return sum(lista_numeros) / len(lista_numeros)

numeros = [3, 7, 10, 16, 22] #Lista de números
resultado = promedio(numeros) #Llamando a la función para calcular el promedio de la lista de números
print("El promedio de la lista de números es:", resultado)