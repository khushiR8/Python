stack=[]
stack2=[]
while True:
    n=int(input('enter a positive number:'))
    if n>0:
        stack.append(n)
    else:
        break
print(stack)

while True:
    val=int(input('enter a value:'))
    if val>0:
        stack2.append(val)
    else:
        break
print(stack2)

found=False
for num in stack:
    if num>val:
        print(f'bottom value > than {val} is {num}')
        found=True
        break
if not found:
    print(f'no value > than {val} is found')