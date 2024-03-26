lista = [10, 3, 4, 7, 2]

print (4 in lista) #O(1)

for number in lista: #O(n)
    if (number == 4):
        print("TRUE")

suma = 0
for number in lista #O(n)
    suma += number

for i in range (len(lista) -1): #O(n>2)
    for j in range (len(lista) -i -1):
        if lista [j] > lista