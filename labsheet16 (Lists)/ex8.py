row=int(input('enter number of rows:'))
cols=int(input('enter number of columns:'))
l=[]
for i in range(row):
    column=[]
    for i in range(cols):
        n=int(input('enter a character:'))
        column.append(n)
    l.append(column)

print(l)