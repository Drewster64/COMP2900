#8. Contar la cantidad de vocales en una cadena de texto:
#●	Función: contar_vocales(cadena)
#●	Parámetro: cadena (texto a analizar)
#●	Devuelve: La cantidad de vocales en la cadena de texto

def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    counter = 0
    for letra in cadena:
        if letra in 'aeiouAEIOU':
            counter += 1
    return counter

texto = input("Ingrese su cadena de texto: ")
cantVocales = contar_vocales(texto)
print("La cantidad de vocales en la cadena de texto es:", cantVocales)


