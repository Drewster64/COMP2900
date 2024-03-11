"""
6. Invertir una cadena de texto:
●	Función: invertir_cadena(cadena)
●	Parámetro: cadena (texto a invertir)
●	Devuelve: La cadena de texto invertida
"""

def invertir_cadena(cadena):
    invertida = ""
    for caracter in cadena:
        invertida = caracter + invertida
    return invertida

texto = input("Ingrese una cadena de texto: ")
texto_invertido = invertir_cadena(texto)
print("El texto invertido es:", texto_invertido)
