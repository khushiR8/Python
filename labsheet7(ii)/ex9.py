rows=int(input('enter number of rows:'))
cols=int(input('enter number of cols:'))
list=[]
for i in range(rows):
    column=[]
    for i in range(cols):
        words=str(input('enter words in the list:'))
        column.append(words)
    list.append(column)

for row in list:
    print(row)

for i in range(cols):
    for j in range(rows):
        print(list[j][i])