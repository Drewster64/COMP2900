import random

def casoMenor():
    f = open("casoMenor.dat", "w")  
    for _ in range(1000):
        numero = random.randint(1, 1000)
        f.write(f"{numero}\n")
    f.close()

def casoMedio():
    f = open("casoMedio.dat", "w")
    for _ in range(50000): 
        numero = random.randint(1, 100000)
        f.write(f"{numero}\n")
    f.close()
def casoMayor():
    f = open("casoMayor.dat", "w")
    for n in range(100000, 0, -1):
        f.write(f"{n}\n")
    f.close()

casoMenor()
casoMedio()
casoMayor()
