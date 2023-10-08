for i in range(1,11):
    for k in range(1,11):
        print(i*k,end=" ")
    print()


for x in range(1,6):
    for y in range(1,x+1):
        print(x, end=" ")
    print(" ")

for x1 in range(6,0,-1):
    for y1 in range(0,x1-1):
        print(x1-1, end=" ")
    print(" ")


def potegowanie(liczba, potega):
    print(liczba**potega)

potegowanie(2,5)
potegowanie(5,4)

