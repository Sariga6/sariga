n=int(input("enter the time in minutes"))
if(n>60):
    hour=n//60
    mins=n%60
    print(hour,mins)
else:
    print("0",n)
