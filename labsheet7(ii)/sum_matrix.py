matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total=0
for row in range(len(matrix)):
    for cols in range(len(matrix[row])):
        total+=matrix[row][cols]
print(f'Sum of matrix : {total}')
   
     
#row 0 [1,2,3]
#row 1 [4,5,6]
#row 2 [7,8,9]

# row[0],cols[0] =1
# row[0],cols[1] =2