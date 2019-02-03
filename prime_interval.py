q,n=map(int,input("enter the range").split(' '))
if n<=100000:
    for j in range(q+1,n):
        for i in range(2,j):
            if(j%i==0):
                break
        else:
            print(j,end=' ')
