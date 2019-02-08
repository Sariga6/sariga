a=[]
n=int(input("how many elements to be displayed"))
if (n<1000 and n>=1):
    for i in range(0,n):
        c=int(input("enter the elements"))
        a.append(c)
b=sorted(a)
print(b)

