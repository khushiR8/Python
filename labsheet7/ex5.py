#Write a program that allows a user to input a number of integers in a list and
#then displays the smallest as well as the largest in the list.

list=[]

for i in range(1,6):
    n=int(input('enter a number :'))
    list.append(n)

list.sort()
print(list)  
print(f'smallest number :{list[0]}')
print(f'largest number :{list[-1]}')
  
#alternative way
#print(min(list))
#print(max(list))
