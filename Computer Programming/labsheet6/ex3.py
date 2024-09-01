#Write a program to check if the input number 
# is a prime number.

prime=True
n=int(input('enter a number:'))

for i in range (2,n,1):
    if n % i == 0:
      prime=False
      
if prime:
    print(n,'is a prime number')
else:
    print(n,'is not a prime number')