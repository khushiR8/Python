#ex6

msg=input("Enter celsius or fahrenheit :")

if (msg == "fahrenheit"):
    
    f=float(input("Enter temp in fahrenheit :"))
    c= (5*(f-32))/9
    print("Temperature in celsius is :",c)
    
else:
    c=float(input("Enter temp in celsius :"))
    f=((9*c)/5)+32
    print("Temperature in fahrenheit is :",f)