#8. Contar la cantidad de vocales en una cadena de texto:
#●	Función: contar_vocales(cadena)
#●	Parámetro: cadena (texto a analizar)
#●	Devuelve: La cantidad de vocales en la cadena de texto

def contar_vocales(cadena):
    return sum(1 for letra in cadena.lower() if letra in 'aeiou')
#lower se encarga de cambiar el texto a minusculas para poder identificar las vocales utilizando el if aeiou
#independientemente de si estas son mayusculas o minusculas
#1 les asigna un valor para que posteriormente se sumen con Sum
#dando esto como resultado la cantidad de vocales en el texto

texto = input("Ingrese su cadena de texto: ")
cantVocales = contar_vocales(texto)#llamando la funcion
print("La cantidad de vocales en la cadena de texto es:", cantVocales)#Imprimiendo cantidad de vocales
