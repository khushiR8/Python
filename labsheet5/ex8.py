x=1
power=0

n=int(input('Enter a positive value of n:'))
if n < 0 :
    print(f'Incorrect value,try again')
else:
    print(f'correct value,continue')
    
while x <= 5:
    power=x**n
    print(f'Power of x is :{power}')
    x+=1
    

       