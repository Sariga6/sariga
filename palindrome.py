n=int(input("enter the number"))
temp=n
sum1=0
if(n<=1000):
    while(n!=0):
        r=n%10
        sum1=sum1*10+r
        n=n//10
    if(temp==sum1):
        print("yes")
    else:
        print("no")

