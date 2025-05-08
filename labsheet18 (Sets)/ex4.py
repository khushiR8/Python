person1=set()
person2=set()

while True:
    num1=int(input(f'enter sticker for person1:'))
    if num1==0:
        break
    person1.add(num1)
print(f'cards for person 1: {person1}')  
while True:
    num2=int(input(f'enter sticker person2:'))
    if num2==0:
        break
    person2.add(num2)
print(f'cards for person 2: {person2}')

x=person1-person2 #person1 has but person 2 doesnt
y=person2-person1 #person2 has but person 2 doesnt

n=min(len(x),len(y))  #calc number of exchanges possibles
print(f'\ncards available to exchange: {n}')
print(f'cards available for person1: {sorted(x)}')
print(f'cards available for person2: {sorted(y)}')