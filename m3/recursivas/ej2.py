"""
•	Ejercicio 2: Potencia de un número
Escribe una función recursiva que calcule la potencia de un número base elevado a un exponente entero no negativo (base^exponente). Luego, prueba tu función con diferentes pares de base y exponente.
"""
def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)
"""la funcion potencia primero se encarga de ver si el exponente es = 0, de ser asi devuelve 1.
 Si el exponente es 1, devuelve el valor de la base. De no cumplir con ninguna de las opciones anteriores en el ciclo,
 la funcion procede a la recursiva, que se encarga de ir restandole 1 al valor de exponente hasta llegar a 0 o 1.
 Despues de finalizar la recursion, se realiza la multiplicacion para obtener el resultado
 """
base = int(input("Ingresa el valor de la base: "))
exponente = int(input("Ingresa el valor del exponente: "))

if exponente < 0:
    print("El exponente no puede ser negativo.")
else:
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la potencia {exponente} es igual a: {resultado}")