"""
•	Ejercicio 5: Combinaciones (Coeficiente binomial)
Escribe una función recursiva que calcule el coeficiente binomial 
o el número de combinaciones posibles de n elementos tomados de k en k (nCk). Luego, prueba tu función con diferentes valores de n y k.
"""
def coeficienteBinomial(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return coeficienteBinomial(n - 1, k - 1) + coeficienteBinomial(n - 1, k)
    
n = 8
k = 5
resultado = coeficienteBinomial(n, k)
print(f"El coeficiente binomial de {n} tomados de {k} es:", resultado)
