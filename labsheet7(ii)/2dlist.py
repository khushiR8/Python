num_Rows = int(input('Enter number of rows: '))
num_Columns = int(input('Enter number of columns:'))
my2dList = []
for i in range(num_Rows): #loop through each row,starting with 0
    cols = [] #each time we are in a row,we start with an empty list to store data in each column 
    for j in range(num_Columns):
        data = input('Enter Data: ')
        cols.append(data) #appending data for each row
    my2dList.append(cols)
    
print(my2dList)
