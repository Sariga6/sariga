lt=[]
n=int(input("enter the limit"))
if(n<=100000 and n>=1):
    for i in range(0,n):
        a=int(input("enter the element"))
        lt.append(a)
for j in range(len(lt)):
    print(lt[j],end=" ")
    print(j)
   
