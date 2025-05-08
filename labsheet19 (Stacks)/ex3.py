#each player has 10 cards which can be arranged in any order
#cards are placed in a stack (top is the last card in the list)
#on each turn,the topmost card is popped and the higher card wins
#if both cards are equal, its a draw
import random
stack1=[]
stack2=[]

for i in range(10):
    x=random.randint(1,10)
    y=random.randint(1,10)
    stack1.append(x)
    stack2.append(y)
      
print(stack1)
print(stack2)

for i in reversed(stack1):
    print(f'person 1 cards from top to bottom : {i}')

print()
for i in reversed(stack2):
    print(f'person 2 cards from top to bottom : {i}')
print()
p1_score=0
p2_score=0
draw=0
for i in range(10):
    card1=stack1.pop()
    card2=stack2.pop()
    print(f'for turn {i+1}: Player 1 plays {card1}, Player 2 plays {card2}')
    if card1>card2:
        print(f'\nplayer 1 wins this turn')
        p1_score+=1
    elif card2>card1:
        print(f'\nplayer 2 wins this turn')
        p2_score+=1
    else:
        print('Draw')
        draw+=1
print(f'Player1 score: {p1_score}')
print(f'Player2 score: {p2_score}')
print(f'Number of draws: {draw}')

if p1_score>p2_score:
    print(f'Player 1 wins this game')
elif p2_score>p1_score:
    print(f'Player 2 wins this game')
else:
    print(f'it is a draw')
