"""
10. Contar la cantidad de apariciones de una letra en una cadena de texto:
●	Función: contar_apariciones_letra(cadena, letra)
●	Parámetros: cadena (texto a analizar) y letra (letra a buscar)
●	Devuelve: La cantidad de apariciones de la letra en la cadena de texto
"""

def contar_apariciones_letra(cadena, letra):

    cadenaMin = cadena.lower()
    letraMin = letra.lower()
    return cadenaMin.count(letraMin)
    """
    Metodo lower convertirá los valores asignados a minusculas para que el programa las reconozca independientemente de si 
    el usuario las ingresa la cadena de texto con minusculas o mayusculas.
    Metodo count permitirá contar las mismas dentro de la cadena 
    """

cadena = input("Ingrese una cadena de texto: ")
letra = input("Ingrese la letra que desea buscar: ")
cantidad = contar_apariciones_letra(cadena, letra)
print("La cantidad de apariciones de la letra", letra, "en la cadena es:", cantidad)
