#Write a program that prompts the user to enter a given number and then prints all the
#divisors of the given number.

n=int(input('enter a number:'))

for i in range (1,n,1):
   if n % i == 0:
      print(i)
      