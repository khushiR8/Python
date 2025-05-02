#To find the power, apply the same logic
#E.g if we have to find the power of 3^3
#3^3 is also 3^3 = 3*3^2 and so on
#so x^n = x*x^n-1


def power(x,n):
    if n==0:
        return 1
    else:
        return x * power(x,n-1)

y=3
z=3
calculatedPower=power(y,z)
print(calculatedPower)
    
