#Write a python program that takes a number as input and prints its multiplication
#table up to 10.

i=1
n=int(input('enter a number :'))

print(f'Multiplication table for {n}')

for i in range(1,11):
  print(f'{n} * {i} = {i*n}')

