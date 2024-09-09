#Write a program which produces a simple multiplication table of the following format 
#for integers in the range 1 to 9: 
#1 x 1 = 1  
#1 x 2 = 2 ...  
#9 x 9 = 81 

for i in range(1,10):
    for j in range(1,10):
        print(f'{i} x {j} = {i * j}')
        
