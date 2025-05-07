import random
rows=int(input('enter number of rows:'))
cols=int(input('enter number of columns:'))
matrix=[]
for i in range(rows):
    column=[]
    for i in range(cols):
        n=random.randint(0,100)
        column.append(n)
    matrix.append(column)
print(matrix)