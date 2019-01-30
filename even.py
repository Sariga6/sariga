n,q=map(int,input("enter the limit").split(' '))
if (n<=100000 and q<=100000):
    for i  in range(n+1,q):
        if i%2==0:
            print(i,end=" ")
