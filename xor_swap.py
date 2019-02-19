a,b=map(int,input("enter 2 numbers to be swaped").split(' '))
a=a^b
b=a^b
a=a^b
print(a,b)
