#7. Validar si una cadena de texto es un número entero:
#●	Función: es_numero_entero(cadena)
#●	Parámetro: cadena (texto a validar)
#●	Devuelve: True si la cadena es un número entero, False si no lo es

def es_numero_entero(cadena):
    return cadena.isdigit()
#isdigit() se encarga de verificar si los caracteres del texto son numeros enteros
# de no ser numero o no ser entero imprimará false

texto = input("Ingrese una cadena de texto: ")
if es_numero_entero(texto):
    print("TRUE")
else:
    print("FALSE")
