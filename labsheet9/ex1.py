num_Rows = int(input('Enter number of rows: '))
num_Columns = int(input('Enter number of columns:'))
my2dList = []
for i in range(num_Rows):
    cols = []
    for j in range(num_Columns):
        data = input('Enter Data: ')
        cols.append(data)
    my2dList.append(cols)
    
print(my2dList)    
