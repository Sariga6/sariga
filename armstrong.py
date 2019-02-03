def digits(s):
    power=len(str(n))
    return power
n=int(input("enter the number"))
sum1=0
temp=n
while temp!=0:
    r=temp%10
    r1=r**digits(n)
    sum1=sum1+r1
    temp=temp//10
if(n==sum1):
    print("yes")
else:
    print("no")
    
    
