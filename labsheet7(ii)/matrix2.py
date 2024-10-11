import random

matrix=[]
num_rows=int(input('enter number of rows'))
num_cols=int(input('enter number of cols'))

for row in range(0,num_rows):
    matrix.append([]) #add an empty row
    for column in range(0,num_cols):
        matrix[row].append(random.randint(0,100))
        
print(matrix)        