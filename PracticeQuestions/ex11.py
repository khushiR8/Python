def countnum(L):
    evencount=0
    oddcount=0
    for i in range(len(L)):
        if L[i] % 2 ==0:
            print(f'even number')
            evencount+=1
        else:
            print(f'odd number')
            oddcount+=1
    return evencount,oddcount

n=int(input('enter length of list:'))
list=[]
for i in range(n):
    x=int(input('enter number to the list:'))
    list.append(x)

y=countnum(list)
print(y)