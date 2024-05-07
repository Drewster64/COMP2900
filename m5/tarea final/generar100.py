import random
def lista100():
    f = open("100.dat", "w")  
    for _ in range(100):
        numero = random.randint(1, 100)
        f.write(f"{numero}\n")
    f.close()

lista100()