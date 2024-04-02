"""
•	Ejercicio 4: Invertir una cadena
Escribe una función recursiva que invierta una cadena dada. Luego, prueba tu función con diferentes cadenas.
"""
def invertirCadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return invertirCadena(cadena[1:]) + cadena[0]
        """La recursiva se encarga de tomar el ultimo caracter y colocarlo en el primer lugar.
             repitiendo el proceso hasta haber recorrido toda la cadena de texto
         """

cadena = input("Ingresa la cadena de texto que desea invertir: ")

print("Cadena de texto original:", cadena)
print("Cadena de texto invertida:", invertirCadena(cadena))
