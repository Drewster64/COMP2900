#Calcular el máximo de dos números:
#●	Función: maximo(a, b)
#●	Parámetros: a y b (números)
#●	Devuelve: El máximo de a y b

print('Hola!')
def maximo(): #definiendo la función para determinar el máximo
    a = float(input("Ingrese el primer número: ")) 
    b = float(input("Ingrese el segundo número: "))
    if a > b:
        return a
    else:
        return b

resultado = maximo() #llamando la función para determinar el máximo
print("El máximo es de los números es:", resultado)
