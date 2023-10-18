hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

rem=((mins+dura)%60)
hoursleft=(int(round((mins+dura)/60,0)))
if rem==0:
    rem ="00"
elif rem<10:
    print("Event ends at:",hour+hoursleft,":","0" + str(rem))
else:
    print("Event ends at:",hour+hoursleft,":",rem)
