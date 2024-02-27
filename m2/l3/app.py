currentYear = int(input('Current Year: '))
birthYear = int(input('Birth Year: '))

def age():
    global currentYear
    global birthYear
    currentAge = currentYear - birthYear
    print(f'Your age is {currentAge}')

age()

