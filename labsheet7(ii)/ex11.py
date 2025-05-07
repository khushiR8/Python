n=int(input('enter length of list:'))
numbers=list(range(2,n)) #creates a list numbers from 2 to n-1
p=2 #initialise p=2 since 2 is the 1st prime number
while p*p<n: #remove multiples up to sqr n
    for i in range(2*p,n,p): #loop through multiples of p,starting from 2*p up to n
        if i in numbers: 
            numbers.remove(i)
    for j in numbers:
        if j>p:
            p=j
            break
    else:
        break
print(f'prime numbers less than {n} are :{numbers}')