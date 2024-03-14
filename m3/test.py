from ej1 import calcular_promedio
from ej2 import clasificar_numero
from ej3 import imprimir_numeros
from ej4 import calcular_area_circulo
from ej5 import buscar_elemento
  
# test 1
assert calcular_promedio(4, 6) == 5, "El promedio calculado no es correcto."

# test 2 
assert clasificar_numero(5) == "Positivo", "La clasificación no es correcta."
assert clasificar_numero(-3) == "Negativo", "El valor NO es negativo."
assert clasificar_numero(0) == "Cero", "La clasificación no es correcta."

# test 3
assert imprimir_numeros() == 11, "El ciclo corrió correctamente"

# test 4 
import math
assert calcular_area_circulo(3) == math.pi, "El área calculadano es correcta."

#test 5
arreglo = [1, 2, 3, 4, 5]
assert buscar_elemento(arreglo, 3), "El elemento no fue encontrado cuando debería."
assert buscar_elemento(arreglo, 6), "El elemento no fue encontrado cuando no debería."