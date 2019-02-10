def merge(left,right):
    result=[]
    i,j=0,0
    while (i<len(left)) and (j<len(right)):
        if(left[i]<right[j]):
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    result=result+left[i:]
    result=result+right[j:]
    return result
def mergesort(a):
    if(len(a)<=1):
        return a
    mid=int(len(a)/2)
    left=mergesort(a[:mid])
    right=mergesort(a[mid:])
    return merge(left,right)
a=[]
n=int(input("enter how many elements to be displayed"))
if (n<1000 and n>=1):
    for i in range(0,n):
        c=int(input("enter the elements"))
        a.append(c)
print(mergesort(a))        
        

     
        
