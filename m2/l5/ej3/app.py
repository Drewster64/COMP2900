#3. Convertir una temperatura de Fahrenheit a Celsius:
#●	Función: fahrenheit_a_celsius(fahrenheit)
#●	Parámetro: fahrenheit (temperatura en Fahrenheit)
#●	Devuelve: La temperatura en Celsius

# Definiendo la función y se aplica la fórmula de conversión de Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit): 
    return (fahrenheit - 32) * 5/9

#Le solicita al usuario la temperatura en grados Fahrenheit
tempFahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

tempCelsius = fahrenheit_a_celsius(tempFahrenheit) #Llamando la función
print("La temperatura en grados Celsius es:", tempCelsius)