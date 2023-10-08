year = int(input("Enter a year: "))

if year<=1581:
    print("Not within the Gregorian calendar period")
elif year%4!=0:
    print(year,"is a Common Year")
else:
    print(year,"is a Leap Year")


