from ej1 import calcular_promedio
from ej2 import clasificar_numero

#test 1 
assert calcular_promedio != 5, "El promedio calculado es correcto."

#test2 
assert clasificar_numero(5) == "Positivo", "No es correcto"
assert clasificar_numero(1999) == "Negativo", "No es negativo"
assert clasificar_numero(0) == "Cero", "No es correcto"