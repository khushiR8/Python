list=[]
n=int(input('enter the length of list:'))
for i in range(n):
    x=int(input('enter a number:'))
    list.append(x)
print(list)

l=list[0] #start comparing with position 0 in the list
s=list[0] 
for i in list:
    if i>l:
        l=i
    elif i<s:
        s=i   
print(l)
print(s)

#alternative way
# list.sort()
# print(f'largest:{list[-1]}')
# print(f'smallest:{list[0]}')
# print(f'{min(list)}')
# print(f'{max(list)}')