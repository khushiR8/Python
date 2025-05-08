stack=[]


while True:
    n=int(input('enter a positive number:'))
    if n==0:
        break
    if n>0:
        stack.append(n)
print(stack)

for i in reversed(stack):
    print(i)
    