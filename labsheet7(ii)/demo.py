rows=int(input('Enter number of rows:'))
cols=int(input('Enter number of columns:'))
list=[]
for i in range(rows):
    column=[]
    for j in range(cols):
        n=int(input('Enter numbers:'))
        column.append(n)
    list.append(column)
print(list)