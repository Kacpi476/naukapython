def tax(number):
    podatek = 0
    if number <= 10000:
        podatek = 0
    elif number <=20000:
        number = number - 10000
        podatek = number*0.1
    else:
        podatek = 20000*0.1
        podatek += (number - 20000)*0.2
    print(podatek)


#tax(45000)


def przychod(income):
    podatek = int
    if income <= 10000:
        podatek = 0
    elif income <= 20000:
        podatek = (income-10000)*0.1
    else:
        podatek = (10000*0.1) + ((income-20000)*0.2)
    print(podatek)

przychod(45000)
        
