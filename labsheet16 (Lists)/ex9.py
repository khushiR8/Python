row=int(input('enter number of rows:'))
cols=int(input('enter number of columns:'))
l=[]
for i in range(row):
    column=[]
    for i in range(cols):
        c=str(input('enter a character:'))
        column.append(c)
    l.append(column)

for row in l:
    print(row)

for i in range(cols):
    for j in range(row):
        print(l[j][i])