import random

rnd=random.randint(1,9)
guess=None

while guess != rnd:
    guess=int(input('enter a number between 1 to 9 :'))
    if guess != rnd:
        print(f'Wrong guess,try again')
    else:
        print(f'correct guess :{guess}')