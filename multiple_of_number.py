def display(num):
    message=""
    if(num%3==0 and num%5==0):
        print("zoom")
    
    elif(num%5==0):
        print("zap")
    elif(num%3==0):
        print("zip")
    else:
        print("invalid")
    return message


message=display(9)
print(message)
