"""
Ejercicio con Cadenas: Dada una lista de palabras, al menos 10, escribe una función que utilice 
búsqueda secuencial para determinar si una palabra dada está en la lista."""
def busquedaSecuencial(lista, objetivo):
    for posicion, palabra in enumerate(lista, start=1):
        if palabra == objetivo:
            print(f"La palabra '{objetivo}' se encuentra en la lista.")
            return posicion
    print(f"La palabra '{objetivo}' no se encuentra en la lista.")
    return -1 

lista = ["jose", "balvin", "bicicleta", "carro", "vaso", "laptop", "boligrafo", "piercing", "Nike", "Malik", "Inter"]
objetivo = input("Ingrese la palabra (en minusculas) que desea buscar en la lista: ")

resultado = busquedaSecuencial(lista, objetivo)

