#Note for a recursive function , always think a step back 
#For e.g to calculate the factorial of a number(3), we have to do 
#3!= 3*2*1 which can be written as 3! =3*(3-1) in other words n!=n*(n-1)

#A recursive program consists if:
#Base case : stop a certain condition
#Smaller case : call a smaller version of itself
#General case : If the recursive function works properly, the problem will be solved
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

#calling the function 
x=5
factorial=fact(x)
print(factorial)