def invertir_cadena(cadena):
    return ''.join(reversed(cadena))
#reversed invierte el texto y lo devuelve
#join junta el exto invertido en una cadena

texto = input("Ingrese una cadena de texto: ")
texto_invertido = invertir_cadena(texto)#llama funcion con texto para la cadena
print("El texto invertida es:", texto_invertido)