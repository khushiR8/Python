#Write a python program, using a switch statement, to check whether a year is a leap year or not.

i=0

for i in range(5):
    n=int(input('enter year :'))
    if n % 4 == 0:
      print(f'{n} is a leap year')
    else:
      print(f'{n} is not a leap year')