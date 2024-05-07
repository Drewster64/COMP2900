def casoMenor():
    numeros = list(range(1, 1001))
    
    with open("casoMenor.dat", "w") as f:
        for numero in numeros:
            f.write(f"{numero}\n")

def casoMedio():
    numeros = list(range(1, 50001))
    
    with open("casoMedio.dat", "w") as f:
        for numero in numeros:
            f.write(f"{numero}\n")

def casoMayor():
    numeros = list(range(100000, 0, -1))
    
    with open("casoMayor.dat", "w") as f:
        for numero in numeros:
            f.write(f"{numero}\n")

casoMenor()
casoMedio()
casoMayor()
