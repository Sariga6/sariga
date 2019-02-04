N,A,D=map(int,input("enter the values of n,a,d").split(' '))
if N>=1 and D<=100000:
    s=((N/2)*((2*A)+(N-1)*D))
    print(int(s))
    
