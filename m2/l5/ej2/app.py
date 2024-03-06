#2. Calcular el área de un triángulo:
#●	Función: area_triangulo(base, altura)
#●	Parámetros: base y altura (números)
#●	Devuelve: El área del triángulo

def area(base, altura):
    area = (base * altura) / 2
    return area

#Solicita el usuario los datos necesarios sobre la medida del triángulo
base = float(input("Ingrese la medida de la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

resultado = area(base, altura) #Calcula el área del triángulo utilizando la función area
print("El área del triángulo es:", resultado)
