list=[]
n=int(input('enter number of elements:'))
count=0

for i in range(n):
    if count < n:
        x=int(input('enter a number:'))
        list.append(x)
        count+=1
    else:
        print('enter another value:')
        
print(list)        