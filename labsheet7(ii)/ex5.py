list=[]

for i in range(1,5):
    n=int(input('enter numbers :'))
    list.append(n)
    
print(f'list before sorting:{list}')    
list.sort()    
print(f'list after sorting:{list}')

print(f'Largest number :{list[-1]}')
print(f'Smallest number :{list[0]}')
    