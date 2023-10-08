def silnia1(m):
    if m==0:
        return 1
    else:
        return m*silnia1(m-1)


for i in range(11):
    print("silnia z ",i, "to ",silnia1(i))