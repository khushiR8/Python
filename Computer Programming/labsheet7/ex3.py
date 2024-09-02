#Write a program that allows a user to 12 input float values in a list and
#compute and display the average of the input numbers.

list=[]

for i in range (1,13):
    n=float(input('enter a number :'))
    list.append(n)
    
for i in list:
    print(i,end=" ")    
    
sum_list=sum(list)    
print(f'sum of list :{sum_list}')

avg_list=sum_list/12
print(f'average of list :{avg_list}')

