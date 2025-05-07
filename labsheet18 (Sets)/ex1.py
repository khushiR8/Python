s=set()
for i in range(10):
    n=int(input(f'enter number {i+1}: '))
    
    if n in s:
        print('same number input')
    else:
        s.add(n)
print(s)