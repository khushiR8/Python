q=[]

n=int(input('enter number of names:'))
for i in range(n):
    name=input(f'enter name {i+1}: ')
    q.append(name)
print(f'Lists of names: {q}')
print(f'\nQueue displayed from front to back:')
for i in q:
    print(i)

delete=int(input('\nenter names to be deleted:'))
for i in range(delete):
    if q:
        removed=q.pop(0) #remove element at the front
        print(f'deleted: {removed}')
    else:
        print(f'queue is empty')
        break
print()
for i in q:
    print(i)
    
    
    