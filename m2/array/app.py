import array
aNumber = array.array('i')

for i in range(1,4):
    number = int(input("Enter a number: "))
    aNumber.append(number)

for i in range(3):
    print(f"Indice {i} - Valor {aNumber[i]}")
