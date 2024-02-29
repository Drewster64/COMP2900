import array
aNumber = array.array('i')

for i in range(1,4):
    number = int(input("Enter a number: "))
    aNumber.append(number)

for i in range(3):
    print(f"Indice {i} - Valor {aNumber[i]}")

for n in aNumber:
    print(f"Valor {n}")

for i in range(len(aNumber)):
    print(f"indice {i} - Valor {aNumber[i]}")