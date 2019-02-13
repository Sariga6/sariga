string=input("enter the sentence")
count=0
for a in string:
    if(a.isnumeric())==True:
        count=count+1
print(count)
