

def silnia(n):
    if n == 1:
        return n
    else:
        return n * silnia(n-1)


num=int(input("wprowadz liczbe"))

if num == 0:
    print("silnia 0 to 1")
elif num<0:
    print("blad")
else:
    print("silnia ",num, "to ", silnia(num))


#albo
def silnia1(m):
    if m==0:
        return 1
    else:
        return m*silnia1(m-1)
    
print(silnia1(5))

#ciag fibonaciego

def fibo(n):
    if n<=1:
        return n 
    else:
        return fibo(n-1)+fibo(n-2)
    
x=int(input("fibonaci liczba działań:"))
for i in range(x):
    print(fibo(i))
