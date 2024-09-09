#Reverse list

list=[]

for i in range(1,6):
    n=int(input('enter an integer value :'))
    list.append(n)
    
print(f'List of numbers:{list}')
list.reverse()
print(f'List in reversed :{list}')    
    
    