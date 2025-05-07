t=(('333', '33'), ('1416', '55'))
l=[]
for row in range(len(t)):
    column=[]
    for col in range(len(t[row])):
        column.append(int(t[row][col]))
    l.append(column)
        
newtuple=tuple(l)
print(newtuple)