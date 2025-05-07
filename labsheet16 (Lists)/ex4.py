list=[]
n=int(input('enter the lenght of list:'))
for i in range(n):
    x=int(input('enter a number:'))
    list.append(x)
    
print(f'list before reverse:{list}')
list.reverse()
# newlist=list[::-1]
print(f'list after reverse:{list}')