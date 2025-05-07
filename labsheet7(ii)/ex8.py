rows=int(input('enter number of rows:'))
cols=int(input('enter number of columns:'))
list=[]
for i in range(rows):
    column=[]
    for i in range(cols):
        n=int(input('enter numbers:'))
        column.append(n)
    list.append(column)
print(list)

        