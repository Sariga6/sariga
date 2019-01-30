n=int(input("enter the number"))
if n<=1000:
    for i in range(2,n):
        if(n%i==0):
            print("no")
            break
    else:
        print("yes")
