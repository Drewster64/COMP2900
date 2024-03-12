#7. Validar si una cadena de texto es un número entero:
#●	Función: es_numero_entero(cadena)
#●	Parámetro: cadena (texto a validar)
#●	Devuelve: True si la cadena es un número entero, False si no lo es

def es_numero_entero(cadena):
    for numero in cadena:
        if numero < '0' or numero > '9':
            return False
    return True

def numEntero(cadena):
    for numero in cadena:
        if numero < '0' or numero > '9':
            return False
    return True

texto = input("Ingrese una cadena de texto: ")
if es_numero_entero(texto):
    print("TRUE")
else:
    print("FALSE")

