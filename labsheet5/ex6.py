import random

rnd=random.randint(1,100)
guess=None

while guess != rnd:
    guess=int(input('guess number between 1 and 100 :'))
    if guess < rnd:
        print('Too low! try again')
    elif guess > rnd:
        print('Too high!try again')
    else:
        print(f'Congrats correct number :{rnd}')
    

