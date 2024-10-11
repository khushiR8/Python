#Write a python program that input five integers in an array.The program counts the total number of even and odd numbers and display it.

array=[]

for i in range(1,6):
    n=int(input('enter a number :'))
    array.append(n)
print(f'Array of numbers :{array}')    

evencount=0
oddcount=0

for n in array:
    if n % 2 == 0:
        evencount += 1
    else:
        oddcount += 1
print(f'Even numbers :{evencount}')
print(f'Odd numbers :{oddcount}')
        