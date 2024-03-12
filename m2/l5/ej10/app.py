"""
10. Contar la cantidad de apariciones de una letra en una cadena de texto:
●	Función: contar_apariciones_letra(cadena, letra)
●	Parámetros: cadena (texto a analizar) y letra (letra a buscar)
●	Devuelve: La cantidad de apariciones de la letra en la cadena de texto
"""

def contar_apariciones_letra(cadena, letra):
    counter = 0
    for caracter in cadena:
        if caracter.lower() == letra.lower():
            counter += 1
    return counter

cadena = input("Ingrese una cadena de texto: ")
letra = input("Ingrese la letra que desea buscar: ")
cantidad = contar_apariciones_letra(cadena, letra)
print("La cantidad de apariciones de la letra", letra, "en la cadena es:", cantidad)

