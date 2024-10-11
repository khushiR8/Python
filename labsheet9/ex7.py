def listing():
    list=[]
    for i in range(4):
        n=int(input('enter numbers :'))
        list.append(n)
    list.sort()
    return list

def largest(list):
    print(f'largest number:{list[-1]}')
    
numlist=listing()
largest(numlist)      